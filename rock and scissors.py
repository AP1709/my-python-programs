import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
x= int(input("Choose 1 for hand , 2 for paper and 3 for scissors\n"))
print("You choose")
if x==1:
  print(rock)
if x==2:
  print(paper)
if x==3:
  print(scissors)
a=random.randint(1,3)
print("computer chooses")
if a==1:
  print(rock)
if a==2:
  print(paper)
if a==3:
  print(scissors)
if x==a:
  print("Draw")
if x ==1 and a==3:
  print("User win")
if x==3 and a ==2:
  print("User wins")
if x==2 and a==1 :
  print("User wins")
else:
  print("Computer wins")
