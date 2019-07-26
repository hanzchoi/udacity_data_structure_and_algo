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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""



def get_outcall_numbers(call_logs):
    outcall_set = set([])

    for call_log in call_logs:
        outcall_set.add(call_log[0])

    return outcall_set


def all_phone_numbers_except_outcalls(call_logs, text_logs):
    phone_number_set = set([])

    for call_log in call_logs:
        phone_number_set.add(call_log[1])

    for text_log in text_logs:
        phone_number_set.add(text_log[0])
        phone_number_set.add(text_log[1])

    return phone_number_set


possible_telemarketer_numbers = []
outcall = get_outcall_numbers(calls)
except_outcall = all_phone_numbers_except_outcalls(calls, texts)

for number in outcall:
    if number not in except_outcall:
        possible_telemarketer_numbers.append(number)

print('These numbers could be telemarketers: ')

for number in possible_telemarketer_numbers:
    print(number)
