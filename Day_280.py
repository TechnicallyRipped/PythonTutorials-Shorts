

# pip install cryptography 

from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(f"Key: {key}")

cipher = Fernet(key)

text_to_encrypt = "Secret message!"

encrypted_text = cipher.encrypt(text_to_encrypt.encode())

print(f"Original Text: {text_to_encrypt}")
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = cipher.decrypt(encrypted_text).decode()

print(f"Decrypted Text: {decrypted_text}")









