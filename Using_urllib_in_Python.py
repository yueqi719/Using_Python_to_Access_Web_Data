import urllib.request, urllib.parse, urllib.error
#almost the same as open(), open an online url
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') 
for line in fhand:
    print(line.decode().strip())

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(counts)