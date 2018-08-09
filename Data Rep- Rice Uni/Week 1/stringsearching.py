"""def count_vowels(word):
    count_a=word.count("a")
    count_e=word.count("e")
    count_i=word.count("i")
    count_o=word.count("o")
    count_u=word.count("u")
    count=count_a+count_e+count_i+count_o+count_u
    return count

print(count_vowels("aaassseefffgggiiijjjoOOkkkuuuu"))
print(count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle"))

"""
def demystify(string_l1):
    replace_l= string_l1.replace("l","a")
    replace_m= replace_l.replace("1","b")
    return replace_m

print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))
