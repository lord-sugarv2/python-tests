import random
import tkinter as tk
import time

emojies = [
    "\U0001F355", # cherry
    "\U0001F354", # barbarbar
    "\U0001F32E", # barbar
    "\U0001F32F", # bar
    "\U0001F363", # 7
]

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

Balance = 10
slots = slots()

window = tk.Tk()
window.title("Casino")

def spin():
    global Balance
    Balance = Balance - 1
    balLabel.config(text = "Balance: £" + str(Balance))

    num = slots.spin()
    spinLabel.config(text = slots.toEmojies(num))
    resultLabel.config(text = "Winnings: £" + str(slots.getWinnings(num)))

balLabel = tk.Label(window, text = "Balance: £" + str(Balance))
balLabel.grid(row = 0, column = 0)

spinLabel = tk.Label(window, text = "Welcome to the casino!", font=("Arial", 20))
spinLabel.grid(row = 1, column = 0)

resultLabel = tk.Label(window, text = "hit spin to begin")
resultLabel.grid(row = 2, column = 0)

spinButton = tk.Button(window, text = "SPIN", width=50, command = spin)
spinButton.grid(row = 3, column = 0, pady = 5, padx = 5)

options = tk.Label(window, text = """\U0001F355 \U0001F355 \U0001F355: £1.5
\U0001F354 \U0001F354 \U0001F354: £10
\U0001F32E \U0001F32E \U0001F32E: £40
\U0001F32F \U0001F32F \U0001F32F: £160
\U0001F363 \U0001F363 \U0001F363: £1000
""", font=("Arial", 20))
options.grid(row = 0, column = 1, rowspan = 3)

window.mainloop()
