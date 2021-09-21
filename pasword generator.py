import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
pa=""
import random
s=[]
for i in range(0,nr_letters):
  b=random.choice(letters)
  s.append(b)
for n in range(0,nr_numbers):
  c=random.choice(numbers)
  s.append(c)
for t in range(0,nr_symbols):
  d=random.choice(symbols)
  s.append(d)

#going for suffle password or hard one
pa1=""
random.shuffle(s)
for q in range(0, len(s)):
  pa1 +=s[q]
print(pa1)