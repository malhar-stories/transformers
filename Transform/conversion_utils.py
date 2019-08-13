"""
Module for handling data conversions
"""
import xmltodict
import json_flatten
import json
import csv


class Convert(object):
    """
    Class for handling data conversions
    """

    def xml_to_json(self, xml_input: str) -> dict:
        """
        method to handle the data conversion from XML format to JSON format
        :param xml_input:
        :return:
        """
        converted_json = xmltodict.parse(xml_input)
        return converted_json

    def json_to_xml(self, input_json: dict) -> str:
        """
        method to handle the data conversion from JSON to XML format
        :param input_json:
        :return:
        """
        pass

    def json_to_csv(self, input_json: dict) -> str:
        """
        method to handle the data conversion from JSON to CSV format
        :param input_json:
        :return:
        """
        csv_content = json_flatten.flatten(input_json)
        return csv_content

    def xml_to_csv(self, input_xml: str) -> dict:
        """
        Conversion for XML format to CSV format.
        For this conversion we will convert the XML into JSON first and then we
         will be converting that JSON to CSV format.

        Approach: XML -> JSON -> CSV

        :param input_xml:
        :return:
        """
        converted_json = xmltodict.parse(input_xml)
        converted_csv = json_flatten.flatten(converted_json)

        return {'columns': converted_csv.keys(),
                'values': converted_csv.values()}
