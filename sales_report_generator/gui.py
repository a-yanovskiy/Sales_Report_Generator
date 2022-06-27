import tkinter as tk
from tkinter import filedialog
import pyperclip
import report_generator as report


def make_report():
    file_path = filedialog.askopenfilename()
    df = report.read_xlsx(file_path)
    text = report.generate_report(df)
    pyperclip.copy(text)


def gui():
    window = tk.Tk()
    window.geometry('310x250')
    window.title("Sales Report Maker")

    # DELETE_WORD_IN_DISH_NAME
    del_word_lbl = tk.Label(window, text="Delete this word from dish name")
    del_word_lbl.grid(column=0, row=0)
    del_word_smile = tk.Entry(window, width=20) 
    del_word_smile.grid(column=1, row=0)

    # empty label
    empty_lbl = tk.Label(window, text="")
    empty_lbl.grid(column=0, row=2)

    # smiles
    ## DISH_SMILE
    dish_lbl = tk.Label(window, text="Dish Smile")
    dish_lbl.grid(column=0, row=3)
    dish_smile = tk.Entry(window, width=15)
    dish_smile.insert(0, '\U0001F34B') 
    dish_smile.grid(column=1, row=3)

    ## LEADERS_SMILE
    leaders_lbl = tk.Label(window, text="Leaders Smile")
    leaders_lbl.grid(column=0, row=4)
    leaders_smile = tk.Entry(window, width=15)
    leaders_smile.insert(0, '\U00002734') 
    leaders_smile.grid(column=1, row=4)

    ## GROWS_SMILE
    grows_lbl = tk.Label(window, text="Grows Smile")
    grows_lbl.grid(column=0, row=5)
    grows_smile = tk.Entry(window, width=15) 
    grows_smile.insert(0, '\U00002714') 
    grows_smile.grid(column=1, row=5)

    ## FALLS_SMILE
    falls_lbl = tk.Label(window, text="Falls Smile")
    falls_lbl.grid(column=0, row=6)
    falls_smile = tk.Entry(window, width=15) 
    falls_smile.insert(0, '\U0000274C') 
    falls_smile.grid(column=1, row=6)

    # empty label
    empty_lbl = tk.Label(window, text="")
    empty_lbl.grid(column=0, row=7)

    # button
    btn = tk.Button(window, text="Choose file", command=make_report)
    btn.grid(column=0, row=8)

    # lbl = tk.Label(window, text="", fg='#913831')  # empty label
    # lbl.grid(column=0, row=10)
    # lbl.config(text="RESULT COPIED TO CLIPBOARD")

    tk.messagebox.showinfo("Info", "Result copied to clipboard!")

    window.mainloop()


gui()