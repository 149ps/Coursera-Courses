# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count+=1
        float_value=line.find("0.")
        number=float(line[float_value:])
        total+=number
avg=float(total/count)

print("Average spam confidence:",avg)
