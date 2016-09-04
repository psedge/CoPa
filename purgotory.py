def send_message(message):
    if config['addr'] is None:
        return

    data = Hash.create_message_object(message)

    messages.append(data)

    for part in Packer.split(message['message'], settings.PACKET_LENGTH):

        crypto = Encryption(part)
        encrypted_data = crypto.encrypt_data()

        socket.post_connection(encrypted_data, config['addr'])

socket = SocketHandler(log, lambda x, y: new_connection(x, y))


# def new_connection(data, addr):
#     message = Encryption.decrypt_data(data)
#     gui.receive(message, addr)
