import re

hand  = open('regex_sum.txt')
sum = 0

for line in hand:
    line = line.rstrip()
    nums = re.findall('[0-9]+',line)
    #print(nums)
    if len(nums) == 0: continue
    for num in nums:
        sum = sum + int(num)

print(sum)