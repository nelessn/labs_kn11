import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
window = tk.Tk()

textwnd = tk.Label(text="що ви хочете зашифрувати?")
entry = tk.Entry()
textwnd2 = tk.Label(text="який ключ?")
entry2 = tk.Entry()

textwnd.pack()
entry.pack()
textwnd2.pack()
entry2.pack()



def myclick(word, key):
    word = str(word).replace(" ", "")
    chars = dict()
    result = ""

    messagebox.showinfo(title="Результат", message="Зашифрований текст: " + result)

btn = tk.Button(
    text="enter",
    command=lambda: myclick(entry.get(), int(entry2.get())),
    width=6,
    height=1,
    bg="black",
    fg="white")
    
btn.pack()
window.mainloop()


