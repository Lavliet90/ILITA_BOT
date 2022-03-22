
def counting_user_messages(id_user):
    db_object.execute(f'UPDATE users SET messages = messages + 1 WHERE id = {id_user}')
    db_