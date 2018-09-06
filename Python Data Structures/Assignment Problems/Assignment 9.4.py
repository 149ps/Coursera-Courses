name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dict1=dict()
for line in handle:
    if line.startswith('From:'):
        words=line.split()
        key=words[1]
        dict1[key]=dict1.get(key,0)+1

a=max(dict1.values())
for key,value in dict1.items():
    if value==a:
        print(key,value)