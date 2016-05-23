# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.readlines()
    f.close()
    newtext = ''
    for line in text:
        for letter in range(len(line)-2,-1,-1):
            newtext += line[letter]
        newtext += '\n'
    return newtext

print(decrypt('texts/reversed_zen_lines.txt'))
