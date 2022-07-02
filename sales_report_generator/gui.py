import tkinter as tk
from tkinter import filedialog
import pyperclip

from format_report import read_xlsx
from report_generator import generate_report


def get_add_entry():
    dish = dish_entry.get()
    leaders = leaders_entry.get()
    grows = grows_entry.get()
    falls = falls_entry.get()
    return dish, leaders, grows, falls


def get_del_entry():
    deleted_text = del_word_entry.get()
    return deleted_text


def make_report():
    file_path = filedialog.askopenfilename()
    result = ''
    df = read_xlsx(file_path)
    dish_del_text = get_del_entry()
    entry_add_list = map(lambda x: x if x == '' else x + ': ', get_add_entry())
    dish_add_text, leaders_add_text, grows_add_text, falls_add_text = entry_add_list
    text = generate_report(df,
                           result,
                           dish_add_text,
                           leaders_add_text,
                           grows_add_text,
                           falls_add_text,
                           dish_del_text)
    pyperclip.copy(text)
    tk.messagebox.showinfo("Info", "Result copied to clipboard!")


def element(frame, label=''):
    lbl = tk.Label(frame, text=label)
    lbl.pack()
    entry = tk.Entry(frame, width=40)
    entry.pack()
    return entry


# GUI
window = tk.Tk()
window.geometry('300x300')
window.title("Sales Report Maker")

del_word_entry = element(window, "This text will be deleted from dish name:")

# entry frame
tk.Frame(window)
entry_frame = tk.LabelFrame(text='This text will be added:')

dish_entry = element(entry_frame, "Dish text")
leaders_entry = element(entry_frame, "Leaders text")
grows_entry = element(entry_frame, "Grows text")
falls_entry = element(entry_frame, "Falls text")

entry_frame.pack()

# button
empty_lbl = tk.Label(window, text="")
empty_lbl.pack()
report_btn = tk.Button(window,
                       text="Choose file to make report_generator",
                       command=lambda: [get_add_entry(),
                                        get_del_entry(),
                                        make_report()])
report_btn.pack()

window.mainloop()
