# imports
import json
import string
import random
import csv
from decimal import Decimal
from faker import Faker
fake = Faker()
from constants import columns, valid_datatypes

# number of rows to generate in csv
RECORD_COUNT = 50000

model_definition = open('modelDef.json',)
model_definition = json.load(model_definition)

total_columns=[]
unique_columns={}

def generate_data(type):
    if type.get('defaultValue',False):
        return type['defaultValue']
    if type['type'] =='name':
        return fake.name()
    if type['type']=='email':
        return fake.email()
    if type['type'] =='address':
        return fake.address()
    if type['type']=='string':
        length = random.randint(int(type['minLength']), int(type['maxLength']))
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))
    if type['type'] =='timestamp':
        return fake.date_time()
    if type['type']=='date':
        return fake.date()
    if type['type'] =='username':
        username=fake.name()
        username=username.replace(' ','')
        username+=str(fake.random_int(min=1, max=10000))
        return username
    if type['type'] =='boolean':
        flag = random.randint(1, 2)
        if flag == 1:
            return True
        else:
            return False
    if type['type'] =='number':
        flag = random.randint(1, 2)
        if flag == 1:
           return fake.random_int(min=int(type['minValue']), max=int(type['maxValue']))
        else:
            return f'{fake.random_int(min=int(type["minValue"]), max=int(type["maxValue"]))}.{fake.random_int(min=1,max=99)}'

for i in range(len(model_definition)):
    column=model_definition[i]
    if(column['type'] not in valid_datatypes):
        raise Exception(f'not a valid datatype at {i} for further infrmation see docs')
    column['minLength']=column.get('minLength','3')
    column['maxLength']=column.get('maxLength','10')
    column['minValue']=column.get('minValue','100')
    column['maxValue']=column.get('maxValue','100000000')
    model_definition[i]=column
    total_columns.append(column['name'])
    if column.get('unique')==True:
        unique_columns[column['name']]= set()
        while len(unique_columns[column['name']])<RECORD_COUNT:
            unique_columns[column['name']].add(generate_data(column))

for i in unique_columns:
    unique_columns[i]=list(unique_columns[i])

def create_csv_file():
    with open('./testData.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=total_columns, delimiter='|')
        writer.writeheader()
        for i in range(RECORD_COUNT):
            row={}
            for j in model_definition:
                if j['unique']==True:
                    row[j['name']]=unique_columns[j['name']][i]
                else:
                    row[j['name']]=generate_data(j)
            writer.writerow(row)

create_csv_file()

