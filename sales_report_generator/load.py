import json
import numpy as np
import pandas as pd


def read_xlsx(file_):
    """ read excel to dataframe and replace all empty values to NaN """
    dataframe = pd.read_excel(io=file_, engine='openpyxl', dtype=str)
    dataframe = dataframe.replace(r'^\s*$', np.nan, regex=True)
    dataframe = dataframe.set_index(dataframe.columns[0])  # 1st column --> index
    return dataframe


def save_vars(**entry_variables):
    with open("variables.json", "w") as file:
        json.dump(entry_variables, file, indent=2, ensure_ascii=False)


def load_vars():
    with open("variables.json", "r") as file:
        data = json.load(file)
        return data
