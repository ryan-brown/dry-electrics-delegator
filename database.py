from app.models import User, Update, DBSession

def batch_insert_update(updates):
  with DBSession() as session:
    session.bulk_save_objects(list(map(lambda update: Update(**update), updates)))
    session.commit()

def get_user_updates(username):
  with DBSession() as session:
    user = session.query(User).filter(User.username == username).first()
    return session.query(Update).filter(Update.user_id == user.id).all()
