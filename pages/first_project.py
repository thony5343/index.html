from tkinter import *

def inches_to_cm():
    inches = float(inches_input.get())
    cm = inches * 2.54
    centimeter_result_label.config(text=f"{cm}")

window = Tk()
window.title("Inches to Centimeter Converter")
window.config(padx=100, pady=100)

inches_input = Entry(width=10)
inches_input.grid(column=1, row=0)

inches_input_label = Label(text="inche(s)")
inches_input_label.grid(column=2, row=0)


is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

centimeter_result_label = Label(text="0")
centimeter_result_label.grid(column=1, row=1)

centimeter_label = Label(text="cm")
centimeter_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=inches_to_cm)
calculate_button.grid(column=2, row=2)


window.mainloop()
