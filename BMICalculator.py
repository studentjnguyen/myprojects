from tkinter import *


def calculation():
    if weight_entry is not float or height_entry is not float:
        bmi_error = Label(root, text="ERROR JEREMIAH", bg="black", fg="white")
        bmi_error.grid(row=5, column=2, sticky=W)
    w = float(Entry.get(weight_entry))
    h = float(Entry.get(height_entry))
    bmi_formula = w / (h ** 2)
    bmi_formula = round(bmi_formula, 4)
    bmi_calculation = Label(root, text=bmi_formula, bg="black", fg="white")
    bmi_calculation.grid(row=4, column=2, sticky=W)
    while True:
        if bmi_formula <= 18.5:
            bmi_result = Label(root, text="You are underweight! Eat and Exercise more!", bg="black", fg="white")
            bmi_result.grid(row=5, column=2, sticky=W)
            break
        elif 18.5 < bmi_formula < 24.9:
            bmi_result = Label(root, text="You are normal. Stay cool", bg="black", fg="white")
            bmi_result.grid(row=5, column=2, sticky=W)
            break
        elif 25 < bmi_formula < 29.9:
            bmi_result = Label(root, text="You are overweight. Exercise more!", bg="black", fg="white")
            bmi_result.grid(row=5, column=2, sticky=W)
            break
        elif bmi_formula > 30:
            bmi_result = Label(root, text="You are obese. Please see a doctor.", bg="black", fg="white")
            bmi_result.grid(row=5, column=2, sticky=W)
            break
        else:
            bmi_result = Label(root, text="ERROR JEREMIAH", bg="black", fg="white")
            bmi_result.grid(row=5, column=2, sticky=W)
            continue


root = Tk()
root["bg"] = "black"
root.geometry('400x200')
root.title("BMI Calculator")
weight_label = Label(root, text="Kilograms: ", bg="black", fg="white")
height_label = Label(root, text="Meters: ", bg="black", fg="white")
calculate_button = Button(root, text="Calculate", command=calculation, bg="grey", fg="white")
bmi_answer = Label(root, text="Your BMI: ", bg="black", fg="white")
weight_entry = Entry(root)
height_entry = Entry(root)
weight_label.grid(row=1, column=1, sticky=W)
height_label.grid(row=2, column=1, sticky=W)
weight_entry.grid(row=1, column=2, sticky=W)
height_entry.grid(row=2, column=2, sticky=W)
calculate_button.grid(row=3, column=2, sticky=W)
bmi_answer.grid(row=4, column=1, sticky=W)
root.mainloop()
