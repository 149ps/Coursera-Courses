def allLongestStrings(inputArray):
    list1=[]
    list2=[]
    for i in inputArray:
        length=len(i)
        list1.append(length)
    max_length=max(list1)
    for i in inputArray:
        if(len(i)==max_length):
            list2.append(i)       
    return list2


inputArray = input(list())
print(allLongestStrings(inputArray))