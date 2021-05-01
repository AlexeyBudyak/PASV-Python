# Homework 6, Cycles

# Ex.1 Monkey
monkey = ''
for i in range(10):
    monkey+= f"{i+1} monkey{'s' * bool(i)} "
print(monkey)
print()

# Ex.2 Seconds
seconds = monkey.replace('y ','y-').replace('s ','s-').split('-')[:-1]
seconds.reverse()
seconds = ' '.join(seconds).replace('monkey','second')
print(seconds)
print()

# Ex.3 n ** k
c = n = int(input('Enter number n '))
k = int(input('Enter power k '))
for i in range(k-1): c*= n
print(f"{n} ** {k} = {c}")
print()

# Ex.4 Runner
d = 5
for i in range(10):
    print(f"Day {i+1}: {round(d,2)}km")
    d*= 1.05
print()

# Ex.5 Student
s = w = 5
n = int(input('Enter a goal number for study English words '))
for d in range(n):
    if s >= n: break
    w+= 2; s+= w
print(f"Student need {d+1} day{'s' * bool(d)}")
print()

# Ex.6 Steps
n = int(input('Enter number of steps '))
steps = ''
for i in range(n):
    steps+= ' ' * i + '#\n'
steps = steps.strip('\n')
print(steps)

# Ex.7 Stars
wide = int(input('Enter the width of the diamond (odd number) '))
diamond = ''
for i in range(wide,0,-2):
    # piece = ' ' * ((wide - i) // 2) + '*' * i + '\n'  # another option
    piece = ('*' * i).center(wide) + '\n'
    diamond = f"{piece}{diamond}{piece * bool(wide - i)}"  # * bool(wide - i)   - to avoid duplicate middle part
print(diamond)
