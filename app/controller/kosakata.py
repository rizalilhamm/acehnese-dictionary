from app import db
from app.models import Vocabularies

def buat_kosakata_baru(aceh, indonesia, english):
    kata_baru = Vocabularies(aceh=aceh, real_aceh=None, indonesia=indonesia, english=english)
    db.session.add(kata_baru)
    db.session.commit()