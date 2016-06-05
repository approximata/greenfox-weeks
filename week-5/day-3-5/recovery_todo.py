import sys

arg = sys.argv
def create_file_if_missing(file_name):
    try:
        g = open(file_name,'a')
    except FileNotFoundError:
        f = open(todostore.txt,'a')
        f.close()

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
    fa = open(file_name, 'a')
    fa.write(str(arg[2]) + '\n')
    fa.close()

def removeitem(file_name, task_number):
    frl = open(file_name)
    textfrl = frl.readlines()
    if int(arg[2]) > len(textfrl):
        print('Unable to remove: Index is out of bound')
    else:
        textfrl.remove(textfrl[task_number-1])
        frl.close()
        fw = open(file_name, 'w')
        for line in textfrl:
                fw.write(line)
        fw.close()

def main():
    create_file_if_missing('todostore.txt')
    try:
        if len(arg) == 1:
            print(readfunctions('todohelp.txt'))
        elif arg[1] == '-l':
            readtodo('todostore.txt')
        elif arg[1] == '-a' and len(arg) == 3:
            additem('todostore.txt')
        elif arg[1] == '-r' and len(arg) == 3:
            removeitem('todostore.txt', int(arg[2]))
        elif arg[-1] == '-a':
            print ("Unable to add: No task is provided")
        elif arg[-1] =='-r':
            print ("Unable to remove: No index is provided")
        else:
            print ("Unsupported argument\n")
    except ValueError:
        print('Unable to remove: Index is not a number')

main()
