# create a function that takes a list and returns a new list with all the elements doubled
numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list
def doubledKB(n):
    new_renum=[]
    for i in range(0, len(n)):
        n[i] *= 2
        new_renum.append(n[i])
    return new_renum

print(doubledKB(numbers))
