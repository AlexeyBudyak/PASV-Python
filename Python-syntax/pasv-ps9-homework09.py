import numpy
arr = [1,2,3,4,5,-1,-3,-7,1,15,20]
arr_str = ['apple','appricot','pineapple','banana','grape','plum', 'orange']
vowels = 'aeuio'

print(f'1. {sum(arr[1::2])}')
print(f'2. {numpy.prod(arr[0::2])}')
print(f'3. {round(sum(arr)/len(arr),2)}')
print(f'4. {sum(int(el < 0) for el in arr)}')
print(f'5. {sum(int(len(el)==5) for el in arr_str)}')
# print(f'6. {sum('aeuio'.count(el[0]) for el in arr_str)}'). - не работает с тернарным циклом
print(f'6. {sum(vowels.count(el[0]) for el in arr_str)}')
print(f'7. {[0]*10}')
print(f'8. {list(range(1,11))}')
print(f'9. {list(range(0,20,2))}')
print(f'10. {list(range(1,20,2))}')
print(f'11. {[2 ** x for x in range(10)]}')
str= input('Enter string ')
print(f'12. {[x for x in str]}')
c = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
print(f'13. {[x * 9/5 + 32 for x in c]}')
f = [0, 1]
for i in range(8):
  f.append(sum(f[-2:]))
print(f'14. {f}')
