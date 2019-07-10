"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

#Make a hash and if it has the value then add the value
# loop through and find the largest value
# The phone number is in a form of a string

telephone_call_time = {}

for call_logs in calls:
    if call_logs[0] not in telephone_call_time:
        telephone_call_time[call_logs[0]] = 1
    else:
        telephone_call_time[call_logs[0]] += telephone_call_time.get(call_logs[0])

    if call_logs[1] not in telephone_call_time:
        telephone_call_time[call_logs[1]] = 1
    else:
        telephone_call_time[call_logs[1]] += 1
        
# print(type(calls[-1][0]))

print('TNumber spent the longest time, TotTime seconds, on the phone during September 2016.')

