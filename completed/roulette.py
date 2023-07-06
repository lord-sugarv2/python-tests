import tkinter as tk
import random

CanUse = True
Balance = 1000

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

    def CreateButton(self, text, command, w=25, row=-20, column=1, col="#5F616D"):
        if row == -20: row = self.row
        button = tk.Button(window, text = text, command=command, width=w)
        button.configure(bg=col, fg="white")
        button.grid(pady = 1, padx = 5, row=row, column=column)
        self.row = self.row + 1
        return button

    def CreateTextEntry(self, text, w=25, row=20, column=1):
        if row == -20: row = self.row
        button = tk.Entry(window, text = text, width=w)
        button.configure(bg="#5F616D", fg="white")
        button.grid(pady = 1, padx = 5, row=row, column=column)
        self.row = self.row + 1
        return button

    def CreateLabel(self, text, row=-20, column=1):
        if row == -20: row = self.row
        label = tk.Label(window, text=text)
        label.configure(bg="#343541", fg="White")
        label.grid(pady = 1, padx = 5, row=row, column=column)
        self.row = self.row + 1
        return label
    
vgui = vgui()
window = vgui.CreateFrame("")

counter, column, row = 0, 0, 0
buttons = []
for i in range(1, 100):
    but = vgui.CreateButton(i, lambda: print(i), 6, row, column, i%2 == 0 and "#FF002F" or "#242424")
    buttons.append(but)
    if counter == 2: row = row + 1; counter = -1
    counter = counter + 1
    column = column + 1
    if column == 3: column = 0

oldnum = 1
def Spin(value=0):
    global oldnum
    errorText.configure(text="")
    if value == 50:
        global CanUse
        global Balance
        CanUse = True
        if (oldnum + 1) % 2 == 0 and selectedCol == "Red":
            Balance = Balance + (int(inputLabel.get()) * 2)
            errorText.configure(text = "+ " + str((int(inputLabel.get()) * 2)))
            balanceLabel.configure(text="Balance: £" + str(Balance))
        if (oldnum + 1) % 2 != 0 and selectedCol == "Black":
            Balance = Balance + (int(inputLabel.get()) * 2)
            errorText.configure(text = "+ " + str((int(inputLabel.get()) * 2)))
            balanceLabel.configure(text="Balance: £" + str(Balance))
        return

    newnum = random.randint(1, 98)
    buttons[oldnum].configure(bg=(oldnum + 1)%(2) == 0 and "#FF002F" or "#242424", fg="white")
    buttons[newnum].configure(bg="#00FF44", fg="white")
    oldnum = newnum
    window.after(20, lambda: Spin(value + 1))

balanceLabel = vgui.CreateLabel("Balance: £" + str(Balance), 1, 3)

def StartSpin():
    global CanUse
    global Balance
    if not CanUse: return
    CanUse = False
    enteredText = inputLabel.get()
    if not enteredText.isdigit():
        errorText.configure(text="Please set the text to numbers")
        return
    if selectedCol == 0:
        errorText.configure(text="Please select a color")
        return
    if Balance-int(enteredText) < 0:
        errorText.configure(text="Insufficient funds")
        return

    Balance = Balance-int(enteredText)
    balanceLabel.configure(text="Balance: £" + str(Balance))
    Spin()

SpinButton = vgui.CreateButton("SPIN", StartSpin, 15, 2, 3)

selectedCol = 0
def SelectCol(col):
    global selectedCol
    selectedCol = col
    if col == "Red":
        RedButton.configure(bg="#00FF44", fg="black")
        BlackButton.configure(bg="#242424", fg="white")
    else:
        RedButton.configure(bg="#FF002F", fg="white")
        BlackButton.configure(bg="#00FF44", fg="black")

label = vgui.CreateLabel("Enter Amount\n+ Click color", 4, 3)
inputLabel = vgui.CreateTextEntry("SPIN", 15, 5, 3)
RedButton = vgui.CreateButton("RED", lambda: SelectCol("Red"), 15, 6, 3, "#FF002F")
BlackButton = vgui.CreateButton("Black", lambda: SelectCol("Black"), 15, 7, 3, "#242424")

errorText = vgui.CreateLabel("", 9, 3)

vgui.Finalize(window)
