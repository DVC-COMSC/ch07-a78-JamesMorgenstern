
words = input('Enter the list: ').split()

are = ['a', 'r', 'e']
idxlst = []
final = []

for i in range(len(words)):
    idxlst = [words[i].find(are[j]) for j in range (len(are))]
    check = True
    for x in range(len(idxlst)):
        if (idxlst[x] == -1):
            check = False
    if (check == True):
        print (words[i], end = " ")
        #final.append(words[i])

#print (final)

