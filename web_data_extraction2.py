import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
fopen = urllib.request.urlopen("http://data.pr4e.org/intro-short.txt")
soup = BeautifulSoup(fopen, 'fopen.parser')
count = dict()
for line in fopen:
    print(line)
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word, 0) + 1

print(count)