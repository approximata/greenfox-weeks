ah = ['kuty', 'macsk', 'cic']
# add to all elements an 'a' on the end
for n in range(len(ah)):
    ah[n] += "a"
print(ah)

n=0
while len(ah) > n:
    ah[n] += "a"
    n += 1
print(ah)
