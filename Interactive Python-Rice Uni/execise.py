"""hrs = input("Enter Hours:")

rate= input("Enter Rate per hour:")
pay=float(hrs)*float(rate)
print("Pay:" + str(pay))

x=float(input())
if x < 2 :
    print('Below 2')
elif x >= 2 :
     print('Two or more')
else :
    print('Something else')
"""
"""
astr = 'Hello Bob'
istr = int(astr)
print('First', istr)
astr = '123'
istr = int(astr)
print('Second', istr)
"""

"""
astr = 'Hello Bob'
istr = 0
istr = int(astr)
print(istr)
"""
score = input("Enter Score: ")
score_f=float(score)
if score_f>1 and score_f<0:
    print("Score Out of range")
if score_f>=0.9:
    print("A")
elif score_f>=0.8:
    print("B")
elif score_f>=0.7:
    print("C")
elif score_f>=0.6:
    print("D")
elif score_f<0.6:
    print("F")