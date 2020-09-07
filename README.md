# csv-generator
A python script that takes model from a json file and generates a CSV using faker library in python

## Instalation
install faker using pip install faker (pip3 for linux)

## How to Use
1. Enter the model definition fo the csv file in modelDef.json file in the same directory
2. model definition is of type- 
```
[{
  "name": "loan_id",
  "type": "name",
  "unique": false,
  "defaultValue":null
},
{
  "name": "id",
  "type": "username",
  "unique": true
}]
```
name is column name in csv file
type is data type (supported data types are 'name', 'address', 'number', 'string','timestamp', 'date', 'email', 'username', 'boolean')
unique is whether the values in this column should be unique or not (takes value True or False)
defaultValue is the default value for this column...this same values will be in entire column in csv

3. run csv_faker.py using python 3

