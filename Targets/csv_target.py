"""
Module for CSV file handling and for Target csv
"""
import csv


def csv_target(output_filename: str,
               data_rows: list,
               headers: list = []) -> None:
    """
    This function will write the provided content to csv file.
    :param output_filename: <Filename in which data to be written>
    :param headers: <Headers for the file to be written>
    :param data_rows: <The input data to be written in the file>
    :return: None
    """
    with open(output_filename, 'w+') as output_csv:
        csv_writer = csv.writer(output_csv,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow(headers)

        for row in data_rows:
            csv_writer.writerow(row)
