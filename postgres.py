import psycopg2


class PostgresSql:
    connection = None

    def __init__(self, database, user, password, host, port):
        self.user = user
        self.database = database
        self.password = password
        self.host = host
        self.port = port
        self.__connection()

    def __connection(self):
        self.connection = psycopg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

    def get_connection(self):
        return self.connection
