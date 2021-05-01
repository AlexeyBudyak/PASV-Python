# 1. Name research
import random
name = input('What\'s your name? ')
if bool(random.getrandbits(1)) :
  intro = '{}, you name '.format(name)
  lt = 'letter'
  wlt = 's with ' + lt
  print(f'{intro} has {len(name)} {lt}s')
  print(f'{intro} start{wlt} {name[0]}')
  print(f'{intro} end{wlt} {name[-1]}')
elif bool(random.getrandbits(1)) :
  print(f'{name}, your name has {len(name)} letters')
  print(f'{name}, your name starts with letter {name[0]}')
  print(f'{name}, your name ends with letter {name[-1]}')
else :
  print('{0}, your name has {n} letters\n {0}, your name starts with letter {l1}\n {0}, your name ends with letter {l_end}'.format(name,n=len(name),l1 = name[0],l_end=name[-1]))

print()

# 2. Mirror name
# name = input('What\'s your name? ')
# (we already know your name)

mirror_name = name[-1].upper() + name[-2::-1].lower()
print(f'{name}, your mirror name is {mirror_name}')
print()

# 3. Phone format
pn = input('Enter 10 digits phone number ')
pn = (pn + '0000000000')[:10] # Make sure it's 10 digits
# Creating format (+012) 345-6789 (0-9 - indexes)
pn = '(+' + pn[0:3] + ') ' + pn[3:6] + '-' + pn[6:]
print(pn)
print()

# 4. email generator
fname = input('What\'s your full name? ')
i = fname.find(' ')
email1 = fname[0:i] + '.' + fname[i+1:] + '@company.com'
email2 = fname[i+1:] + '.' + fname[0:i] + '@company.com' 
email3 = fname[0] + '.' + fname[i+1:] + '@company.com'
email4 = fname[i+1:] + pn[-4:] + '@company.com'
print('Available emails for registration:')
print(email1)
print(email2)
print(email3)
print(email4)
print()

# 5. frame your name
print('*' * (len(name)+4))
print('* ' + name + ' *')
print('*' * (len(name)+4))
print()

print('╔' + '═' * (i + 2) + '╦' + '═' * (len(fname) - i + 1) + '╗')
print('║ ' + fname[0:i] + ' ║ ' + fname[i+1:] + ' ║')
print('╚' + '═' * (i + 2) + '╩' + '═' * (len(fname) - i + 1) + '╝')
