import time
import random

casinoText = """
 .d8888b.        d8888  .d8888b. 8888888 888b    888  .d88888b.  
d88P  Y88b      d88888 d88P  Y88b  888   8888b   888 d88P" "Y88b 
888    888     d88P888 Y88b.       888   88888b  888 888     888 
888           d88P 888  "Y888b.    888   888Y88b 888 888     888 
888          d88P  888     "Y88b.  888   888 Y88b888 888     888 
888    888  d88P   888       "888  888   888  Y88888 888     888 
Y88b  d88P d8888888888 Y88b  d88P  888   888   Y8888 Y88b. .d88P 
 "Y8888P" d88P     888  "Y8888P" 8888888 888    Y888  "Y88888P"
 """

emojies = [
    "\U0001F355", # cherry
    "\U0001F354", # barbarbar
    "\U0001F32E", # barbar
    "\U0001F32F", # bar
    "\U0001F363", # 7
]

class player:
    def __init__(self):
        self.Balance = 10

    def getBalance(self):
        return self.Balance

    def printBalance(self):
        print("Balance: " + str(self.Balance))

    def addBalance(self, amt):
        self.Balance = self.Balance + amt

class slots:
    def spin(self):
        number = len(emojies)-1
        return [random.randint(0, number), random.randint(0, number), random.randint(0, number)]

    def toEmojies(self, array):
        data = "[ "
        for number in array:
            data = data + (emojies[number] + " ")
        data = data + "]"
        return data

    def getWinnings(self, array):
        count = 0
        for number in array:
            if number == 0:
                count = count + 1
        if count == 3:
            return 5
        elif count > 1:
            return 1.5

        count = 0
        for number in array:
            if number == 1:
                count = count + 1
        if count == 3:
            return 10

        count = 0
        for number in array:
            if number == 2:
                count = count + 1
        if count == 3:
            return 40

        count = 0
        for number in array:
            if number == 3:
                count = count + 1
        if count == 3:
            return 160

        count = 0
        for number in array:
            if number == 4:
                count = count + 1
        if count == 3:
            return 1000
        
        return 0

player = player()
slots = slots()

print(casinoText)
print("Welcome to the casino! Remeber you are always getting closer to winning the jackpot!")
input("[ ENTER ] to play slots")

print("""
Results:
[ \U0001F355 \U0001F355 \U0001F355 ]: £1.5
[ \U0001F354 \U0001F354 \U0001F354 ]: £10
[ \U0001F32E \U0001F32E \U0001F32E ]: £40
[ \U0001F32F \U0001F32F \U0001F32F ]: £160
[ \U0001F363 \U0001F363 \U0001F363 ]: £1000""")

while True:
    print("\n")

    player.printBalance()
    input("[ ENTER ] to spin £1")
    player.addBalance(-1)

    if player.getBalance() < 0:
        print("\n")
        print("It appears your bankrupt!")
        input("[ ENTER ] for a £10 loan")
        player.addBalance(10)
        print("\n")
    
    numbers = 0
    for i in range(10):
        numbers = slots.spin()
        print(slots.toEmojies(numbers), end="\r")
        time.sleep(1/20)
    print("")
    winnings = slots.getWinnings(numbers)
    print("You won: " + str(winnings))
    player.addBalance(winnings)
