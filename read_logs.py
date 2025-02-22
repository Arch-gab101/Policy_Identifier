import csv
import os.path
import pathlib


logs_path = pathlib.Path('/Users/tkhutswa/Documents/Policy_Identifier/Policy_Identifier/read_logs.py')

with open(logs_path, 'r') as log:
    data = log.read()
    
    print(data)
