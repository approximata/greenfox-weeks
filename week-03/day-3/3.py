# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class Pirate:

    def __init__(self):
        self.rum = 0
    def drink_rum(self):
        self.rum += 1
        return 'Cheers'
    def hows_goin_mate(self):
        if self.rum <= 5:
            return "Nothin'"
        else:
            return "Arrrr!"

Captian = Pirate()
print(Captian.drink_rum())
print(Captian.hows_goin_mate())
print(Captian.drink_rum())
print(Captian.hows_goin_mate())
print(Captian.drink_rum())
print(Captian.hows_goin_mate())
print(Captian.drink_rum())
print(Captian.hows_goin_mate())
print(Captian.drink_rum())
print(Captian.hows_goin_mate())
print(Captian.drink_rum())
print(Captian.hows_goin_mate())
