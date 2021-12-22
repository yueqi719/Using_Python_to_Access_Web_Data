import re

hand  = open('regex_sum.txt')
total = 0

for line in hand:
    line = line.rstrip()
    nums = re.findall('[0-9]+',line)
    print(nums)
    if len(nums) == 0: continue
    for num in nums:
       total = total + int(num)

print(total)

#shorter code 
import re
print(sum([int(i) for i in re.findall('[0-9]+',open("regex_sum.txt").read())]))