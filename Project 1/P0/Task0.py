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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# print("First record of texts, <incoming number> texts <answering number> at time <time>")
# print("Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds")


text_incoming_number = texts[0][0]
text_answering_number = texts[0][1]
text_time = texts[0][2]

calls_incoming_number = calls[-1][0]
calls_answering_number = calls[-1][1]
calls_time = calls[-1][2]
calls_during = calls[-1][3]

print(texts[0])
print(calls[-1])
print('First record of texts, {} texts {} at time {}'.format(text_incoming_number, text_answering_number, text_time))
print('Last record of calls, {} calls {} at time {}, lasting {} seconds'.format(calls_incoming_number, calls_answering_number, calls_time, calls_during))

