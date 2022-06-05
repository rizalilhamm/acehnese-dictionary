import os
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from flask_login import UserMixin
from app import db

class User(UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    role = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return self.email

    def create_hashed_password(self, new_password):
        self.password = generate_password_hash(new_password, method='sha256')
    
    def verify_hashed_password(self, password):
        return check_password_hash(self.password, password)