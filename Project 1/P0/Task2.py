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

telephone_call_time = {}

for call_logs in calls:
    if call_logs[0] not in telephone_call_time:
        telephone_call_time[call_logs[0]] = int(call_logs[-1])
    else:
        telephone_call_time[call_logs[0]] += int(call_logs[-1])
    
    if call_logs[1] not in telephone_call_time:
        telephone_call_time[call_logs[1]] = int(call_logs[-1])
    else: 
        telephone_call_time[call_logs[1]] += int(call_logs[-1])

longest_phone_number = ""
longest_time = 0

for phone_number in telephone_call_time:
    if telephone_call_time.get(phone_number) > longest_time:
        longest_phone_number = phone_number
        longest_time = telephone_call_time.get(phone_number)

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(longest_phone_number, longest_time))

