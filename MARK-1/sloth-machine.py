"""
DON'T GET ADDICTED TO IT!!!
"""
import random

MAX_LINES = 3
MAX_DEPOSIT = 100
ROWS = 3
COLS = 3

SYMBOLS_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

SYMBOL_VALUES = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


class SlotMachine:
    def __init__(self, rows, cols, symbols, values):
        self.rows = rows
        self.cols = cols
        self.symbols = symbols
        self.values = values
        self.balance = 0

    def deposit(self):
        while True:
            try:
                amount = int(input(f"Enter deposit amount (max ${MAX_DEPOSIT}): $"))
                if 1 <= amount <= MAX_DEPOSIT:
                    self.balance = amount
                    break
                print(f"Amount should be between $1 and ${MAX_DEPOSIT}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_lines(self):
        
        while True:
            try:
                lines = int(input(f"Enter number of lines to bet on (1-{MAX_LINES}): "))
                if 1 <= lines <= MAX_LINES:
                    return lines
                print(f"Please enter a number between 1 and {MAX_LINES}.")
            except ValueError:
                print("Invalid input. Please enter a number.")


    def get_bet(self, max_bet):
        while True:
            try:
                bet = int(input("Enter your bet per line: $"))
                if 1 <= bet <= max_bet:
                    return bet
                print(f"Bet must be between $1 and ${max_bet}.")
            except ValueError:
                print("Invalid input. Please enter a number.")



    def spin(self):
        all_symbols = []
        for symbol, count in self.symbols.items():
            all_symbols.extend([symbol] * count)

        columns = []
        for _ in range(self.cols):
            column = []
            available = all_symbols[:]
            for _ in range(self.rows):
                choice = random.choice(available)
                available.remove(choice)
                column.append(choice)
            columns.append(column)
        return columns


    def print_spin(self, columns):
        for row in range(self.rows):
            row_symbols = [columns[col][row] for col in range(self.cols)]
            print(" | ".join(row_symbols))



    def calculate_winnings(self, columns, lines, bet):
        winnings = 0
        winning_lines = []
        for line in range(lines):
            symbol = columns[0][line]
            if all(col[line] == symbol for col in columns):
                win = self.values[symbol] * bet
                winnings += win
                winning_lines.append((line + 1, symbol, win))
        return winnings, winning_lines



    def log_result(self, total_bet, winnings, winning_lines):
        with open("game_log.txt", "a") as file:
            file.write(f"Total bet: ${total_bet} | Winnings: ${winnings}\n")
            for line, symbol, win in winning_lines:
                file.write(f"  Line {line}: {symbol} - Won ${win}\n")
            file.write("\n")



    def play_round(self):
        lines = self.get_lines()
        while True:
            bet = self.get_bet(self.balance // lines)
            total_bet = bet * lines
            if total_bet <= self.balance:
                break
            print(f"Insufficient balance. You need ${total_bet}, but have ${self.balance}.")

        print(f"\nBetting ${bet} on {lines} line(s) - Total Bet: ${total_bet}")
        columns = self.spin()
        self.print_spin(columns)
        winnings, winning_lines = self.calculate_winnings(columns, lines, bet)


        if winnings > 0:
            print(f"\n🎉 You won ${winnings}!")
            for line, symbol, amount in winning_lines:
                print(f"  Line {line} matched with '{symbol}' for ${amount}")
        else:
            print("\nNo wins this time.")

        self.balance += winnings - total_bet
        print(f"Your updated balance: ${self.balance}")
        self.log_result(total_bet, winnings, winning_lines)


    def start(self):
        print("🎰 Welcome to the Slot Machine Game! 🎰")
        self.deposit()

        while self.balance > 0:
            choice = input("\nPress Enter to play, type 'auto' for 5 rounds, or 'q' to quit: ").lower()
            if choice == 'q':
                print("Thanks for playing!")
                break
            elif choice == 'auto':
                for i in range(5):
                    print(f"\n🔁 Auto-spin Round {i + 1}")
                    if self.balance <= 0:
                        print("Balance too low to continue auto-spins.")
                        break
                    self.play_round()
            else:
                self.play_round()

        if self.balance <= 0:
            print("💸 You're out of money. Game over!")


if __name__ == "__main__":
    machine = SlotMachine(ROWS, COLS, SYMBOLS_COUNT, SYMBOL_VALUES)
    machine.start()
