"""
This file contains the final operations for required ETL operations.
i.e. fetching XML content from mySQL database and writing it in CSV file as
required.
"""
import base64
from Taps.sql_taps import SQLTaps
from Targets.csv_target import csv_target
from Transform.conversion_utils import Convert


def etl_operations():
    """
    Retquired operations for ETL XML to CSV.
    :return:
    """
    tap = SQLTaps(db_type='mysql',
                  username='root',
                  password='',
                  host='localhost',
                  db_name='ETLtestDb')

    conn = tap.get_connection()

    query = 'SELECT id, filename, student_xml FROM StudentsData'

    rows = tap.get_rows(conn, query)

    rows_json = tap.covert_ResultProxy_to_JSON(rows)

    result_list = rows_json.get('result')
    converter = Convert()

    csv_row_list = list()

    headers = list()

    for row in result_list:
        xml_content = base64.b64decode(row.get('student_xml').encode())
        csv_content = converter.xml_to_csv(xml_content)
        headers = csv_content.get('columns')
        csv_row_list.append(csv_content.get('values'))

    csv_target('students.csv', csv_row_list, headers)


if __name__ == '__main__':
    etl_operations()
