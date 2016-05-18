numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list
def reversMate(n):
    new_renum=[]
    for i in range(len(n)-1, -1, -1):
        new_renum.append(n[i])
    return new_renum
print(reversMate(numbers))
