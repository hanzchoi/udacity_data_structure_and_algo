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

with open('calls_01.csv', 'r') as f:
    reader = csv.reader(f)
    calls01 = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

area_code_and_mobile_prefixes = set([])

# 97448 02140,(022)34715405,07-09-2016 15:02:50,679


def fixed_phone_lines_check(phone_number):
    if phone_number[0] == "(" and phone_number[1] == "0":
        return True
    else:
        return False


def mobile_phone_number_check(phone_number):
    if phone_number[0] == "7" or phone_number[0] == "8" or phone_number[0] == "9":
        return True
    else:
        return False


def add_area_code_or_mobile_prefixes_to_set(phone_number):
    if fixed_phone_lines_check(phone_number):
        close_index = phone_number.find(")")
        area_code_and_mobile_prefixes.add(phone_number[1:close_index])
    elif mobile_phone_number_check(phone_number):
        area_code_and_mobile_prefixes.add(phone_number[0:5])


for call_logs in calls01:
    add_area_code_or_mobile_prefixes_to_set(call_logs[0])
    add_area_code_or_mobile_prefixes_to_set(call_logs[1])


print('The numbers called by people in Bangalore have codes: ')

for number in sorted(area_code_and_mobile_prefixes):
    print(number)