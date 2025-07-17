def load_txt():
    with open("typwar.txt" , "r") as file : 
        line = file.readlines()
        return random.choice(line)