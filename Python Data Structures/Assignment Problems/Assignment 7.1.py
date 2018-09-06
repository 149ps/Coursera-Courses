# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
read_text=fh.read()
read_strip=read_text.rstrip()
upper_text=read_strip.upper()
print(upper_text)
