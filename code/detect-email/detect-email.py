 # detect email
# 15.10.2020 Modified:
# How to run: python detect-email.py input > result
import sys
import re

emails_list = []
with open (sys.argv[1],'r') as file:

    for input_data in file:
        emails = re.findall(r'[\w\.]+@[\w]+(?:\.[\w]+)+', input_data.strip())
        emails_list.extend(emails)

emails_list = set(emails_list)
if (len(emails_list) > 0):
    print(";".join(sorted(emails_list)))
