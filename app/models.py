# from flask import jsonify

# from app import db

# class Vocabularies(db.Model):
    
#     index = db.Column(db.Integer, primary_key=True)
#     aceh = db.Column(db.String(150), nullable=True)
#     indonesia = db.Column(db.String(150), nullable=True)
#     english = db.Column(db.String(150), nullable=True)
#     jawoe = db.Column(db.String(150), nullable=True)

#     def __repr__(self):
#         return f'{self.aceh} | {self.indonesia} | {self.english}'


# class Examples(db.Model):
#     index = db.Column(db.Integer, primary_key=True)
#     aceh = db.Column(db.String(150), nullable=True)
#     contoh_aceh = db.Column(db.String(200), nullable=True)
#     contoh_indonesia = db.Column(db.String(200), nullable=True)
#     contoh_english = db.Column(db.String(200), nullable=True)
#     aceh_id = db.Column(db.Integer, nullable=True)

#     def __repr__(self):
#         return f'{self.aceh}: {self.contoh_aceh}: {self.contoh_indonesia}'
    