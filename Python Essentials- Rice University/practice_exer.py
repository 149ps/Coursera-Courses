"""
Template - Take a list of integers and concatenate their digits
"""
"""
def concatenate_ints(int_list):
    new_int=int_list[0]
    j=len(int_list)
    for i in range(1,j):
         new_int =  str(new_int) + str(int_list[i])
    return new_int
    
# Tests
print(concatenate_ints([4]))
print(concatenate_ints([4, 0, 4]))
print(concatenate_ints([123, 456, 789]))
print(concatenate_ints([32, 796, 1000]))


# Output
#4
#404
#123456789
#327961000
"""
#Simple task list.
"""
lst=[1,5,7,3]
tup=(1,5,7,3)

print(lst[2:3])
print(tup[2:3])
tup[1]=9
print(tup)
"""

"""

def first_repeated_character(s):
    
    hash1=list(s)
    for index,char1 in enumerate(s):
        c=len(s)
        if char1 in hash1[index+1:c]:
            return char1
    return ' It\'s a non-repeating String'
print(first_repeated_character("geeksforgeeks"))

"""
"""
s='abcba'
hash1=[]
hash2=list(s)
for index,char1 in enumerate(s):
    c=len(s)
    hash1.append(char1)
    if char1 in hash2[index+1:c]:
        print(char1)
    



"""
"""
def mutate_list(alist):
    alist.append(42)
    

lst1=[1,2,3]
print(lst1)
mutate_list(lst1)
print(lst1)

"""
"""
lst1=[1,2,3]
lst1.append(5)
lst1.remove(1)
print(lst1)
"""
"""
def count_vowels(word):
    list=['a','e','i','o','u']
    count=0
    for char in word:
        if char in list:
           count=count+1
    return count
print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))
"""
"""
def demystify(l1_string):
    str=''
    for char in l1_string:
        if char=='l':
            str=str+'a'
        elif char=='1':
            str=str+'b'
        else:
            str=str+char
            
    return str
print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))
"""
"""
a='aaabbbabababbbbaa'
b='aaabbbabababbbbaa'
x=(a>b)-(a<b)
print(x)
"""
"""
lst=[1,3,5,7,9]
lst.reverse()
print(lst)
lst.reverse()
print(lst)
"""
"""
def dif_last(fib):
    for index,item in enumerate(fib):
        number=fib[index]+fib[index+1]
        fib.append(number)
        if index==21:
            return fib[index]

fibbo=[0,1]
print(dif_last([0,1]))
"""
new_t=tuple(1,)
print(new_t)
    