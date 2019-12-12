"""

def max_difference(nums):
    cur_max=0
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]<nums[j]:
                if (nums[j]-nums[i])>cur_max:
                    cur_max=nums[j]-nums[i]
                    a=nums[i]
                    b=nums[j]
    return cur_max,a,b

nums=[4,3,10,2,9,1,6]
print(max_difference(nums))


def periodicSequence(s0, a, b, m):
    s=[]
    s.append(s0)
    print(s)
    i=1
    while True: 
        val=(a*s[i-1] + b) % m
        if val in s[1:]:
            return val
        else:
            s.append(val)
            i+=1
s0=1
a=2
b=3
m=5
print(periodicSequence(1,2,3,5))
"""
"""
import numpy as np
a=np.array([10,2,31,4,15,6])
x=a.argsort()
y=np.array([])
"""
list1=[1,2,3]
dict1={}
dict1[1]=list1
print(dict1)

x=[[1,2],
   [3,4]]]

        

            
                
                
        
