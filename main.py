import tkinter as tk

def button_pressed():
    tokm= float(input.get()) *  1.609
    converted_label["text"] = str(tokm)
    
window = tk.Tk()
window.title("Miles to Kilometer converter")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)
#create the GUI


input = tk.Entry(width=10)
input.grid(column=1,row=0)

miles_label = tk.Label(text="miles")
miles_label.grid(column=2,row=0)

equal_to_label = tk.Label(text="is equalt to")

km_label=tk.Label(text="km")
km_label.grid(column=2, row=1)




#first 
converted_label = tk.Label(text="0",font=20)
converted_label.grid(column=1, row=1)

button = tk.Button(text="button",command=button_pressed)
button.grid(column= 1, row = 2)














#stops the GUI from closing 
tk.mainloop()


















