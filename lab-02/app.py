from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText'].strip()  # Xóa khoảng trắng ở đầu và cuối
    key = int(request.form['inputKeyPlain'])
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText'].strip()  # Xóa khoảng trắng ở đầu và cuối
    key = int(request.form['inputKeyCipher'])
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText'].strip()  # Xóa khoảng trắng ở đầu và cuối
    key = request.form['inputKey'].strip()  # Chìa khóa cho Playfair
    playfair = PlayFairCipher()  # Sử dụng lớp PlayFairCipher
    playfair_matrix = playfair.create_playfair_matrix(key)  # Tạo ma trận Playfair từ chìa khóa
    encrypted_text = playfair.playfair_encrypt(text, playfair_matrix)  # Gọi phương thức mã hóa của Playfair
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText'].strip()  # Xóa khoảng trắng ở đầu và cuối
    key = request.form['inputKey'].strip()  # Chìa khóa cho Playfair
    playfair = PlayFairCipher()  # Sử dụng lớp PlayFairCipher
    playfair_matrix = playfair.create_playfair_matrix(key)  # Tạo ma trận Playfair từ chìa khóa
    decrypted_text = playfair.playfair_decrypt(text, playfair_matrix)  # Gọi phương thức giải mã của Playfair
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# RailFence Cipher
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain']) 
    rail_fence_cipher = RailFenceCipher()
    encrypted_text = rail_fence_cipher.rail_fence_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])  # Rail Fence key là số nguyên
    rail_fence_cipher = RailFenceCipher()
    decrypted_text = rail_fence_cipher.rail_fence_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

#vigenere
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']  # Vigenère key là chuỗi
    vigenere_cipher = VigenereCipher()
    encrypted_text = vigenere_cipher.vigenere_encrypt(text, key)  # GỌI ĐÚNG HÀM
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']  # Vigenère key là chuỗi
    vigenere_cipher = VigenereCipher()
    decrypted_text = vigenere_cipher.vigenere_decrypt(text, key)  # GỌI ĐÚNG HÀM
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)