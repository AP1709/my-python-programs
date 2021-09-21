def prime_checker(number):
  is_prime = True
  if number == 1:
    print("It's a prime number")
  for i in range(2,number):
    if number % i == 0:
      is_prime = False
  if is_prime == True  :
    print(f"{number} is a prime no")
  else:
    print(f"{number} is a not prime no")

n = int(input("Check this number: "))
prime_checker(number=n)
