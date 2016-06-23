from random import randint

def get_enemystartpoint():
    x = randint(0,9)
    y = randint(0,9)
    coordinate = []
    coordinate.append(x)
    coordinate.append(y)
    return coordinate
    # if is_step_valid(x, y):
    #     return x, y
    # else:
    #     get_enemystartpoint()
    #

print(get_enemystartpoint()[0], get_enemystartpoint()[1])
