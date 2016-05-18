ah = [3, 4, 5, 6, 7]
summa = 0
# print the sum of all numbers in ah
#s1
for n in range(len(ah)):
    summa += ah[n]
print(summa)
#s2
sumwh = 0
n = 0
while len(ah) > n:
    sumwh += ah[n]
    n += 1
print(sumwh)
#s3
print(sum(ah))
