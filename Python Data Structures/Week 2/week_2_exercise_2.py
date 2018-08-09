fh = open('short.txt')
print(fh)

count=0
sum=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count+=1
        float_value=line.find("0.")
        number=float(line[float_value:])
        sum=sum+number
avg=float(sum/counter)

print("avg spam is: ",avg)
