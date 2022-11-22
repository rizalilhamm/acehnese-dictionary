from flask import jsonify
from datetime import datetime
from app import db

class Vocabularies(db.Model):
    
    index = db.Column(db.Integer, primary_key=True)
    aceh = db.Column(db.String(150), nullable=True)
    indonesia = db.Column(db.String(150), nullable=True)
    english = db.Column(db.String(150), nullable=True)
    jawoe = db.Column(db.String(150), nullable=True)

    def __repr__(self):
        return f'{self.aceh} | {self.indonesia} | {self.english}'


class Examples(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    aceh = db.Column(db.String(150), nullable=True)
    contoh_aceh = db.Column(db.String(200), nullable=True)
    contoh_indonesia = db.Column(db.String(200), nullable=True)
    contoh_english = db.Column(db.String(200), nullable=True)
    aceh_id = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'{self.aceh}: {self.contoh_aceh}: {self.contoh_indonesia}'

    
# class dictionaries(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     kategori = db.Column(db.String(255), nullable=False)
#     aceh = db.Column(db.String(255), nullable=False)
#     inggris = db.Column(db.String(255), nullable=False)
#     deskripsi = db.Column(db.String(255), nullable=True)
#     gambar = db.Column(db.String(255), nullable=True)
#     audio = db.Column(db.String(255), nullable=True)
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


# class users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     email = db.Column(db.String(255), nullable=False)
#     email_verified_at = db.Column(db.DateTime, nullable=True)
#     password = db.Column(db.String(255), nullable=False)
#     remmeber_token = db.Column(db.String(255), nullable=True)
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


# class vocabulary_requests(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     kosakata = db.Column(db.String(255), nullable=False)
#     bahasa_tujuan = db.Column(db.String(255), nullable=False)
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# class vocabulary_sugestions(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     aceh = db.Column(db.String(255), nullable=False)
#     indonesia = db.Column(db.String(255), nullable=False)
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)