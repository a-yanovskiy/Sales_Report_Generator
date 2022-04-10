from tkinter import *
from tkinter import filedialog as fd
import tkinter
import pyperclip
import sales_report_engine


def make_report():
    file_path = fd.askopenfilename()
    df = sales_report_engine.read_xlsx(file_path)
    text = sales_report_engine.generate_report(df)
    pyperclip.copy(text)


def gui():
    window = Tk()
    window.title("Sales report by markets")
    # lbl = Label(window, text="", fg='#913831')  # empty label
    # lbl.grid(column=0, row=2)

    btn = Button(window, text="Choose file", command=make_report)
    btn.grid(column=0, row=0)
    # lbl.config(text="RESULT COPIED TO CLIPBOARD")
    
    tkinter.messagebox.showinfo("Info", "Result copied to clipboard!")

    window.mainloop()
