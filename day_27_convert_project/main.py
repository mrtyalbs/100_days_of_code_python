from tkinter import *

def miles_to_km_converter():
    miles = float(miles_input.get())
    km = miles * 1.609344
    km_result_label.config(text=f"{km}")

window = Tk()
window.config(height=400, width=400)
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

miles_input = Entry(width=8)
miles_input.grid(column=2, row=2)
miles = miles_input.get()

miles_label = Label(text="Miles")
miles_label.config(padx=5, pady=5)
miles_label.grid(column=3, row=2)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=1, row=3)

km_label = Label(text="Km")
km_label.config(padx=5, pady=5)
km_label.grid(column=3, row=3)

km_result_label = Label(text="0")
km_result_label.grid(column=2, row=3)

convert_button = Button(text="Convert", command=miles_to_km_converter)
convert_button.grid(column=2, row=4)







window.mainloop()