
def compress(data):
    comp_data = []
    dictionnary = ['']
    word = ''
    i = 0
    for char in data:
        i += 1
        word += char
        if not word in dictionnary:
            dictionnary.append(word)
            comp_data.append([dictionnary.index(word[:-1]), word[-1]])
            word = ''
        elif i == len(data):
            comp_data.append([dictionnary.index(word), ''])
            word = ''
    #print(dictionnary)
    dictionnary=dictionnary[1:]
    return dictionnary

def roomPresentNumber(comp_data):
    dictionarylist=[]
    for element in comp_data:
        counter = 0
        secondaryList=[]
        for elemnt2 in comp_data:
            if element in elemnt2:
                counter+=1
        secondaryList.append(element)
        secondaryList.append(counter)
        dictionarylist.append(secondaryList)
    print(dictionarylist)


