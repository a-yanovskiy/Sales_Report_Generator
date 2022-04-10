import pandas as pd
import numpy as np
import re


def read_xlsx(file_):
    """ read excel to dataframe and replace all empty values to NaN """
    dataframe = pd.read_excel(io=file_, engine='openpyxl', dtype=str)
    dataframe = dataframe.replace(r'^\s*$', np.nan, regex=True)
    dataframe = dataframe.set_index(dataframe.columns[0])  # 1st column --> index
    return dataframe


def sort_and_filter_dict_by_items(dictionary, filter='positive') -> dict:
    """ sort dict by float values """
    dict_ = {}
    for i, k in dictionary.items():
        if not pd.isnull(k):
            k = int(k) if k.count('.')==0 else float(k)
            if filter == 'positive':
                if k < 0:
                    continue
            elif filter == 'negative':
                if k >= 0:
                    continue
                else:
                    k = abs(k)
            dict_[i] = k

    series = pd.Series(dict_)
    series.sort_values(
        axis=0, 
        ascending=False, 
        inplace=True, 
        kind='quicksort', 
        na_position='last', 
        ignore_index=False, 
        key=None,
    )
    return series.to_dict()


def format_dict(dict) -> str:
    result = ''
    for market, value in dict.items() :
        market = re.split(' ИП', market)[0]
        if value == value:
                meter = 'кг'
                if re.match(r'^-?\d+(?:\.\d+)$', str(value)) is None:
                    meter = 'шт'
                    value = int(value)
                else:
                    value = round(float(value), 2)
        else:
            continue
        result += market + ': ' + str(value) + ' ' + meter + '; '
    return result


def df_to_dict(df_series, result={}) -> dict:
    df_series = df_series[df_series.index.notnull()]
    item = df_series.iloc[0:1]
    rest_items = df_series.iloc[1:]
    if item.empty:
        return result
    else:
        index = item.index[0]
        value = item.values[0][0]
        result[index] = value
        return df_to_dict(rest_items, result)


def generate_report(dataframe, result='', dish=''):
    df_first_column = dataframe.iloc[:, 0:1]
    df_second_column = dataframe.iloc[:, 1:2]
    
    if df_first_column.empty:
        return result
    else:
        dish = re.split('[0-9]', df_first_column.columns[0])[0].strip()
        
        result += '\n \U0001F34B *_' + dish + '_*'

        if not df_second_column.empty:
            if re.match(r'^Unnamed', df_second_column.columns[0]):
                df_rest_columns = dataframe.iloc[:, 2:]
                comparing = df_to_dict(df_second_column)

                grows_sales = sort_and_filter_dict_by_items(comparing, 'positive')
                result += '\n \U00002714 _Прирост:_ ' + format_dict(grows_sales)

                falls_sales = sort_and_filter_dict_by_items(comparing, 'negative')
                result += '\n \U0000274C _Падение:_ ' + format_dict(falls_sales)

            else:
                df_rest_columns = dataframe.iloc[:, 1:]
        else:
            df_rest_columns = dataframe.iloc[:, 1:]
        
        f = df_to_dict(df_first_column)
        sorted_ = sort_and_filter_dict_by_items(f)
        sales_leaders = format_dict(sorted_)
        
        result += '\n \U00002734 _ЛИДЕРЫ ПРОДАЖ:_ ' + sales_leaders + '\n'

        return generate_report(df_rest_columns, result, dish)


# path1 = 'd:\Downloads\акции1.xlsx'
# path2 = 'd:\Downloads\новинки 08.04.22.xlsx'
# file = read_xlsx(path1)
# print(generate_report(file))
