from __future__ import print_function
import re
from sys import argv
import urllib

file = urllib.urlopen(argv[1])
reversed_text = file.read()[::-1]

search_result = re.search(r'("oci\..*?")', reversed_text)
ico_url = search_result.group(0)[::-1] if search_result else 'Could not resolve a logo...'

print(ico_url)
