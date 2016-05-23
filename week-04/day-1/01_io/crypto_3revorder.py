# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    f = open(file_name)
    text = f.readlines()
    f.close()
    newtext = text[::-1]
    newtext = ''.join(newtext)
    return newtext

print(decrypt('texts/reversed_zen_order.txt'))
