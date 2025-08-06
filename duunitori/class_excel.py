import pandas as pd
from duunitori.pickle_helper import load, pickle_save
from duunitori.class_job import Job

def style_if_column_false(column_name):
    def _style(row):
        for _ in row:
            return ['background-color: red' if row[column_name] == False else
                    ['background-color: #0a25f2' if row.name % 2 else 'background-color: #0a25f2'][0] for _ in row]
    return _style

def combine_styles(row):
    red_style = style_if_column_false('remote')(row)
    return red_style

def df_to_excel(df:pd.DataFrame, path = "Jobs.xlsx"):
    df.to_excel(path, index=False)

def colour_excel(df:pd.DataFrame):
    styled_df = df.style.apply(combine_styles, axis=1)
    return styled_df



