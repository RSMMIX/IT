from tkinter import *
# from tkinter import ttk
from math import sqrt
# from tkinter import messagebox

# Triangle type checking function
def check_triangle_type(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "ป้อนข้อมูลไม่ถูกต้อง"
    elif a == b == c:
        return "Equilateral Triangle"
    elif a == b or a == c or b == c:
        if c != sqrt(a**2 + b**2):
            return "Isosceled Triangle"
        else:
            return "Right Triangle"
    else:
        if c != sqrt(a**2 + b**2):
            return "Scalene Triangle"
        else:
            return "Right Triangle"

# Function to check if input is valid
def validate_input(input_str):
    try:
        float_value = float(input_str)
        int_value = int(float_value)
        if float_value != int_value or '.' in input_str:
            raise ValueError
        if int_value < 1 or int_value > 101:
            raise ValueError
        return True
    except ValueError:
        return False

# Result display function
def show_result():
    a_valid = validate_input(side1_entry.get())
    b_valid = validate_input(side2_entry.get())
    c_valid = validate_input(side3_entry.get())

    if not (a_valid and b_valid and c_valid):
        messagebox.showerror("ข้อผิดพลาด", "ป้อนข้อมูลไม่ถูกต้อง")
        return

    a = float(side1_entry.get())
    b = float(side2_entry.get())
    c = float(side3_entry.get())
    triangle_type = check_triangle_type(a, b, c)
    result_entry.delete(0, END)
    if triangle_type == "ป้อนข้อมูลไม่ถูกต้อง":
        messagebox.showerror("ข้อผิดพลาด", "ป้อนข้อมูลไม่ถูกต้อง")
        return
    result_entry.insert(0, triangle_type)


# Set up window
window = Tk()
window.title("ตรวจสอบประเภทสามเหลี่ยม")
window.geometry("250x200")

# Create a frame
frame = Frame(window)
frame.pack()

# Create a message
myLabel = Label(frame, text="Enter the length of side", font=14)
myLabel.grid(row=0, column=0, columnspan=2)

label_side1 = Label(frame, text="Side 1")
label_side2 = Label(frame, text="Side 2")
label_side3 = Label(frame, text="Side 3")

myLabelRe = Label(frame, text="Result", font=14)
myLabelRe.grid(row=4, column=1, columnspan=2)

# Create an input box
side1_entry = Entry(frame, width=15, bg="#BDD861")
side2_entry = Entry(frame, width=15, bg="#BDD861")
side3_entry = Entry(frame, width=15, bg="#BDD861")

# Create a results box
result_entry = Entry(frame, width=15, bg="#BDD861")

# composition
label_side1.grid(row=1, column=0)
label_side2.grid(row=2, column=0)
label_side3.grid(row=3, column=0)

side1_entry.grid(row=1, column=1)
side2_entry.grid(row=2, column=1)
side3_entry.grid(row=3, column=1)
result_entry.grid(row=5, column=1)

# Add button
button_calculate = Button(frame, text="enter", bg="#BDD861", command=show_result)
button_calculate.grid(row=5,column=0)


# Start the program
window.mainloop()