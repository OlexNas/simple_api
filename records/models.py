from. extensions import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    tickers = db.relationship('Ticker')

    @classmethod
    def from_dict(cls, data):
        return User(
            name = data['name']
        )

    def __repr__(self):
        return f"User {self.name}"

class Ticker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(18))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



