import random
import re

# Ex.1 I wish I have eyes like yours
colors = ['green', 'blue', 'brown', 'black', 'gray', 'hezel'];
phrase = "My eyes are green too!"
phrase = phrase.replace('green', colors[random.randint(0, 5)])
my_eyes_color = phrase[len('My eyes are '):-len(' too!')] # actual color
print(phrase[:-len(' too!')])
your_color = input('What is your favorite color? ').lower()
if your_color != my_eyes_color:
  print('I changed my mind!')
  phrase = phrase.replace(my_eyes_color, your_color)
print(phrase)
print()

# Ex.2 Fun bussines card
print("Let's do your personal bussiness card!")
s1 = input("What's your first name? ")
s2 = input("What's your middle name? ")
s3 = input("What's your last name? ")
eyes_color = 'Eyes color: ' + your_color
text_width = max(len(s1),len(s2),len(s3),len(eyes_color) - 9)
p0 = '╓────────┬─' + '─' * text_width +          '─╖'
p1 = '║ 😀 Just │ ' + s1.rjust(text_width,' ') + ' ║'
p2 = '║ a nice │ ' + s2.rjust(text_width, ' ') + ' ║'
p3 = '║ person │ ' + s3.rjust(text_width, ' ') + ' ║'
p4 = '╟────────┴─' + '─' * text_width +          '─╢'
p5 = '║ ' +  eyes_color.center(text_width + 9) + ' ║'
p6 = '╙──────────' + '─' * text_width +          '─╜'

print(f"{p0}\n{p1}\n{p2}\n{p3}\n{p4}\n{p5}\n{p6}\n")

# Ex.3 Replace trouble

s = "We like Python & Python likes us, but Redex doesn't work for replace() function :-("
s = re.sub('[aeuio]', '', s)
print(s)
print()

# Ex.4 Simple replacement, one line code

print('Fixed text: ' + \
  input('Enter a sentence ')\
  .replace(\
    input("What's word would you like to replace? "),\
    input('On what word would you like to replace? ')))


# Ex.5 Going to clean summer
s = "1]04 35-%^&?!!@({2 345I like summer52345 $#%^ $&*?"
unwanted = '0123456789-^%&?!@(){}[]*$# '
s = s.lstrip(unwanted); n = len(s)
s = s.rstrip(unwanted); n = n - len(s)
print(s + '!' * n)
