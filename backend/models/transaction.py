from app import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100), nullable=False)
    receiver = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    encrypted_details = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Transaction {self.sender} -> {self.receiver} for {self.amount}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
