# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.
def countreadlines(file_name):
    fr = open(file_name)
    text = fr.readlines()
    fr.close()
    return len(text)

print(countreadlines('sample.txt'))
