"""
Module contains code for storing XML to SQL DB
"""
import sys
import json
import os
sys.path.append('.')
import base64
from Taps.sql_taps import SQLTaps
from sqlalchemy.engine.result import ResultProxy


def get_config(config_file_name: str) -> dict:
    """
    Read the config file for main working file for database
    and put the data for connecting to the DB.
    :return:
    """
    with open(config_file_name, 'rb') as f:
        config = f.read()
        config_json = json.loads(config)
        return config_json


def write_blob(filename: str) -> ResultProxy:
    """
    Method to write the file to blob column of mysql.
    :param filename: <filename for reading>
    :return:
    """
    with open(filename, 'rb') as write_file:
        file = write_file.read()
        encoded_file = base64.b64encode(file)
        config = get_config('config.json')
        tapobj = SQLTaps(username=config.get('username'),
                         host=config.get('host'),
                         password=config.get('password'),
                         db_name=config.get('db_name'),
                         db_type=config.get('db_type'))

        xml_filename = filename.split('/')[::-1][0]

        conn = tapobj.get_connection()
        result = tapobj.get_rows(conn,
                                 'INSERT INTO StudentsData (id, '
                                 'filename, student_xml) '
                                 'values({id},\'{filename}\', '
                                 '\'{file}\');'.format(
                                     id=3, filename=xml_filename,
                                     file=encoded_file.decode()))
        return result


if __name__ == '__main__':
    write_blob(os.path.abspath('utils/student.xml'))
