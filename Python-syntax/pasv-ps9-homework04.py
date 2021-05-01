# Homework 04

# Introduction
# Research class examples (without Google):
# print(day in [1,2,3,4,5,6,7]) <- What is [1,....,7]?
print(type([1,2,3,4,5,6,7])) # Ok, it's 'list'
print('A little research about \'list\' type')
# Could we use variable for this?
a = [1,2,3,4,5,6,7]
print(a) # Yes we could
# Could we use indexes?
print(a[3]) # Yes
# Could we use [being:end:step] form as in strings?
print(a[-1:3:-1]) # Yes
# Is it mutuble?
a[2] = 8
print(a) # Yes
# Could be used different types of data?
a[3] = 'Test'
print(a) # Yes
print()

# Ex.1. The first letter of the name
name = input('What is your name? ')
vowels = 'aeiou'
if name[0].lower() in vowels:
  cute_name = ['Angel, you are so bright',
              'Eiffel tower'
              'Iris, a beutiful flower' ,
              'Olive at a beutiful garden',
              'Unlimited gifted student'][vowels.find(name[0].lower())]
  print(f'Your name start with vowel \'{name[0]}\' as {cute_name}!')
else:
  print(f'Your name start with consonant. Such a nice name!')
print()

# Ex.2. Name length
# Will use already entered name
if len(name) <= 5 :
  print('I like your short name!')
  pref_name = name
else :
  # create nice short name that ends with consonant 
  if name[4] not in vowels:
    short_name = name[:5]
  elif name[3] not in vowels:
    short_name = name[:4]
  elif name[2] not in vowels:
    short_name = name[:3]  
  else:
    short_name = name[:2]
  permit=input(f'Your name is long, my I call you \'{short_name}\' for short? ')
  if permit.lower() in ['yes','y','ok','sure','np','yep']:
    pref_name = short_name
  else:
    pref_name = name;
  print(f'Ok, I\'ll call you \'{pref_name}\'')

# Ex.3. Good time
time = input(f'{pref_name}, what\'s time now? (Ex: 3:25pm or 15:25) ')
#  if only hours in input, without minutes
if ':' not in time:  
  if 'm' in time:
    time = time[:-2] + ':00' + time[-2:]
  else:
    time = time + ':00' 
hr = int(time[:time.find(':')])
if 'm' in time:
  if 'p' in time:
    if hr < 12:
      hr+= 12
  else:
    if hr == 12 :
      hr = 0
if hr not in range(0,24):
  print('Wrong time')
else:
  times_of_day = ['night','morning','day','evening']
  print(f'Good {times_of_day[hr//6]}, {pref_name}!')
  print()

# Ex.4. Shopping
price = float(input(f'{pref_name}, What\'s price of a merchandise? '))
if price >= 300:
  discount_pr = 30
elif price >= 200:
  discount_pr = 20
elif price >= 100:
  discount_pr = 10
else:
  discount_pr = 0
discount = round(price * discount_pr / 100,2)
expense = price - discount;
print(f'You had {discount_pr}% discount (${discount}, total expense is ${expense}')
print()

# Ex.5. Age season
age = int(input('Input a human age '))
print('Chidren' if age<=16 else 'Young man' if age < 50 else 'Senior')
print()

# Ex.6. Traffic light
lights = ['red', 'yellow', 'green', 'red']
# light = input(f'Enter traffic light ({lights[:3]}) ')
# print(lights[lights.index(light)+1])
print(lights[lights.index(input(f'Enter traffic light ({lights[:3]}) '))+1])
print()

# Ex.7. Day of the week
num_of_day = int(input('Enter number of a day of a week (1 - 7) '))
print('Weekday' if num_of_day < 6 else 'Weekend')

# Or in one line:
# print('Weekday' if int(input('Enter number day of week (1 - 7) ')) < 6 else 'Weekend')
print()

# Ex.8. Happy number
x = input('Enter any long size number ')
s = 0;
# By intuition reserch operator 'for' (see introduction)
for n in x:
  s+=int(n)
print(f"{'Not a l' if s % 9 else 'L'}ucky number")
