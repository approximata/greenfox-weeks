import sys
import csv

arg = sys.argv
def create_file_if_missing(file_name):
    try:
        g = open(file_name,'a')
    except FileNotFoundError:
        f = open(todostore.csv,'a')
        f.close()

def readfunctions(file_name):
    fr = open(file_name)
    text = fr.read()
    fr.close()
    return text

def check(truefalse):
    if truefalse == 'True':
        return '[x] '
    else:
        return '[ ] '

def readtodo(file_name):
    linenumber = 1
    text = ''
    with open(file_name, 'r') as f:
        reader = csv.reader(f, delimiter = ';')
        for column in reader:
            text = text + str(linenumber) + ' - ' + check(column[0]) + ' ' + column[1] + '\n'
            linenumber += 1
        if len(text) <= 0:
            return('No todos for today!')
        return text
        f.close()

def additem(file_name):
    fa = open(file_name, 'a')
    fa.write('False;' + arg[2] + '\n')
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

def complete_task(file_name, task_number):
        texttox = []
        fr = open(file_name, 'r')
        reader = csv.reader(fr, delimiter = ';')
        for line in reader:
            texttox.append(line)
        if texttox[task_number-1][0] == 'True':
            print('It is already checked')
        else:
            texttox[task_number-1][0] = 'True'
        fr.close()
        fw = open(file_name, 'w')
        for i in texttox:
            fw.write(i[0] + ';' + i[1] + '\n')
        fw.close()

def main():
    create_file_if_missing('todostore.txt')
    try:
        if len(arg) == 1:
            print(readfunctions('todohelp.txt'))
        elif arg[1] == '-l':
            print(readtodo('todostore.csv'))
        elif arg[1] == '-a' and len(arg) == 3:
            additem('todostore.csv')
        elif arg[1] == '-r' and len(arg) == 3:
            removeitem('todostore.csv', int(arg[2]))
        elif arg[1] == '-c' and len(arg) == 3:
            complete_task('todostore.csv', int(arg[2]))
        elif arg[1] == '-a':
            print ("Unable to add: No task is provided")
        elif arg[1] =='-r':
            print ("Unable to remove: No index is provided")
        elif arg[1] =='-c':
            print ("Unable to complete: No index is provide")
        else:
            print ("Unsupported argument\n")
    except ValueError:
        print('Unable to remove: Index is not a number')

main()
