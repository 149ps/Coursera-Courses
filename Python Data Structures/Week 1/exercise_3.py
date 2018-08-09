"""def count(word,ltr):
    count=0
    for letter in word:
        if letter==ltr:
            count+=1
    return count

print(count('banana','a'))
"""


"""if word < 'cricket':
    print('Your word, ' + word + ' ,comes after apple.')
elif word > 'cricket':
    print('Your word, ' + word + ' ,comes before apple.')
else:
    print('All right apple.')
if word < 'apple':
    print('Your word,' + word + ', comes before apple.')
elif word > 'apple':
    print('Your word,' + word + ', comes after apple.')
else:
    print('All right, apple.')
"""
"""
word='Good Morning'
print(word.startswith('Good'))
 find() method gives the starting method"""

text = "X-DSPAM-Confidence:    0.8475";
number=text.find("0.")
print(float(text[number:]))



