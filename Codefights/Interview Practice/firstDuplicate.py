def firstDuplicate(a):
    arr=[]
    for i in a:
        print(i)
        if i in arr:
            return i
        arr.append(i)
    return -1

a = [2, 3, 3]
print(firstDuplicate(a))


