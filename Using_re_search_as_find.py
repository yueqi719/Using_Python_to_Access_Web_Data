import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:',line):
        print(line)

#for line in hand:
 #   line = line.rstrip()
  #  if line.find('From:') >= 0:
   #     print(line)