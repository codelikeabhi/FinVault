from app import db

class Key(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_key = db.Column(db.Text, nullable=False)
    private_key = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Key {self.public_key}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
