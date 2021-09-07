from abc import ABCMeta


class Logger(metaclass=ABCMeta):
    def __init__(self):
        pass


class DBConnector(metaclass=ABCMeta):
    def __init__(self):
        pass


class MongoDBConnector(DBConnector):
    def __init__(self):
        super(MongoDBConnector, self).__init__()



class MySqlConnector(DBConnector):
    def __init__(self):
        super(MongoDBConnector, self).__init__()



class ContentManager:
    def __init__(self, logger=None, db_connection=None):
        self.logger = logger
        self.db_connection = db_connection

    def list_content(self, type):
        self.logger.debug("listing objects of the type")
        self.db_connection.get_multi()

    def save_content(self, object):
        self.db_connection.save(object)

    def delete_content(self, object_id, type=None):
        if type and not object_id.startswith(object_id):
            object_id = f"{type}{object_id}"
        self.db_connection.delete(object_id)


logger = Logger()
db_conn = MongoDBConnector()
my_sql_connector = MySqlConnector()

content_manager = ContentManager(logger=logger, db_connection=my_sql_connector)
