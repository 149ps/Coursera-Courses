import re
fname=open("D:\\SCU\\Coursera\\Using Python to Acess Web Data\\Week 2\\regex_sum_82567.txt")
nums=[]
for line in fname:
    list1=re.findall('[0-9]+',line)
    nums=nums+list1
print(nums)

sum=0
for num in nums:
    sum=sum+int(num)
print(sum)

