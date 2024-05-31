import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    final_number = " "
    for i in range (6):
        lottery = random.randint(1, 100)
        final_number += str(lottery)+ " "
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(title = "lottery ticket", message = final_number)
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
