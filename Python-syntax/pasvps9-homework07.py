'''
 Hello Larisa, just for push myself for harder tasks and for your fun I made a tetris game for open the homework 😁
 If it's too long and boring it has hidden commands:
 '+' - add 100 points (release one code line)
 'homework' - show all homework

 On replit pseudographics looks different and much worse compare to PyCharm will keep it in mind next time
'''

homework = ["import re",
            "s = input('Enter string ')",
            "cap = len(re.sub('[^A-Z]','', s))",
            "print('Capital letters:',cap) # Ex.1",
            "print('Vowels: ',len(re.sub('[^aeuioAEUIO]','', s)))  # Ex.2",
            "print(''.join(c+'*' for c in s)[:-1]) # Ex.3",
            "print(''.join(c+' ' * (not c.isalpha()) for c in s))  # Ex.4",
            "vow = 'aeuioAEUIO'",
            "print(''.join(c.upper()*(c in vow)+c.lower()*(c not in vow) for c in s)) # Ex.5",
            "print(s[0::2],s[1::2]) # Ex.6",
            "print(s.upper() * (cap > len(s)/2) + s.lower() * (cap <= len(s)/2)) # Ex.7"]

import random

def fig_out(x, fig): # Display a tetris piece for drop off
    s = ''
    for i in range(4):
        if i < len(fig):
            print(' ' * (x * 2 + 1) + fig[i])

def glass(cont, score):    # Display tetris field
    global homework
    sc = score
    if score >= 1000000: sc = 'Cheating!'
    for i,y in enumerate(cont):
        line = '▍' + y + '▐'
        if not i: line+= f'  Score: {sc}'
        if i > 1 and i <= len(homework)+1 and score >= (i-1) * 100: line+= f'  {homework[i-2]}'
        print(line)
    print('▀' + '▀' * 20 + '▀')

def rotate(x, f, figs): # Rotation of a tetris piece
    f[1] = f[1] + 1
    if f[1] >= len(figs[f[0]]):
        f[1] = 0
    wide_fg = len(figs[f[0]][f[1]][0]) // 2
    if x + wide_fg > 10:
        x = 10 - wide_fg
    return (x,f)

def drop_height(cont, x, fig):      # Calculation drop off height for a tetries piece
    arr_h = []
    for i in range(len(fig[0])//2):
        h = 0
        while h< 20 and cont[h][x*2+i*2] == '.' : h+= 1
        if h < 20:
            for j in range(len(fig)-1,-1,-1):
                if fig[j][i * 2] == ' ': h+= 1
        arr_h = arr_h + [h - len(fig)]
    return min(arr_h)

def dropoff(cont,x,fig):    # dropp of a tetris piece
    h = drop_height(cont, x, fig)
    for i in range(len(fig)):
        line = ''
        for j in range(0,20,2):
            if j in range(x*2, x*2 + len(fig[i])) and fig[i][j - x*2] == '█':
                line+= '█▉'
            else:
                line+= cont[h+i][j:j+2]
        cont[h+i] = line
    return cont

def new_piece():
    return (3,[random.randint(0, 6), 0])

def reduction_check(cont):
    n = 0
    for i in range(20):
        print(i, cont[i].find('.'))
        if cont[i] == '█▉' * 10:
            n  = n + 1
            cont = ['. '*10] + cont[:i] + cont[i+1:]
    return (cont, [0,100,300,700,1500][n])

figs = [[['█▉█▉',
          '█▉█▉']],

        [['█▉',
          '█▉',
          '█▉',
          '█▉'],
         ['█▉█▉█▉█▉']],

        [['█▉█▉█▉',
          '  █▉  '],
         ['█▉  ',
          '█▉█▉',
          '█▉  '],
         ['  █▉  ',
          '█▉█▉█▉'],
         ['  █▉',
          '█▉█▉',
          '  █▉']],

        [['█▉█▉  ',
          '  █▉█▉'],
         ['  █▉',
          '█▉█▉',
          '█▉  ']],

        [['  █▉█▉',
          '█▉█▉  '],
         ['█▉  ',
          '█▉█▉',
          '  █▉']],

        [['█▉█▉',
          '  █▉',
          '  █▉'],
         ['█▉█▉█▉',
          '█▉    '],
         ['█▉  ',
          '█▉  ',
          '█▉█▉'],
         ['    █▉',
          '█▉█▉█▉']],

        [['█▉█▉',
          '█▉  ',
          '█▉  '],
         ['█▉    ',
          '█▉█▉█▉'],
         ['  █▉',
          '  █▉',
          '█▉█▉'],
         ['█▉█▉█▉',
          '    █▉']]
        ]

(x,f) = new_piece() # x - position before drop off, f - Number of figure and its rotate stage
c = ''
cont = ['. '*10]*20 # Content of the glass
score = prize = 0
while c != 'x':
    fig_out(x,figs[f[0]][f[1]])
    glass(cont, score)
    c = input('Enter command: L - left, R - right, O - rotate, D - drop, X - Exit ').lower()
    if c == 'l' and x:
        x-= 1
    if c == 'r' and x + len(figs[f[0]][f[1]][0]) / 2 < 10:
        x+= 1
    if c == 'o':
        (x,f) = rotate(x,f,figs)
    if c == 'd':
        cont = dropoff(cont,x,figs[f[0]][f[1]])
        (cont,prize) = reduction_check(cont)
        score+= prize
        (x,f) = new_piece()
    if c == '+':
        score+= 100
    if c == 'homework':
        score = 1000000
    if cont[0] == '█▉' * 10:
        print('Game Over!')
        break
    print('\n'*100)
