#import os
"""
def echo_file(file_name):
    #Open a file, read its contents, and echo to console
    my_file = open(file_name, 'r')
    my_file_text = my_file.read()
    print(my_file_text)
    my_file.close()
"""
"""
print(os.path.abspath("Random.txt"))
"""
"""
def smallest(lst):
    smallest_num=1000
    for i,num in enumerate(lst1):
        if num < smallest_num:
            smallest_num=num
    return smallest_num
lst1=input()
print(smallest(lst1))
"""


  
smallest=None
largest=None
while True:
    num=input()
    if num=="done" : break
    try:
        num=float(num)
    except:
        print("Invalid input")
        continue
    
        
    if largest is None:
        largest=float(num)
        print("Maximum ",largest)
    elif num > largest:
        largest=float(num)
        print("Maximum ",largest)
    else:
        print("Maximum ",largest)

    if smallest is None:
        smallest=float(num)
        print("Minimum ",smallest)
    elif num < smallest:
        smallest=float(num)
        print("Minimum ",smallest)
    else:
        print("Minimum ",smallest)

print("Maximum",int(largest))
print("Minimum",int(smallest))
    
"""
for num in lst1:
    if smallest is None:
        smallest=num
    elif num < smallest:
        smallest=num
print(smallest)
7
for num in lst2:
    if largest is None:
        largest=num
    elif num>largest:
        largest=num
print(largest)

"""