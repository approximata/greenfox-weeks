numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function
# def summacska(numer):
#     summa = numer[0]
#     for n in range(1, len(numer)):
#         summa += numer[n]
#     print(summa)
#
# summacska(numbers)

def summacska(numer):
    summa = 0
    for num in numer:
        summa += num
    return(summa)

print(summacska(numbers))
