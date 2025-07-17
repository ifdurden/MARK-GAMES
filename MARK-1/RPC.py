import random

def main():
    printingout()

#simple rock paper and scissor game hope you enjoy it!

def printingout():
    print("Press R for Rock")
    print("Press P for Paper")
    print("Press S for Scissor")
    print("************************************")
    count = 0
    score = 0

    while count != 3: 
        print(f"Round: {count+1}/3")
        x= get_user_input()
        y = get_random_input()
        print(f"Your chose : {x}")
        print(f"The Computer Chose: {y}")

        z = get_winner(x,y)
        if z == 1 : 
            print("You win")
            score += 1
        elif z == 2 :
            print("You lose!")
        else: 
            print("It's a draw")
        count += 1
    if score >= 2 : 
        print("You have done really well!")
    print(f"Your Score : {score}/{count}")

    
def get_random_input():
    
    r = random.randint(1,3)
    match r: 
        case 1 : return "Rock"
        case 2 : return "Paper"
        case 3 : return "Scissor"

def get_user_input():
    while True : 
        move = input("Enter R / P / S or Q to quit: ").capitalize()
        if move == "Q" : 
            quit()
        elif move in ["R" , "P", "S"]: 
            if move == "R" :
                return "Rock"
            elif move == "P": 
                return "Paper"
            elif move == "S" : 
                return "Scissor"
        else :
            print("Please Enter Either R , P or S ")

def get_winner(x , y):

    if (x=="Rock" and y=="Scissor") or (x=="Paper" and y =="Rock") or (x=="Scissor" and y=="Paper"):
        return 1

    elif (x=="Rock" and y=="Paper") or (x=="Paper" and y=="Scissor") or (x=="Scissor" and y=="Rock"):
        return 2

    elif x == y: 
        return 3

if __name__ == "__main__":
    main()