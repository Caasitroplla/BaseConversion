from tkinter import *
from convert import *

# Creating a window
window = Tk()

# Set size
window.geometry('300x200')

# Title the window
window.title('Base Convertor')

def convert():
	input_base = input_base_var.get()
	output_base = output_base_var.get()
	input_value = input_var.get()
	nomalised = normalise(input_value, int(input_base))
	output_var.set(str(de_normalise(int(nomalised), int(output_base))))
	output_box.config(text=output_var.get())



options = [
	'1','2','3','4','5','6','7','8','9','10',
	'11','12','13','14','15','16','17','18',
	'19','20','21','22','23','24','25','26',
	'27','28','29','30','31','32','33','34',
	'35'
]

# Datatype of menu text
input_base_var = StringVar()
output_base_var = StringVar()
input_var = StringVar()
output_var = StringVar()

# Initial menu text
input_base_var.set('10')
output_base_var.set('10')


# Input dropdown menu
input_base = OptionMenu(window, input_base_var, *options)

# Input dropdown menu label
input_base_label = Label(window, text='Input base')

# Ouput dropdown menu
output_base = OptionMenu(window, output_base_var, *options)

# Output dropdown menu label
output_base_label = Label(window, text='Output base')

# Create button, it will change label text
button = Button(window, text='convert', command=convert)

# Create entry field
entry = Entry(window, textvariable=input_var)

# Input value box label
input_box_label = Label(window, text='Enter variable:')

# Output label
output_label = Label(window, text="Output value:")

# Output box
output_box = Label(window, text=output_var)


# Griding a whole lota shit
input_box_label.grid(row=0, column=0)
entry.grid(row=0, column=1)

input_base_label.grid(row=1, column=0)
input_base.grid(row=1, column=1)

output_base_label.grid(row=2, column=0)
output_base.grid(row=2, column=1)

button.grid(row=3, column=1)

output_label.grid(row=4, column=0)
output_box.grid(row=4, column=1)

# Show the window
window.mainloop()



