def list_sort(lista):

    even = []
    odd = []
    characters = []
    mydict = dict()
    if not isinstance(lista, list):
        return 'Invalid Input'

    if not lista:
        mydict['evens'] = even
        mydict['odds'] = odd
        mydict['chars'] = characters
        return mydict

    for i in lista:

        if isinstance(i, int):
            if i % 2 == 0:
                even.append(i)

            else:
                odd.append(i)

        elif isinstance(i, str):
            characters.append(i)

    mydict['evens'] = sorted(even)
    mydict['odds'] = sorted(odd)
    mydict['chars'] = sorted(characters)
    
    return mydict


print(list_sort([2,0,6,5,1,7, 'z', 'a']))
