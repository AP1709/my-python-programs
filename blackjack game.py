import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
l1=[] #for user
l2=[] #for computer
def deal_card():
    for i in range (0,3):
        a= random.randint(0,10)
        b = cards[a]
        l1.append(b)
    for j in range(0,3):
        a1= random.randint(0,10)
        b1 = cards[a]
        l2.append(b)
    print(f"The user card is{l1[0]} and {l1[1]}")
    print(f"Computer card is {l2[0]} ")
    user_input = input("press 'y' if u wanna continue else press 'n'\n").lower()
    if user_input == 'n':
        add1 = l1[0]+l1[1]
        add2 = l2[0]+l2[1]
        if add1 < add2 :
            print("User wins")
        elif add2 < add1:
            print("Sorry you lost")
            print(f"computer cards are {l2[0]} and {l2[1]}")
        else:
            print ("draw")
    if user_input == 'y':
        print(f"User cards are {l1} ")
        if sum(l1) > 21 or sum(l1) < sum(l2) :
            print ("you lose")
        else:
            print (f"Computer cards is {l2}")
            print ("you win")

#for looping the process
deal_card()
flag= True
while flag:
    user_in2 = input("if u wanna play a new game press 1 esle press 2 to exit\n")
    if user_in2 == '1':
        deal_card()
        flag = True
    else:
        print ("thank you for using our game")
        flag = False
