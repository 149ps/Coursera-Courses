fname = input("Enter file name: ")
fh = open(fname)
lst = list()
lst1=list()
for line in fh:
    line.rstrip()
    lst=line.split()
    for word in lst:
        if not word in lst1:
            lst1.append(word)
    lst1.sort()
print(lst1)
