# Homework Python Syntax #2

# Ex.1 Find sum of 3 digits
digits = input('Input 3-digits ')
# Take 3 last digits in case that input was not 3 digits
digits = ('000'+ digits)[-3:] 
sum = int(digits[0]) + int(digits[1]) + int(digits[2])
print(f'Sum of 3 digits ({digits}) is {sum}')

print()

# Ex.2 Sum of polygon angles
sides = int(input('Input number of sides in polygon '))
angles_sum = (sides - 2) * 180
if(sides < 3) : print("It's not a polygon") 
else : print(f"Polygon with {sides} sides has {angles_sum}° sum of angles")

print()

# Ex.3 Mile convertor
print('mi -> km & mi -> ft convertor')
mi = float(input('Input miles '))
print(f"-> {round(mi * 1.60934,2)}km") # round to 10m
print(f"-> {round(int(mi * 5280),-2)}ft") # round to 100 ft

print()

# Ex.4,5 °C -> °F & °F -> °C convertor
print('°C -> °F & °F -> °C convertor')
print('Input temperature with degree type (for example 32F or 0C)');
T = input();
# Handling formats '20°F', '20F' and '20'
if(T[-2] == '°'): t = float(T[0:-2]) 
elif(T[-1] == 'F' or T[-1] == 'C' or T[-1] == '°'): t = float(T[0:-1]) 
else: t = float(T)
# if no degree sign, it will be F
if(T[-1]=='C'):  print(f"-> {round(1.8 * t + 32,2)}°F")
else: print(f"-> {round((t - 32) * 5/9,2)}°C")

print()

# Ex.6 Tips
value = float(input('Input value of order '))
print('Tips suggestion:')
print(f"Perfect service 20% (${round(value * 0.2, 2)})")
print(f"Good service 15% (${round(value * 0.15, 2)})")
print(f"Ok service 10% (${round(value * 0.1, 2)})")
tips_percent = float(input('Tips % '))
tips = round(value * tips_percent / 100, 2)
tax_percent = float(input('Tax % '))
tax = round(value * tax_percent / 100, 2)
total = value + tips + tax
print();
print(f"Value: ${value}")
print(f"Tips: ${tips}")
print(f"Value: ${tax}")
print('-------------------')
print(f"Total: ${tax}")

print();

# Ex.7 Sale
price = float(input('Price after discount: '))
sale = float(input('Discount % '))
full_price = round(price / (1 - sale / 100),2);
print(f'Full price ${full_price}')
