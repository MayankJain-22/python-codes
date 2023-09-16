import random
def func1():
    print("total no of user win = " , userwin)
    print("total no. of computer win = " , compwin)
    print("total no. of game left = " ,tries,"\n" )
tries = 10
userwin = 0
compwin = 0
list1 = ["snake" , "water" , "gun"]

while(1):
    while(tries>0):
        a = random.choice(list1)
        b = input("enter your choice \nenter s for snake\nenter w for water\nenter g for gun\nenter your choice here : ")
        print("\ncomputer selected- ", a ,"\n")


        if b == "s" and a == "snake":
            print("match is a tie\n")
            tries = tries - 1 
            func1()
            continue
        elif b == "s" and a== "water":
            print("you won\n")
            tries = tries - 1
            userwin = userwin + 1
            func1()
            continue
        elif b=="s" and  a == "gun":
            print("you lost\n")
            tries = tries - 1
            compwin = compwin + 1
            func1()
            continue


        elif b == "w" and a == "water":
            print("match is a tie\n")
            tries = tries - 1 
            func1()
            continue
        elif b == "w" and a== "gun":
            print("you won\n")
            tries = tries - 1
            userwin = userwin + 1
            func1()
            continue
        elif b == "w" and  a == "snake":
            print("you lost\n")
            tries = tries - 1
            compwin = compwin + 1
            func1()
            continue


        elif b == "g" and a == "gun":
            print("match is a tie\n")
            tries = tries - 1 
            func1()
            continue
        elif b == "g" and a== "snake":
            print("you won\n")
            tries = tries - 1
            userwin = userwin + 1
            func1()
            continue
        elif b == "g" and  a == "water":
            print("you lost\n")
            tries = tries - 1
            compwin = compwin + 1
            func1()
            continue
    if userwin > compwin:
        print("\nCONGRATULATION , you WON this match\n")

    elif userwin == compwin:
        print("\nThe match is TIED")
          
    else:
        print("\nyou LOST this match")
    a =input("do you want to play again\nenter yes or no\n")
    if a == "yes":
        tries = 10
        userwin = 0
        compwin = 0
        continue
    elif a == "no":
        print("\nthank you for playing")
        break    
        