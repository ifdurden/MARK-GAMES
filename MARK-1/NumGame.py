#the most simplest one yet 
import random
og_num = random.randint(1 ,11)
count = 1

while True: 
    try:
        number = int(input("Enter a number between (1-10): "))
        if number > 10 : 
            print("The Range Between The Number Should be 1-10")
        elif number < og_num : 
            print("Too low")
            count+=1
        elif number >  og_num : 
            print("Too high")
            count+=1
        else :
            print("*************************************")
            print(f"The random number : {og_num}")
            print(f"The number You choice : {number}")
            break
            
    except ValueError  :
            print(f"Error : Inputed A String When Asked For Nunber")
            print("Please enter a number.")


print("They Matched!")
print(f"It Took You {count} Tries")