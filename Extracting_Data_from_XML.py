import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1: 
    url = 'http://py4e-data.dr-chuck.net/comments_1426897.xml'

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

sum = 0
counts = tree.findall('.//count')
print('count:', len(counts))
for item in counts:
    sum = sum + int(item.text)
print('sum', sum)
#done