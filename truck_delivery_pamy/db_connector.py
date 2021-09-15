import redis
import json


class DBConnector:
    def __init__(self):
        self.connection = None
        self.get_connection()

    def get_connection(self):
        if self.connection:
            return self.connection
        else:
            self.connection = redis.Redis(host="localhost",
                                          port=6379)
            return self.connection

    def save(self, id_save, object_to_save):
        encode_data = json.dumps(object_to_save)
        result_save = self.connection.set(id_save, encode_data)
        return result_save

    def get_by_id(self, id):
        result_get = self.connection.get(id)
        decode_data = json.loads(result_get)
        return decode_data
