import random
import time
MAX_OPERAND = 15
MIN_OPERAND = 3
OPERATOR = ["+" , "-" , "*"]
TOTAL_PROBLEMS = 10

def get_question():
    
    left = random.randint(MIN_OPERAND , MAX_OPERAND)
    right = random.randint(MIN_OPERAND , MAX_OPERAND)
    operator = random.choice(OPERATOR)    
    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression)
    return expression , answer

def get_input():
    input("Press enter to continue")
    print("------------------------")
    start = time.time()
    for i in range (TOTAL_PROBLEMS):
        expression , answer = get_question()
        while True :
            try:
                ans = int(input(f"Problem #{i+1} : {expression} = "))
                if ans == answer : 
                    break
            except ValueError: 
                print("Error!Please enter a valid number!")
    end = time.time()
    total = round(end - start , 2)
    if total <=20 :
        print("Congrts!!")
        print(f"You have done it in {total} seconds well done")
    else :
        print(f"It took you: {total} seconds")
    
def main():
    get_input()

if __name__ == "__main__":
    main()
#and that was a math thing simple really!
#how fast can you solve these problem