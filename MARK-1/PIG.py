import random 
#there are flaws in this game still figureing it out!
#not the best one bt works just fine

def main():
    game_setter(player_setter())


def game_setter(x):
    max_score = 50
    player_scores = [0 for _ in range(x)]  

    while max_score > max(player_scores):
        for player_index in range(x) : 
            current_score = 0


            while True : 
                print("If you want to dice yes if not press any other key")
                should_dice = input(f"Player {player_index+1}, Do you want to dice : ").lower()
                if should_dice != "yes" : 
                    break
                value = roll()
                if value == 1 : 
                    print(f"Player {player_index+1} got a 1")
                    current_score = 0
                    break 

                current_score += value
                print(f"Player ({player_index+1}) diced  : {value}")
                print(f"Player ({player_index+1}) total score : {current_score}")

            if current_score == 0: 
                player_scores[player_index]  = current_score
            else : 
                player_scores[player_index] += current_score

            print(f"Player {player_index+1} Final Score : {player_scores[player_index]}")

    max_score = max(player_scores)
    winning_index = player_scores.index(max_score)
    print(f"Player {winning_index+1} won the match with a score of : {max_score}")


def player_setter():
    while True: 
        try : 
            player = int(input("Enter the amount of player that will play (2-4): "))
            if player < 2 or player > 4 : 
                print("Please Enter a number range in 2-4")
                
            else : 
                return player
        except ValueError :
            print("Error: Please enter a valid nunber between 2-4 ")


def roll():
    max_dice=6
    min_dice=1
    
    return random.randint(min_dice , max_dice)

if __name__ == "__main__" :
    main()