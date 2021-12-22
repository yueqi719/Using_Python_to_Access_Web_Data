import re

x = 'My 2 favorite number are 19 and 42'
y = re.findall('[0-9]+',x)
print(y) #this gives a list of strings containing string 2, 19, and 42

a = 'From: Using the : character'
b = re.findall('^F.+:', a)
print(b) #返回了From : Using the : 而不是 From : 是因为match the greatest possible string 

#Non-greedy
c = re.findall('^F.+?:', a) #add ?
print(c) #['From:']

#Fine-Tuning String extraction
ln = 'From yueqi@ucsd.edu Sat Jun 5 2008'
email = re.findall('\S+@\S+', ln)
print(email) #['yueqi@ucsd.edu']
email2 = re.findall('^From.(\S+@\S+)', ln)
print(email2) #['yueqi@ucsd.edu']
part = re.findall('@([^ ]*)',ln)
print(part) #['ucsd.edu']
part2 = re.findall('^From .*@([^ ]*)',ln)
print(part2) #['ucsd.edu']
print(re.findall('\S+?@\S+',ln)) #quiz question

#Spam Confidence
hand  = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    #find line starts with 'X-DSPAM-Confidence: '
    #extract from one or more idgit with dot one or more times
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print("Maximum:", max(numlist)) #Maximum: 0.9907