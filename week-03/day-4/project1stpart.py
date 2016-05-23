names = ['laci', 'gabi', 'pisti', 'misi']

def revers_words(words):
    new_renum=[]
    for i in range(len(words)-1, -1, -1):
        new_renum.append(words[i])
    return new_renum


print(revers_words(names))


name = "lacika"

def revers_word(word):
    new_word = ''
    for i in range(len(word)-1, -1, -1):
        new_word += word[i]
    return word + new_word 

print(revers_word(name))
