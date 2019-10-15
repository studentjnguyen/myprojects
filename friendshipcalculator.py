from tkinter import *


def calculation():
    """
    Generates random number percentage when the button is pressed.
    Gets string from user input and allows the returned text to be formatted according to names and resulting percentage.
    """
    first_name = str(Entry.get(first_entry))
    second_name = str(Entry.get(second_entry))
    import random
    percentage = random.randint(1, 101)
    if percentage <= 25:
        friendship_result = Label(root, text="wow {} and {} are on bad terms :(".format(first_name, second_name), bg="white", fg="red")
        friendship_result.grid(row=5, column=2, sticky=W)
        friendship_calculation = Label(root, text=percentage, bg="white", fg="red")
        friendship_calculation.grid(row=4, column=2, sticky=W)
    elif 25 < percentage <= 50:
        friendship_result = Label(root, text="meh {} and {} are on okay terms :P".format(first_name, second_name), bg="white", fg="orange")
        friendship_result.grid(row=5, column=2, sticky=W)
        friendship_calculation = Label(root, text=percentage, bg="white", fg="orange")
        friendship_calculation.grid(row=4, column=2, sticky=W)
    elif 50 < percentage <= 75:
        friendship_result = Label(root, text="yay {} and {} are good friends :D".format(first_name, second_name), bg="white", fg="purple")
        friendship_result.grid(row=5, column=2, sticky=W)
        friendship_calculation = Label(root, text=percentage, bg="white", fg="purple")
        friendship_calculation.grid(row=4, column=2, sticky=W)
    elif 75 < percentage <= 100:
        friendship_result = Label(root, text="omg {} and {} are best friends pogchomp :O".format(first_name, second_name), bg="white", fg="green")
        friendship_result.grid(row=5, column=2, sticky=W)
        friendship_calculation = Label(root, text=percentage, bg="white", fg="green")
        friendship_calculation.grid(row=4, column=2, sticky=W)


"""
Basic geometry of the tkinter window including buttons and entry for user inputs.
"""
root = Tk()
root["bg"] = "white"
root.geometry('400x200')
root.title("Friendship Calculator")
first_label = Label(root, text="First Name: ", bg="white", fg="green")
second_label = Label(root, text="Second Name: ", bg="white", fg="green")
calculate_button = Button(root, text="Calculate", command=calculation, bg="green", fg="white")
friendship_answer = Label(root, text="Your percentage: ", bg="white", fg="green")
first_entry = Entry(root)
second_entry = Entry(root)
first_label.grid(row=1, column=1, sticky=W)
second_label.grid(row=2, column=1, sticky=W)
first_entry.grid(row=1, column=2, sticky=W)
second_entry.grid(row=2, column=2, sticky=W)
calculate_button.grid(row=3, column=2, sticky=W)
friendship_answer.grid(row=4, column=1, sticky=W)
root.mainloop()
