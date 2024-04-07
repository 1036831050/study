from cryptography.fernet import Fernet

# 生成一个随机的密钥
def generate_key():
    return Fernet.generate_key()

# 使用给定的密钥加密文本
def encrypt_text(key, text):
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(text.encode())
    return encrypted_text

# 使用给定的密钥解密文本
def decrypt_text(key, encrypted_text):
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    return decrypted_text

# 生成密钥
key = generate_key()

def read_file(path):
    with open(path, 'rb') as file:
        return file.read()

# 加密文本
text_to_encrypt = read_file(r"F:\git\study\vscode\python\metgetoffmpeg.py")
encrypted_text = encrypt_text(key, text_to_encrypt)
print("Encrypted text:", encrypted_text)

# 解密文本
decrypted_text = decrypt_text(key, encrypted_text)
print("Decrypted text:", decrypted_text)
# 保存密钥到文件
with open('key.key', 'wb') as key_file:
    key_file.write(key,"F:\git\study\vscode\python\metgetoffmpeg.py")