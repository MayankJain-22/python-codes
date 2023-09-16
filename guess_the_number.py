print("\t\tYOU HAVE TO GUESS THE NUMBER \n \nTotal numbers of tries are 9\n")
num = 45
tries = 9
while(1):
    ans = int(input("Enter the no. ->"))
    tries = tries-1
    if tries == 0:
        print("\n->GAME OVER\n")
        print("numbers of tries used = ",9-tries,"\n")
        print("do you want to play again \n if yes enter 1 and if no then enter 2")
        play1 = int(input())
        if play1 == 1 :
            tries=9
            continue
        elif play1 == 2:
            print("thank you for playing")
            break
        else:
            print("enter 1 or 2")
        break
    elif ans>num:
        
        print("->The number is less than" ,ans,"\n" )
        print("->Number of tries left is", tries,"\n")
        print("->Numbers of tries used = ",9-tries ,"\n")
        continue
    elif ans<num:
        
        print("->the number is more than" ,ans,"\n" )
        print("->number of tries left is", tries,"\n")
        print("numbers of tries used = ",9-tries,"\n")
        continue
    
    else:
        print("->CONGRATULATIONS!,you have guessed the correct number\n")
        print("numbers of tries used = ",9-tries,"\n")
        print("do you want to play again\nif yes enter 1 and if no then enter 2")
        play1 = int(input("->"))
        if play1 == 1 :
            tries=9
            continue
        elif play1 == 2:
            print("thank you for playing")
            break
        else:
            print("enter 1 or 2")
        break
