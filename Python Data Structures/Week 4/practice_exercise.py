lst1=['a','b','c']
"""
pop(gives the index if no index is given then deletes the last element)

Syntex: lst1.pop(index)

del (deletes the element of index specified)

Syntex:
del [list name(index name)]

remove deletes the element specified by name.

list.remove('element name') 



total=0
count=0
while(True):
    inp=input("Enter a number:")
    if inp=='done':
        break
    value=float(inp)
    total+=value
    count+=1

avg= total/count
print("Average is:",avg)

"""
"""
lst1=list()
while(True):
    inp=input('Enter a number:')
    if inp=='done':
        break
    value=float(inp)
    lst1.append(value)
    
avg=sum(lst1)/len(lst1)
print('Average is:',avg)
"""

'To convert a string into a list.'
"""
str1="Hello World, How are you"
t=str1.split(',')
print(t)
"""
"""
lst1=['p','r','a','t']
s=''
i=s.join(lst1)
print(i)
"""
"""
def checkPalindrome(inputString):
    lst1=list(inputString)
    l=0
    h=len(lst1)-1
    print(lst1)
    while(h>l):
        if(lst1[l]!=lst1[h]):
            print(lst1[l],lst1[h])
            return False
        else:
            l+=1
            h-=1
            print(lst1[l],lst1[h])
            print(l,h)
    return True

str1='aaabaaaa'
print(checkPalindrome(str1))
"""
"""
str1='world '
lst1=list(str1)
print(str1)
i=0
j=4
for char in lst1:
    lst1[i]=lst1[j]
    i+=1
    j-=1
    print(''.join(lst1))
    
    """
"""

def adjacentElementsProduct(inputArray):
    start = inputArray[0]
    product=start * inputArray[1]
    for i,element in enumerate(inputArray[1:-1]):
        start=element
        print(element,i)
        temp_product= element * inputArray[i+2]
        print(temp_product)
        if( temp_product > product):
            product=temp_product
    return product


array=[3,6,-2,17,7,3]
print(adjacentElementsProduct(array))

"""
"""

def almostIncreasingSequence(sequence):
    selist=list(sequence)
    count=0
    for i,element in enumerate(selist):
        print(element,selist[i-1])
        if (element<selist[i-1]):
            count+=1
            if(count>1):
                return False
        else:
            return True
        
a=[1,3,2,1]
print(almostIncreasingSequence(a))

"""

def matrixElementsSum(matrix):
    cost=0
    for i,row in enumerate(matrix):
        print(i,row)
        for j,element in enumerate(row):
            print(j,element)
            if (element==0):
                for z in range(len(matrix)):
                    print(matrix[z][j])
                    matrix[z][j]=0
            elif(element!=0): 
                cost+=element
    return cost


a=[[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
"""print(a[:len(a)][:])"""
print(matrixElementsSum(a))
