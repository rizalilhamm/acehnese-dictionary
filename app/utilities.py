from app import db
from app.models import Vocabularies, Examples


def new_vocabulary(payload):
    index = len(Vocabularies.query.all()) + 1
    aceh = payload['aceh']
    real_aceh = payload['real_aceh']
    indonesia = payload['indonesia']
    english = payload['english']

    if 'aceh' not in payload or payload['aceh'].strip() == '':
        return 'Aceh word must inisialized, click back button to re-write the form!'
    if 'real_aceh' not in payload or payload['real_aceh'].strip() == '':
        return 'Real Aceh word must inisialized, click back button to re-write the form!'
    if 'indonesia' not in payload or payload['indonesia'].strip() == '':
        return 'Indonesian word must inisialized, click back button to re-write the form!'
    if 'english' not in payload or payload['english'].strip() == '':
        return 'English word must inisialized, click back button to re-write the form!'
    
    if 'jawoe' in payload and payload['jawoe'] != None:
        jawoe = payload['jawoe']
        new_vocabulary = Vocabularies(index=index, aceh=aceh, real_aceh=real_aceh, indonesia=indonesia, english=english, jawoe=jawoe)
    else:
        new_vocabulary = Vocabularies(index=index, aceh=aceh, real_aceh=real_aceh, indonesia=indonesia, english=english)
    
    db.session.add(new_vocabulary)
    db.session.commit()

    return f'{new_vocabulary.aceh} created!'


def new_example(aceh_id, aceh_word, payload):
    aceh = Vocabularies.query.filter_by(index=aceh_id, aceh=aceh_word).first()
    if aceh is None:
        return '404: NOT FOUND. click back button to fill the form'

    index = len(Examples.query.all()) + 1
    new_example = Examples(
        index = index,
        aceh = aceh.aceh,
        contoh_aceh = payload['contoh_aceh'] or '',
        contoh_indonesia = payload['contoh_indonesia'] or '',
        contoh_english = payload['contoh_english'] or '',
        aceh_id = aceh.index
    )
    db.session.add(new_example)
    db.session.commit()

    return f'{new_example} added for {aceh}!'