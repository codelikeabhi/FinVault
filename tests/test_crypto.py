import unittest
from backend.crypto.encryption import encrypt_data, decrypt_data
from backend.crypto.keygen import generate_keys

class TestEncryption(unittest.TestCase):

    def test_encryption_decryption(self):
        keys = generate_keys()
        data = "Sensitive Financial Data"
        encrypted_data = encrypt_data(data, keys['public'])
        decrypted_data = decrypt_data(encrypted_data, keys['private'])
        self.assertEqual(decrypted_data, data)

if __name__ == '__main__':
    unittest.main()
