while True:
    try:
        number = int(input('what number\n'))
        print(18/number)
        break
    except ValueError:
        print('number please')
    except ZeroDivisionError:
        print('dont zero')
    finally:
        print('loop master')
