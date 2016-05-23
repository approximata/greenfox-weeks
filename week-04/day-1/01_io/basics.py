# 1. Create a method that reads all contents of a file when its name given as param
def readfile(file_name):
    fr = open(file_name)
    text = fr.read()
    fr.close()
    return text

# 2. Create a method that gets a file_name and a number as param and reads the numberth line of the file
def readline(file_name, number):
    frl = open(file_name)
    for i in range(number):
        textfrl = frl.readline()
    frl.close()
    return textfrl.rstrip()

print(readline('texts/duplicated_chars.txt', 5))

# 3. Create a method that gets a long sentence as param and gives back the contained words in a list
def words(sentence):
    wordsofstring = sentence.rstrip('.')
    wordsofstring = wordsofstring.split()
    return wordsofstring

print(words('what is happenning in here.'))

# 4. Create a method that gets a list of words and creates a sentence with the words separated by spaces
def sentence(words):
    newsentence = ""
    for word in words:
        word = word.rstrip('.')
        newsentence += word + " "
    newsentence = newsentence[:-1]
    return newsentence + '.'

aha = ['alma', 'macska', 'kutya.']
print(sentence(aha))

# 5. Create a method that gets a string and gives back the character codes in a list
def char_codes(string):
    neword = []
    letters = string.split()
    for letters in string:
        neword += [ord(letters)]
    return neword

print(char_codes("jdvjkb"))

# 6. Create a method that gets a list of integers and gives back a string which characters are created from the numbers used as character codes
def string(char_codes):
    newstring = ''
    for char in char_codes:
        newstring += chr(char)
    return newstring

list = [12, 34, 56, 102, 121]
print(string(list))
