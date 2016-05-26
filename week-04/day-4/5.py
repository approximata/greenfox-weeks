# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).
def get_bunnyears(bunny, ears):
    if ears <= 0:
        return 0
    else:
        return bunny + get_bunnyears(bunny, ears-1)
print(get_bunnyears(5, 3))
