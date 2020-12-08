# Extra Credit  6 sided die.
# Extra Credit a.
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        from random import randint
        print(randint(1, self.sides))


current_number = 0
while current_number != 10:
    side6 = Die()
    side6.roll_die()
    current_number += 1
    continue


# b. probability of getting a 4 on a die
def die_probability():
    sides = 6
    four = 1
    four_probability = four / sides
    four_probability_percent = four_probability * 100
    print('\n')
    print("The probability of getting four dots on a six sided die is: ")
    print(str(round(four_probability_percent, 0)) + '%')

my_die = die_probability()