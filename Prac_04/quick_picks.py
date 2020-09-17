from random import randint
DIGITS_1 = randint(1, 45)
DIGITS_2 = randint(1, 45)
DIGITS_3 = randint(1, 45)
DIGITS_4 = randint(1, 45)
DIGITS_5 = randint(1, 45)
DIGITS_6 = randint(1, 45)


numbers = [DIGITS_1, DIGITS_2, DIGITS_3, DIGITS_4, DIGITS_5, DIGITS_6]
print(numbers)
quick_pick = int(input("How many quick picks? "))
for i in range(1,quick_pick+1):
    numbers.sort()
    print(numbers)



