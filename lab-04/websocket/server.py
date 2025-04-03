import random
import tornado.ioloop
import tornado.web
import tornado.websocket

# Lớp WebSocketServer xử lý kết nối WebSocket
class WebSocketServer(tornado.websocket.WebSocketHandler):
    clients = set()

    def open(self):
        # Thêm client mới vào danh sách
        WebSocketServer.clients.add(self)

    def on_close(self):
        # Xóa client khỏi danh sách khi đóng kết nối
        WebSocketServer.clients.remove(self)

    @classmethod
    def send_message(cls, message: str):
        print(f"Sending message {message} to {len(cls.clients)} client(s).")
        for client in cls.clients:
            client.write_message(message)

# Lớp RandomWordSelector chọn một từ ngẫu nhiên từ danh sách
class RandomWordSelector:
    def __init__(self, word_list):
        self.word_list = word_list

    def sample(self):
        # Chọn một từ ngẫu nhiên từ danh sách
        return random.choice(self.word_list)

def main():
    # Tạo ứng dụng Tornado WebSocket
    app = tornado.web.Application(
    [(r"/websocket/", WebSocketServer)], 
     websocket_ping_interval=10, 
    websocket_ping_timeout=30,
    )
    
    app.listen(8888)

    # Khởi tạo IOLoop
    io_loop = tornado.ioloop.IOLoop.current()

    # Khởi tạo RandomWordSelector với danh sách từ ngẫu nhiên
    word_selector = RandomWordSelector(['apple', 'banana', 'orange', 'grape', 'melon'])

    # Khởi tạo PeriodicCallback để gửi từ ngẫu nhiên mỗi 3 giây
    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda: WebSocketServer.send_message(word_selector.sample()), 3000
    )
    periodic_callback.start()

    # Bắt đầu vòng lặp IOLoop
    io_loop.start()

if __name__ == "__main__":
    main()
