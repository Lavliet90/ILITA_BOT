from main import db_object, db_connection


class UpdateMessages:
    def update_messages_count(self, user_id):
        '''
        Count messages from users
        '''
        db_object.execute(f'SELECT id FROM slawe WHERE id = {self.user_id}')
        result = db_object.fetchone()
        if not result:
            return
        else:
            db_object.execute(f'UPDATE slawe SET messages = messages + 1 WHERE id = {self.user_id}')
            db_connection.commit()

    def top_10_stats(self, result):
        '''
        Top 10 by number of messages
        '''
        if not self.result:
            return 'Нет данных...'
        else:
            reply_message = '- Топ флудеров:\n'
            for i, item in enumerate(self.result):
                reply_message += f'{i + 1}: {item[2].strip()} - {item[1]} messages.\n'
            return reply_message
