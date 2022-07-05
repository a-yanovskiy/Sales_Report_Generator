import threading
import tkinter as tk
from tkinter import filedialog
import pyperclip
import sales_report_generator.load as load
from sales_report_generator.report_generator import generate_report


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
    df = load.read_xlsx(file_path)

    dish_del_text = get_del_entry()
    entry_add_list = get_add_entry()

    dish_add_text, leaders_add_text, grows_add_text, falls_add_text = \
        entry_add_list

    load.save_vars(DELETED_TEXT=dish_del_text,
                   DISH_TEXT=dish_add_text,
                   LEADERS_TEXT=leaders_add_text,
                   GROWS_TEXT=grows_add_text,
                   FALLS_TEXT=falls_add_text)

    text = generate_report(df,
                           result,
                           dish_add_text,
                           leaders_add_text,
                           grows_add_text,
                           falls_add_text,
                           dish_del_text)
    pyperclip.copy(text)
    tk.messagebox.showinfo("Info", "Result copied to clipboard!")


def element(frame, label='', insert_var=''):
    lbl = tk.Label(frame, text=label)
    lbl.pack()
    entry = tk.Entry(frame, width=40)
    entry.pack()
    entry.insert(0, insert_var)
    return entry


# GUI
window = tk.Tk()
window.geometry('300x300')
window.title("Sales Report Maker")


# load saved variables
variables = load.load_vars()
DELETED_TEXT = variables['DELETED_TEXT']
DISH_TEXT = variables['DISH_TEXT']
LEADERS_TEXT = variables['LEADERS_TEXT']
GROWS_TEXT = variables['GROWS_TEXT']
FALLS_TEXT = variables['FALLS_TEXT']

# add elements
del_word_entry = element(window,
                         "This text will be deleted from dish name:",
                         DELETED_TEXT)

# entry frame
tk.Frame(window)
entry_frame = tk.LabelFrame(text='This text will be added:')

dish_entry = element(entry_frame, "Dish text", DISH_TEXT)
leaders_entry = element(entry_frame, "Leaders text", LEADERS_TEXT)
grows_entry = element(entry_frame, "Grows text", GROWS_TEXT)
falls_entry = element(entry_frame, "Falls text", FALLS_TEXT)

entry_frame.pack()

    empty_lbl = tk.Label(window, text="")
    empty_lbl.pack()

    # button
    report_btn = tk.Button(window,
                           text="Choose file to make report",
                           command=lambda: threading.Thread(target=make_report,
                                                            args=(del_word_entry,
                                                                  dish_entry,
                                                                  leaders_entry,
                                                                  grows_entry,
                                                                  falls_entry)).start())

    report_btn.pack()

window.mainloop()
