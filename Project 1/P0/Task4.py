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

"""
First get the telemarketing numbers from the phone number list and this time only the out call number 
I am guessing that it is not the usual numbers that starts with 140? 
If that is the case then make a set of outcall incoming call out going text incoming text
combine all of the incoming numbers, text_sending numbers, text_receiving_numbers
"""

def get_outcall_numbers(call_log):

def get_incoming_numbers(call_log):

def get_sending_text_numbers(text_log):
    
def get_receive_text_numbers(text_log):


print('These numbers could be telemarketers: ')
# list of numbers

call_set = set([])

for call_log in calls:
    call_set.add(call_log[0])
    call_set.add(call_log[1])