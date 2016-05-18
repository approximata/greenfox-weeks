numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens
def oddNum(nom):
    new_nom=[]
    for i in nom:
        if i % 2 <> 0:
            new_nom.append(i)
    return new_nom
print(oddNum(numbers))
