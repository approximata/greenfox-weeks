# Adds a and b, returns as result
def add(a, b):
    if type(a) == str or type(b) == str:
        return False
    else:
        sum = round(a, 3)  + round(b, 3)
    return round(sum, 3)

# Returns the highest value from the three given params
def max_of_three(a, b, c):
    if type(a) == str or type(b) == str or type(c) == str:
        return False
    else:
        if a == b or b == c or c == a:
            return False
        else:
            if a > b and a > c:
                return a
            elif b > c and b > a:
                return b
            else:
                return c

def median(pool):

    if type(pool) != list:
        return False
    else:
        newpool = []
        for number in range(len(pool)):
            if type(pool[number]) != str:
                newpool += [pool[number]]
            print(newpool)

    if len(newpool) % 2 == 0:
        return (newpool[int((len(newpool))/2)-1] + newpool[int((len(newpool))/2)]) / 2.0
    else:
        return newpool[int((len(newpool) - 1) / 2.0)]

list1 = [5, 6, 7, 'six', 8]

print(median(list1))

def is_vovel(char):
    return char in 'aeiou'

# Create a method that translates hungarian into the teve language
def translate(hungarian):
    teve = hungarian
    for char in teve:
        if is_vovel(char):
            teve = (char+'v'+char).join(teve.split(char))
    return teve
