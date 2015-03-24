import uuid
import hashlib
import time


class Hash:

    @staticmethod
    def create_message_object(message):

        md5 = hashlib.md5()
        md5.update(message['message'].encode('utf-8'))
        md5.hexdigest()

        arr = {"message": message, "method": "OUT", "args": {"time": time.time()}}

        data = {
            "message": message["message"],
            "uuid": uuid.uuid4(),
            "hash": md5
        }

        return data
