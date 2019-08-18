# transformers

##getting Started
This library will primarily will be used for data conversion and loading.
Currently SQL taps are ready to use. As well as data conversion from 
XML to JSON, XML to CSV, JSON to CSV conversion is also available.

One can load the data to csv using this particular library to CSV.

## Install
This is for linux based systems (it may work with mac too)

**Create virtual environment**
```
$ virtualenv -p python3.7 eltenv
$ source etlenv/bin/activate
``` 

**clone the library inside your virtualenv folder**
```markdown
$ git clone <library url>
$ cd transformers
```

**Install requirements to virtual environment**
```markdown
$ pip install -r requirements.txt
```

## Usage

The usage config is provided with the library. One will need to edit it 
if the SQL Taps or Targets are to be used. The sample data is provided.

Files etl_operations.py is containing the working logic of fetching xml data 
from database and storing it into CSV file.

**command for using etl_operations.py**
```
$ python etl_operations.py
``` 

## Taps

**Currently only SQL taps are created.** So to use them one can follow below 
approach.

```python
from Taps.sql_taps import SQLTaps

sql_obj = SQLTaps(db_type='<db_type>', username='<username>', 
                  password='<password>', host='<host>', 
                  db_name='<db_name>')

# create connection object for SQL DB
connection = sql_obj.get_connection()

# fetch data from DB
data = sql_obj.get_rows(connection, query='<your query>')

# (if required) convert dataset to JSON
json_data = sql_obj.covert_ResultProxy_to_JSON(data)
```


## Data conversion

Currently only data conversion for 
**XML to JSON, XML to CSV and JSON to CSV** are available.
Using it as follows:
```python
from Transform.conversion_utils import Convert

converter = Convert()

xml_to_json = converter.xml_to_json('<xml/>')
xml_to_csv = converter.xml_to_csv('<xml/>')
json_to_csv = converter.json_to_csv({'key': 'value'})
```

## Targets

Currently only CSV tap is available.

Using it as follows:

```python
from Targets.csv_target import csv_target

csv_target(output_filename='sample.csv',
           data_rows=['data', 'rows'], 
           headers=['optional', 'list', 'of', 'headers'])
```


## Tests

To run the test cases use following command:
```
$ python -m unittest tests
```