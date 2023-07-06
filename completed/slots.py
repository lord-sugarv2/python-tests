import tkinter as tk
import random

CanUse = True
Balance = 10
Emojies = [
    ["\U0001F355"], # cherry
    ["\U0001F354"], # barbarbar
    ["\U0001F32E"], # barbar
    ["\U0001F32F"], # bar
    ["\U0001F363"], # 7
]

class vgui:
    def __init__(self):
        self.row = 0

    def CreateFrame(self, title):
        frame = tk.Tk()
        frame.title("Casino")
        frame.configure(bg="#343541")
        return frame

    def Finalize(self, window):
        window.mainloop()

    def CreateButton(self, text, command, w=25, row=-20, column=1):
        if row == -20: row = self.row
        button = tk.Button(window, text = text, command=command, width=w)
        button.configure(bg="#5F616D", fg="white")
        button.grid(pady = 5, padx = 5, row=row, column=column)
        self.row = self.row + 1
        return button

    def CreateLabel(self, text, row=-20, column=1):
        if row == -20: row = self.row
        label = tk.Label(window, text=text)
        label.configure(bg="#343541", fg="White")
        label.grid(pady = 5, padx = 5, row=self.row, column=column)
        self.row = self.row + 1
        return label

class slots:
    def Spin(self):
        length = len(Emojies) - 1
        return [random.randint(0, length), random.randint(0, length), random.randint(0, length)]

    def ToEmojies(self, value):
        val = "[ "
        for num in value:
            val = val + Emojies[num][0] + " "
        val = val + "]"
        return val

    def GetWinnings(self, array):
        count = 0
        for number in array:
            if number == 0: count = count + 1
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

def DoSpin(value, array=[]):
    if value == 10:
        global CanUse
        CanUse = True
        if slots.GetWinnings(array) == 0: return
        global Balance
        Balance = Balance + slots.GetWinnings(array)
        balanceLabel.configure(text = "Balance: £" + str(Balance) + ": (+" + str(slots.GetWinnings(array)) + ")")
        return

    value = value + 1
    spinResult = slots.Spin()
    emojiLabel.configure(text = slots.ToEmojies(spinResult))
    window.after(20, lambda: DoSpin(value, spinResult))

def SpinClicked():
    if not CanUse: return
    global Balance
    if Balance - 1 < 0:
        balanceLabel.configure(text = "BANKRUPT")
        return

    Balance = Balance - 1
    balanceLabel.configure(text = "Balance: £" + str(Balance) + ": (-1)")
    DoSpin(0)

slots = slots()
vgui = vgui()
window = vgui.CreateFrame("")
balanceLabel = vgui.CreateLabel("Balance: £" + str(Balance))

emojiLabel = vgui.CreateLabel("[ ## ## ## ]")
emojiLabel.configure(font=("Arial", 20))

button = vgui.CreateButton("SPIN", SpinClicked)

vgui.Finalize(window)
