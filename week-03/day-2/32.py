num = 123
# create a function that doubles it's input
# double af with it

# def doubleIT(af):
#     af +=af
#     print(af)
#
# doubleIT(num)

# hasznos linkek: cmd shift l cmd shift d


def doubleIT(af):
    return af * 2
print(doubleIT(num))

def test(actual, expected):
    if expected == actual:
        print('check')
    else:
        print('jaj')

test(num * 2, doubleIT(num))
