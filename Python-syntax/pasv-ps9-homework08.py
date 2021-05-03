# Homework 8

def opposite(n):
  return -n

def angles_of_polygon(n):
  if n < 3: return -1 # Not a polygon
      else: return 180 * (n − 2)

def miles_to_feet(x):
  return x * 5280

def count_bmi(weight, height):
  bmi = weight / height ** 2
  for rate,status in [(18.5,'Underweight'),(25,'Normal'),(30),'Overweight']:
    if bmi <= rate: return status
  return 'Obese'

def planeta_name(n):
  return ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"][n-1]
  
def square_of_triangle(a,b,c):
  if 2 * max(a,b,c) >= sum(a,b,c): 
    return "The triangle does not exist"
  p = (a + b + c) / 2
  return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def dividers_num(n):
  s = 0
  for i in range(n+1):
    if n%i == 0: s+= 1
  return s
