import unittest
from backend.app import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_transaction(self):
        response = self.app.post('/create-transaction', json={
            'sender': 'Alice',
            'receiver': 'Bob',
            'amount': 1000,
            'transaction_details': 'Payment for services',
            'public_key': 'public_key_here'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Transaction created successfully', response.data.decode())

if __name__ == '__main__':
    unittest.main()
