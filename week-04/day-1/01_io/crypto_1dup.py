# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    f = open(file_name)
    text = f.readlines()
    f.close()
    newtext = ''
    for line in text:
        for j in range(0, len(line)-1, 2):
             newtext += line[j]
        newtext += '\n'
    return newtext


print(decrypt('texts/duplicated_chars.txt'))
