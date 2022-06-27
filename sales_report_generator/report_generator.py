import re
import numpy as np
import pandas as pd
import format_report as format

DISH_SMILE = '\U0001F34B'
LEADERS_SMILE = '\U00002734'
GROWS_SMILE = '\U00002714'
FALLS_SMILE = '\U0000274C'
DELETE_WORD_IN_DISH = ' Свежов'


def read_xlsx(file_):
    """ read excel to dataframe and replace all empty values to NaN """
    dataframe = pd.read_excel(io=file_, engine='openpyxl', dtype=str)
    dataframe = dataframe.replace(r'^\s*$', np.nan, regex=True)
    dataframe = dataframe.set_index(dataframe.columns[0])  # 1st column --> index
    return dataframe


def generate_report(dataframe, result='', dish=''):
    df_first_column = dataframe.iloc[:, 0:1]
    df_second_column = dataframe.iloc[:, 1:2]
    
    if df_first_column.empty:
        return result
    else:
        dish = re.split('[0-9]', df_first_column.columns[0])[0].strip()
        
        result += '\n' + DISH_SMILE + ' *_' + dish + '_*'

        if not df_second_column.empty:
            if re.match(r'^Unnamed', df_second_column.columns[0]):
                df_rest_columns = dataframe.iloc[:, 2:]
                comparing = format.df_to_dict(df_second_column)

                grows_sales = format.sort_and_filter_dict_by_items(
                    comparing, 'positive')
                result += '\n' + GROWS_SMILE + ' _Прирост:_ ' + format.format_dict(grows_sales)

                falls_sales = format.sort_and_filter_dict_by_items(
                    comparing, 'negative')
                result += '\n' + FALLS_SMILE + ' _Падение:_ ' + format.format_dict(falls_sales)

            else:
                df_rest_columns = dataframe.iloc[:, 1:]
        else:
            df_rest_columns = dataframe.iloc[:, 1:]
        
        f = format.df_to_dict(df_first_column)
        sorted_ = format.sort_and_filter_dict_by_items(f)
        sales_leaders = format.format_dict(sorted_, DELETE_WORD_IN_DISH)
        
        result += '\n' + LEADERS_SMILE + ' _ЛИДЕРЫ ПРОДАЖ:_ ' + sales_leaders + '\n'

        return generate_report(df_rest_columns, result, dish)


# path1 = 'd:\Downloads\Акция неделька (2).xlsx'
# path2 = 'd:\Downloads\Отчет Акция за прошлую неделю.xlsx'

# # file1 = read_xlsx(path1)
# # print(generate_report(file1))

# file2 = read_xlsx(path2)
# print(generate_report(file2))
