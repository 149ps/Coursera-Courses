name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dict1=dict()
for line in handle:
    if line.startswith("From"):
        words=line.split()
        if len(words) > 5:
        	hour=str(words[5])
        	h=hour.split(':')
        	key=h[0]
        	dict1[key]=dict1.get(key,0)+1
for key,value in sorted(dict1.items()):
    print(key,value)
