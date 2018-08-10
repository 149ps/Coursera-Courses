def commonCharacterCount(s1, s2):
    count=0
    list1=list(s2)
    for i in range(len(s1)):
        print(s1[i] in list1)
        if(s1[i] in list1):
            count+=1
            list1.remove(s1[i])
    return count


s1='aabcc'
s2='adcaa'
print(commonCharacterCount(s1, s2))