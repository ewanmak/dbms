from encryption.aes_encrypt import encrypt, decrypt

SENSITIVE_FIELDS = {"ssn", "credit_card"}

def encrypt_row(row: dict) -> dict:
    encrypted_row = {}
    for key, value in row.items():
        if key in SENSITIVE_FIELDS:
            encrypted_row[key] = encrypt(str(value))
        else:
            encrypted_row[key] = value
    return encrypted_row

def decrypt_row(row: dict) -> dict:
    decrypted_row = {}
    for key, value in row.items():
        if key in SENSITIVE_FIELDS:
            decrypted_row[key] = decrypt(value)
        else:
            decrypted_row[key] = value
    return decrypted_row


if __name__ == "__main__":
    sample = {
        "name": "Alice",
        "ssn": "123-45-6789",
        "credit_card": "4111111111111111"
    }

    enc = encrypt_row(sample)
    dec = decrypt_row(enc)

    print("Encrypted:", enc)
    print("Decrypted:", dec)
