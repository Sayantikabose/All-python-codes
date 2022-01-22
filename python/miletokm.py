from tkinter import *

def miles_to_km():
    miles=miles_input.get()
    km=float(miles)*1.609
    km_results_label.config(text=f"{km}")

window=Tk()
window.title("Miles to Km convertor")
window.config(padx=10,pady=10)
window.minsize(width=300,height=100)

miles_input=Entry()
miles_input.grid(column=1,row=0)

miles_label=Label(text="miles")
miles_label.grid(column=2,row=0)

is_equal_label=Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

km_results_label=Label(text="0")
km_results_label.grid(column=1,row=1)

km_label=Label(text="km")
km_label.grid(column=2,row=1)

button=Button(text="Calculate", command=miles_to_km)
button.grid(column=1,row=2)
















window.mainloop()
