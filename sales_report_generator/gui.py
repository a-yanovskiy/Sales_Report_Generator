import threading
import tkinter as tk
from tkinter import filedialog
import pyperclip
import sales_report_generator.load as load
from sales_report_generator.report_generator import generate_report


def make_report(del_word_entry,
                dish_entry,
                leaders_entry,
                grows_entry,
                falls_entry):

    file_path = filedialog.askopenfilename()
    df = load.read_xlsx(file_path)

    dish_del_text = del_word_entry.get()
    dish_add_text = dish_entry.get()
    leaders_add_text = leaders_entry.get()
    grows_add_text = grows_entry.get()
    falls_add_text = falls_entry.get()

    load.save_vars(deleted_text=dish_del_text,
                   dish_text=dish_add_text,
                   leaders_text=leaders_add_text,
                   grows_text=grows_add_text,
                   falls_text=falls_add_text)

    result = ''
    text = generate_report(df,
                           result,
                           dish_add_text,
                           leaders_add_text,
                           grows_add_text,
                           falls_add_text,
                           dish_del_text)
    pyperclip.copy(text)
    return tk.messagebox.showinfo("Info", "Result copied to clipboard!")


def element(frame, label='', insert_var=''):
    lbl = tk.Label(frame, text=label)
    lbl.pack()
    entry = tk.Entry(frame, width=40)
    entry.pack()
    entry.insert(0, insert_var)
    return entry


def gui():
    # GUI
    window = tk.Tk()
    window.geometry('300x300')
    window.title("Sales Report Maker")

    # load saved variables
    variables = load.load_vars()

    deleted_text = variables['deleted_text']
    dish_text = variables['dish_text']
    leaders_text = variables['leaders_text']
    grows_text = variables['grows_text']
    falls_text = variables['falls_text']

    # add elements
    del_word_entry = element(window,
                             "This text will be deleted from dish name:",
                             deleted_text)

    # entry frame
    tk.Frame(window)
    entry_frame = tk.LabelFrame(text='This text will be added:')

    dish_entry = element(entry_frame, "Dish text", dish_text)
    leaders_entry = element(entry_frame, "Leaders text", leaders_text)
    grows_entry = element(entry_frame, "Grows text", grows_text)
    falls_entry = element(entry_frame, "Falls text", falls_text)

    entry_frame.pack()

    empty_lbl = tk.Label(window, text="")
    empty_lbl.pack()

    # button
    button = tk.Button(window,
                       text="Choose file to make report",
                       command=lambda: threading.Thread(target=make_report,
                                                        args=(del_word_entry,
                                                              dish_entry,
                                                              leaders_entry,
                                                              grows_entry,
                                                              falls_entry)
                                                        ).start())

    button.pack()

    return window
