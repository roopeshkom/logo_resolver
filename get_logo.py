from __future__ import print_function
from sys import argv
from bs4 import BeautifulSoup
import urllib

file = urllib.urlopen(argv[1])
html = file.read()
soup = BeautifulSoup(html, 'html.parser')

link = None
for meta in soup.find_all('meta'):
    attributes = meta.attrs
    if 'property' in attributes and attributes['property'] == 'og:image':
        link = meta['content']
        break

print(link if link else 'Could not resolve logo...')
