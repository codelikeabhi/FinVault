from flask import Flask, jsonify, request
from crypto.encryption import encrypt_data, decrypt_data
from models.transaction import Transaction
from models.key import Key
from models.certificate import Certificate
from backend.crypto.keygen import generate_keys

app = Flask(__name__)

@app.route('/create-transaction', methods=['POST'])
def create_transaction():
    data = request.json
    encrypted_data = encrypt_data(data['transaction_details'], data['public_key'])
    new_transaction = Transaction(
        sender=data['sender'],
        receiver=data['receiver'],
        amount=data['amount'],
        encrypted_details=encrypted_data
    )
    new_transaction.save()  # Assuming .save() persists the transaction to DB
    return jsonify({"message": "Transaction created successfully."}), 201


@app.route('/decrypt-transaction', methods=['POST'])
def decrypt_transaction():
    data = request.json
    transaction = Transaction.query.get(data['transaction_id'])
    decrypted_details = decrypt_data(transaction.encrypted_details, data['private_key'])
    return jsonify({"transaction_details": decrypted_details}), 200


@app.route('/generate-keypair', methods=['POST'])
def generate_keypair():
    keypair = generate_keys()
    new_key = Key(public_key=keypair['public'], private_key=keypair['private'])
    new_key.save()  # Store the key pair
    return jsonify({"public_key": keypair['public'], "private_key": keypair['private']}), 201


@app.route('/generate-certificate', methods=['POST'])
def generate_certificate():
    data = request.json
    cert = generate_certificate(data['public_key'])
    new_cert = Certificate(cert_data=cert)
    new_cert.save()  # Store the certificate
    return jsonify({"certificate": cert}), 201

if __name__ == '__main__':
    app.run(debug=True)
