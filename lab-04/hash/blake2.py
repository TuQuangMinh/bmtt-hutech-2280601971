import hashlib

def blake2(message):
    # Khởi tạo đối tượng BLAKE2b với kích thước băm 64 bytes
    blake2_hash = hashlib.blake2b(digest_size=64)
    # Cập nhật dữ liệu vào đối tượng hash
    blake2_hash.update(message)
    # Trả về giá trị băm dưới dạng byte
    return blake2_hash.digest()

def main():
    # Nhập chuỗi văn bản và mã hóa nó thành bytes
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    # Tính toán giá trị băm BLAKE2
    hashed_text = blake2(text)
    # In ra chuỗi văn bản ban đầu và giá trị băm BLAKE2 dưới dạng hex
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print("BLAKE2 Hash:", hashed_text.hex())

# Kiểm tra và gọi hàm main
if __name__ == "__main__":
    main()
