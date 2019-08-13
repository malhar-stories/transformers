"""
Module contains code for storing XML to SQL DB
"""
import sys
sys.path.append('.')
import base64
from Taps.sql_taps import SQLTaps


def write_blob(filename):
    """
    Method to write the file to blob column of mysql.
    :param filename:
    :return:
    """
    with open(filename, 'rb') as write_file:
        file = write_file.read()
        encoded_file = base64.b64encode(file)
        tapobj = SQLTaps(username='root', host='localhost', password='',
                         db_name='ETLtestDb', db_type='mysql')
        xml_filename = filename.split('/')[::-1][0]

        conn = tapobj.get_connection()
        import pdb;
        pdb.set_trace()
        result = tapobj.get_rows(conn,
                                 'INSERT INTO StudentsData (id, '
                                 'filename, student_xml) '
                                 'values({id},\'{filename}\', \'{file}\');'.format(
                                     id=2, filename=xml_filename,
                                     file=encoded_file.decode()))
        return result


if __name__ == '__main__':
    write_blob('/home/shounk/own_projects/ETL/etlenv/transformers/utils'
               '/student.xml')
