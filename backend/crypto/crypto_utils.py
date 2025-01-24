from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import os

def generate_rsa_key_pair():
    """Generates an RSA key pair and returns the private & public keys."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_pem, public_pem

def encrypt_message(message: str, public_key):
    """Encrypts a message using the given public key."""
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=SHA256()),
            algorithm=SHA256(),
            label=None
        )
    )
    return base64.b64encode(encrypted).decode()

def decrypt_message(encrypted_message, private_key):
    """Decrypts an encrypted message using the given private key."""
    encrypted_message = base64.b64decode(encrypted_message)
    decrypted = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=SHA256()),
            algorithm=SHA256(),
            label=None
        )
    )
    return decrypted.decode()

def generate_symmetric_key():
    """Generates a symmetric AES key."""
    key = os.urandom(32)  # AES-256
    return key

def encrypt_symmetric_message(message: str, key):
    """Encrypts a message using AES symmetric encryption."""
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    iv = os.urandom(16)  # Initialization vector
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(message.encode()) + encryptor.finalize()
    return base64.b64encode(iv + encrypted_message).decode()

def decrypt_symmetric_message(encrypted_message, key):
    """Decrypts a symmetric encrypted message."""
    encrypted_message = base64.b64decode(encrypted_message)
    iv = encrypted_message[:16]  # Extract IV
    encrypted_data = encrypted_message[16:]  # Encrypted message
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_data) + decryptor.finalize()
    return decrypted_message.decode()

def sign_message(message: str, private_key):
    """Signs a message using RSA private key."""
    signature = private_key.sign(
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return base64.b64encode(signature).decode()

def verify_signature(message: str, signature: str, public_key):
    """Verifies a signature using RSA public key."""
    try:
        signature = base64.b64decode(signature)
        public_key.verify(
            signature,
            message.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        return False
