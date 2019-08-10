"""The file contains the Taps for SQL databases only."""
from sqlalchemy import create_engine, text
from sqlalchemy.engine.base import Connection
from sqlalchemy.engine.result import ResultProxy


class SQLTaps(object):
    """
    Class providing Taps for SQL databases.

    A generic function takes the following arguments:
    1. Db Type:
    2. Username:
    3. Password:
    4. DB Name:
    """

    def __init__(self, db_type: str,
                 username: str,
                 password: str,
                 db_name: str,
                 host: str) -> None:
        """
        Constructor for the SQLTaps class.
        :param db_type: <database server type: example : MySQL, Postgres, etc.>
        :param username: <username of the db user to connect to the db>
        :param password: <password of the db user to connect to the db>
        :param db_name: <database name which is to be used>
        :param host: <host on which db server is hosted>
        """
        self.db_type = db_type
        self.username = username
        self.password = password
        self.db_name = db_name
        self.host = host

        # constructing the database URL for which we need to connect to
        # and retrieve data
        self.db_URL = (self.db_type + "://" + self.username +
                       ":" + self.password + "@" + self.host +
                       "/" + self.db_name)

        # storing the DB engine object for further requirements
        self.db_engine = create_engine(self.db_URL, echo=True)

    def get_connection(self) -> Connection:
        """
        Get the connection object for specific database you are creating.
        :return:
        """
        return self.db_engine.connect()

    def get_rows(self, connection: Connection, query: str) -> ResultProxy:
        """
        Executes a raw SQL Query and returns the ResultProxy (ResultSet) object
        :param connection: <Connection object over which query to be executed>
        :param query: <Raw query to be executed using SQLAlchemy>
        :return: <ResultProxy object containing the required set of data>
        """
        raw_query = text(query)
        result = connection.execute(raw_query)
        return result

    def covert_ResultProxy_to_JSON(self, resultset: ResultProxy) -> dict:
        """
        Converts Result Proxy object data to a JSON data.
        :param resultset: <ResultProxy object to be converted to JSON>
        :return:
        """
        data_list = []
        result_keys = resultset.keys()

        for row in resultset:
            data_dict = {}
            for index in range(len(result_keys)):
                data_dict[result_keys[index]] = row[index]

            data_list.append(data_dict)

        return {'result': data_list}
