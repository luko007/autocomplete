import tkinter as tk
from main import suggestWord

def callback(input, list_box):
    suggestions = suggestWord(input.get(), 8)
    list_box.delete(0, 'end')
    for i, suggestion in enumerate(suggestions):
        list_box.insert(i, suggestion)


root = tk.Tk()
root.geometry("600x400")
l1 = tk.Listbox(root)

input = tk.StringVar()
input.trace("w", lambda name, index, mode, input=input: callback(input, l1))

name_entry = tk.Entry(root, textvariable = input, font=('calibre',10,'normal'))

name_entry.pack()
l1.pack()

root.mainloop()


