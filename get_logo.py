from __future__ import print_function
import re

with open('test', 'r+') as file:
    reversed_text = str(file.read())[::-1]
    print(re.search(r'("oci\..*?")', reversed_text).group(0)[::-1])
