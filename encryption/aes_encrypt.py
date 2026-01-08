from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt(value: str) -> bytes:
    return cipher.encrypt(value.encode())

def decrypt(token: bytes) -> str:
    return cipher.decrypt(token).decode()

if __name__ == "__main__":
    sample = "SensitiveData"
    encrypted = encrypt(sample)
    decrypted = decrypt(encrypted)

    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
