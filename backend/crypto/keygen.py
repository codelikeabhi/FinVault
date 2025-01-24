from cryptography.fernet import Fernet

def generate_keys():
    key = Fernet.generate_key()
    return {"public": key, "private": key}  # For simplicity, both public and private are the same in this example
