from Crypto.Hash import SHA3_256

def sha3(message):
    # Tạo đối tượng SHA3-256
    sha3_hash = SHA3_256.new()
    # Cập nhật dữ liệu vào đối tượng SHA3-256
    sha3_hash.update(message)
    # Trả về giá trị hash dưới dạng byte
    return sha3_hash.digest()

def main():
    # Nhập chuỗi văn bản và mã hóa nó thành bytes
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    # Tính toán giá trị băm SHA3-256
    hashed_text = sha3(text)
    # In ra chuỗi văn bản ban đầu và giá trị băm SHA3-256 dưới dạng hex
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print("SHA-3 Hash:", hashed_text.hex())

# Kiểm tra và gọi hàm main
if __name__ == "__main__":
    main()
