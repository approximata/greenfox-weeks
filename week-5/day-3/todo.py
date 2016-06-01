import sys

arg = sys.argv

def readfunctions(file_name):
    fr = open(file_name)
    text = fr.read()
    fr.close()
    return text

def readtodo(file_name):
    frl = open(file_name)
    textfrl = frl.readlines()
    frl.close()
    if len(textfrl) == 0:
        print('No todo mari')
    else:
        newtextfrl = []
        for i in range(len(textfrl)):
            newtextfrl = str(i+1) + ' - ' + textfrl[i]
            print(newtextfrl.rstrip())

def additem(file_name):
    fw = open(file_name, 'a')
    if len(arg) == 3:
        fw.write(str(arg[2]) + '\n')
        fw.close()
    else:
        raise ValueError('Unable to add: No task is provided')

if len(arg) == 1:
    print(readfunctions('todohelp.txt'))

elif arg[1] == '-l':
    readtodo('todostore.txt')

elif arg[1] == '-a':
    additem('todostore.txt')
