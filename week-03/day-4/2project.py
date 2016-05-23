names = ('dog goat dad duck doodle never')
def revers_word(word):
    return(word[::-1])
def search_pali(lotofwords):
    palis = []
    for i in range(len(lotofwords)):
        for n in range(i+2,len(lotofwords)):
            if lotofwords[n] == lotofwords[i] and lotofwords[i:n+1] == revers_word(lotofwords[i:n+1]):
                palis.append(lotofwords[i:n+1])
    return palis
print(search_pali(names))
