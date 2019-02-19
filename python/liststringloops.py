def vowelcount(txt):
    if not isinstance(txt,str):
        raise TypeError('invalid input')

    vowels = 'aeiou'
    newtxt =txt.lower()
    duplicates_none =set(newtxt)
    duplication = len(newtxt)-len(duplicates_none)
    vowelstring = ""

    for a in vowels:
        if a in duplicates_none:
            vowelstring += str(a)
    return (vowelstring,duplication)
if __name__ == "__main__":

    print(vowelcount('alwalys'))            