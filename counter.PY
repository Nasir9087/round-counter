import tkinter as tk

def increment():
    global count
    count += 1
    label.config(text=str(count))

def decrement():
    global count
    count -= 1
    label.config(text=str(count))

def reset():
    global count
    count = 0
    label.config(text=str(count))

count = 0

root = tk.Tk()
root.title("Counter")

label = tk.Label(root, text=str(count), font=("Arial", 48))
label.pack(pady=20)

frame = tk.Frame(root)
frame.pack()

btn_decrement = tk.Button(frame, text="-", font=("Arial", 24), command=decrement, width=5)
btn_decrement.pack(side="left", padx=5)

btn_reset = tk.Button(frame, text="Reset", font=("Arial", 24), command=reset, width=7)
btn_reset.pack(side="left", padx=5)

btn_increment = tk.Button(frame, text="+", font=("Arial", 24), command=increment, width=5)
btn_increment.pack(side="left", padx=5)

root.mainloop()
