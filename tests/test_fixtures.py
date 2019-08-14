"""
This module will contains all the constants which are required for
running test cases.
"""
import collections

SAMPLE_XML = b'<student>' \
             b'<name first="Devendu" middle="Kodand" last="Deodhar"/>' \
             b'<class>' \
             b'<stream>Computer Science</stream>' \
             b'<level>PHD</level>' \
             b'<year>First year</year>' \
             b'</class>' \
             b'</student>'

SAMPLE_JSON = collections.OrderedDict(
    [('student', collections.OrderedDict(
        [('name', collections.OrderedDict(
            [('@first', 'Devendu'),
             ('@middle', 'Kodand'),
             ('@last', 'Deodhar')])), (
            'class', collections.OrderedDict(
                [('stream', 'Computer Science'),
                 ('level', 'PHD'),
                 ('year', 'First year')]))]))])

SAMPLE_JSON_FOR_XML_TO_CSV = {
    'student': {
        'name': {
            'first': 'Shounak',
            'middle': 'Girish',
            'last': 'Joshi'
        },
        'class': {
            'stream': 'Computer Science',
            'level': 'Under Graduate',
            'year': 'First year'
        }
    }
}

SAMPLE_CSV = {'student.name.middle': 'Girish',
              'student.class.level': 'Under Graduate',
              'student.name.first': 'Shounak',
              'student.class.stream': 'Computer Science',
              'student.class.year': 'First year',
              'student.name.last': 'Joshi'}

CONVERTED_CSV_COLUMNS = ['student.class.stream', 'student.name.@middle', 'student.name.@first', 'student.class.level', 'student.class.year', 'student.name.@last']

CONVERTED_CSV_VALUES = ['Kodand', 'First year', 'Deodhar', 'PHD', 'Computer Science', 'Devendu']
