import hashlib

def calculate_sha256_hash(data):
    # Khởi tạo đối tượng SHA-256
    sha256_hash = hashlib.sha256()
    # Cập nhật đối tượng hash với dữ liệu được chuyển đổi thành bytes
    sha256_hash.update(data.encode('utf-8'))
    # Trả về giá trị hash dưới dạng chuỗi hex
    return sha256_hash.hexdigest()

# Nhập dữ liệu cần hash
data_to_hash = input("Nhập dữ liệu để hash bằng SHA-256: ")
# Tính giá trị hash của dữ liệu
hash_value = calculate_sha256_hash(data_to_hash)
# In ra kết quả
print("Giá trị hash SHA-256:", hash_value)
