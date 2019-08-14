"""
Module to test data format conversion
"""
import unittest
from collections import Counter
from .test_fixtures import (SAMPLE_XML,
                            SAMPLE_JSON,
                            SAMPLE_JSON_FOR_XML_TO_CSV,
                            SAMPLE_CSV,
                            CONVERTED_CSV_COLUMNS,
                            CONVERTED_CSV_VALUES)

from Transform.conversion_utils import Convert


class TestConversion(unittest.TestCase):
    """
    class to test data format conversion
    """
    converter = Convert()

    def test_xml_to_json_conversion(self) -> None:
        """
        Test if XML data is getting converted to XML as expected
        :return: <None>
        """
        parsed_xml_to_json = TestConversion.converter.xml_to_json(SAMPLE_XML)
        self.assertDictEqual(parsed_xml_to_json, SAMPLE_JSON)

    def test_json_to_csv_conversion(self) -> None:
        """
        Test if JSON data is getting converted to CSV as expected
        :return: <None>
        """
        parsed_json_to_csv = TestConversion.converter.json_to_csv(
            SAMPLE_JSON_FOR_XML_TO_CSV)
        self.assertDictEqual(parsed_json_to_csv, SAMPLE_CSV)

    def test_xml_to_csv_conversion(self) -> None:
        """
        Test if XML data is getting converted to CSV as expected
        :return: <None>
        """
        parsed_xml_to_csv = TestConversion.converter.xml_to_csv(SAMPLE_XML)

        columns = [column for column in parsed_xml_to_csv.get('columns')]
        values = [value for value in parsed_xml_to_csv.get('values')]

        self.assertTrue(sorted(columns) == sorted(CONVERTED_CSV_COLUMNS))
        self.assertTrue(sorted(values) == sorted(CONVERTED_CSV_VALUES))

