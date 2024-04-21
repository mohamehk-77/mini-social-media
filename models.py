from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    # relationship
    posts = db.relationship('Post', backref='author')
    # one user can have many posts

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.password = hash(password)

    @staticmethod
    def get_by_auth(field, value):
        return User.query.filter_by(**{field: value}).first()
