# Homework #1
# 1. The Verse
print('Я не программер, я тренер животных')
print('Со стаей собачьей умею справляться')
print('Не испугаюсь рептилий голодных')
print('С Питоном теперь я хочу состязаться')

print('\n')

#2 Calculation of Velocity
distance_between_inhabited_locality = 48
time_of_travel_by_hiker = 12;
velocity_of_hiker_who_travels_between_inhabited_locality = distance_between_inhabited_locality / time_of_travel_by_hiker
print(velocity_of_hiker_who_travels_between_inhabited_locality)

print('\n')

#3 Humble Greeting
name = 'Alex'
print(f"How do you do {name}?") # 
n = 100;
print(f"I'm C{n//10%10}{n%100}{name[1]}! Thanks")

print('\n')

#4 Calculator
a = 8; b = 3
# Например, если a = 8, b = 3,напечатать
# ```
# 8 + 2 = 10
# 8 - 2 = 6      ??? Ok       
b = b - 1
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} % {b} = {a%b}")
print(f"{a} ** {b} = {a**b}")

print('\n')

#5 Split Two-digit Number
number = 34
print(number // 10, number % 10)

print('\n')

#6 Research Square 
side = 5
area = side ** 2
perimeter = side * 4
print(f"Area of a square with side {side} is {area}")
print(f"Perimeter of a square with side {side} is {perimeter}")

print('\n')

#7 Time is Flying
h = 1; min = 23; sec = 34
if h == 0 & min == 0 & sec ==0 : print('You was going to bed on time!') 
else : print(F"You wasted {h*3600+min*60+sec}sec of your life")

print('\n')

#8 Chessboard and Rice
print(2 ** 63)
