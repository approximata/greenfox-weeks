ab = 100
credits = 49
is_bonus = False
# if credits are at least 50,
# and is_bonus is False decrement ab by 2
# if credits are smaller than 50,
# and is_bonus is False decrement ab by 1
# if is_bonus is True ab should remain the same
if (credits >= 50 and is_bonus == False):
    ab -= 2
    print(ab)
elif (credits < 50 and is_bonus == False):
    ab += 1
    print(ab)
elif (is_bonus == True):
    print(ab)
