import tkinter


def button1_clicked():
    miles = int(entry1.get())
    km = miles * 1.6
    value_label.config(text=f"{km:0.2f}")


window = tkinter.Tk()
window.title("Miles to Km converter")
window.minsize(200, 100)
window.config(padx=20, pady=20)

# Entry
entry1 = tkinter.Entry(width=10)
entry1.grid(row=0, column=1)

# label miles
miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

# label equal to
equal_label = tkinter.Label(text="is equal to")
equal_label.grid(row=1, column=0)

# label value
value_label = tkinter.Label(text="0")
value_label.grid(row=1, column=1)

# label km
km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

# Button
button1 = tkinter.Button(text="Calculate", command=button1_clicked)
button1.grid(row=2, column=1)

window.mainloop()
