"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

phone_numbers_set = set([])

for call_log in calls:
    phone_numbers_set.add(call_log[0])
    phone_numbers_set.add(call_log[1])

for text_log in texts:
    phone_numbers_set.add(text_log[0])
    phone_numbers_set.add(text_log[1])

print('There are {} different telephone numbers in the records.'.format(len(phone_numbers_set)))
