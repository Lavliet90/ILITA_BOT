class RepliesToMessages:
    '''
    Catches user messages andanswers a couple of catchphrases from the gachi
    '''

    def sosi(message):
        if 'соси' in message.text.lower() or 'sosi' in message.text.lower() or \
                'саси' in message.text.lower() or 'sasi' in message.text.lower():
            return f'Сам соси, {message.from_user.first_name}'
            # Только для беседы, в личке не from_user, a chat
        elif 'извини' in message.text.lower() or 'sorry' in message.text.lower() \
                or 'прости' in message.text.lower() or 'прошу прощения' in message.text.lower():
            return f'Sorry for what, {message.from_user.first_name}?'
        else:
            return
