from app import db

class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cert_data = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Certificate {self.cert_data}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
