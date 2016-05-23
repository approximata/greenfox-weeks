# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    #version 1
    # f = open(file_name)
    # text = f.readlines()
    # f.close()
    # newtext = ''
    # for line in text:
    #     for letter_i in range(0, len(line)):
    #         if line[letter_i] == ' ' or line[letter_i] == '\n':
    #             newtext += line[letter_i]
    #         else:
    #             newtext += chr(ord(line[letter_i])-1)
    # return newtext

    #version 2
    f = open(file_name)
    text = f.read()
    f.close()
    newtext = ''
    for letter in text:
        if letter == " " or letter == '\n':
            newtext += letter
        else:
            newtext += chr(ord(letter)-1)
    return newtext


print(decrypt('texts/encoded_zen_lines.txt'))
