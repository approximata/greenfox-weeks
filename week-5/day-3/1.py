# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0
while True:
    try:
        number = int(input('what number\n'))
        print(10/number)
        break
    except ValueError:
        print('integer number please')
    except ZeroDivisionError:
        print('dont give me zero! Fail')
