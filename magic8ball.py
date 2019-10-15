from tkinter import *


def magic_ball():
    random_choices = ["Maybe...", "Jeremiah hacked into this program", "Absolutely.", "Ask me agane later... me tired",
                      "Hmm i dont know...", "Yes", "No.", "Jeremiah was here :)", "Cannot predict now sorry...",
                      "too much questions stop", "it is certain!", "you know what, maybe im not fit for this job",
                      "ok im going to sleep, ask someone else", "now's not a good time to ask sorry",
                      "I asked chase and he said nah", "my boolean instincts say yes"]
    ask_get = Entry.get(first_entry)
    import random
    justin = random.choices(random_choices)
    if "?" in ask_get:
        magic_response.set(justin)
    else:
        magic_response.set("Please put a question.")


root = Tk()

photo = PhotoImage(file=
                   'C:\\Users\\justin.nguyen\\PycharmProjects\\HelloWorld\\justin_nguyen_projects\\'
                   'game-magic-8-ball-no-text.png'
                   )
label = Label(root, image=photo, width=300, height=300)
label.grid(row=1, column=1)
root["bg"] = "white"
root.geometry('400x200')
root.title("Magic 8 Ball")
first_label = Label(root, text="Your question: ", bg="white", fg="black")
ask_button = Button(root, text="Ask", command=magic_ball, bg="black", fg="white")
ball_answer = Label(root, text="Magic 8 Ball says: ", bg="white", fg="black")
magic_response = StringVar()
magic_response.set('')
box_answer = Label(root, textvariable=magic_response, bg="white", fg="black")
first_entry = Entry(root)
first_label.grid(row=2, column=1, sticky=W)
first_entry.grid(row=2, column=2, sticky=W)
ask_button.grid(row=3, column=2, sticky=W)
ball_answer.grid(row=4, column=1, sticky=W)
box_answer.grid(row=4, column=2, sticky=W)
root.mainloop()
