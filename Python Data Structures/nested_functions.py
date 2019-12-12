"""def outer(num1):
    def inner_increment(num1):  # Hidden from outer code
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1, num2)

outer(10)"""

text="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
words=text.split()
print(words)
hour=words[5]
h=hour.split(':')
print(h)
        