import operator

def count_letters(monty_words):
    
    letter_count={}
    for letter in monty_words:
        if letter in letter_count:
            letter_count[letter]+=1
        else:
            letter_count[letter]=0

monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"

monty_words = monty_quote.split()
print(monty_words)
print(count_letters(monty_words))
    