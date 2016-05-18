names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list
def myminstr(fname):
    minnum=fname[0]
    for i in range(len(fname)):
        if minnum < len(fname[i]):
            pass
        else:
            minnum = len(fname[i])
    return fname[minnum]

print(myminstr(names))
