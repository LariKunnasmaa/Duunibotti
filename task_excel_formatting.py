import pandas as pd
from duunitori.pickle_helper import load, pickle_save
from duunitori.class_job import Job
from duunitori.class_excel import df_to_excel, colour_excel, read_excel_sheet, auto_adjust_column_width, move_column_to_last

def small_data_cleaning(df:pd.DataFrame):
    df = df.sort_values(by='remote', ascending=False)
    df["checked"] = ""
    df = df.drop(["text", "model"], axis=1)
    return df

from openpyxl import Workbook
from openpyxl.styles import Font

def add_hyperlink(ws, cell_address, url, display_text, color="0000FF", underline=True):
    """
    Add a clickable hyperlink with custom text to an openpyxl worksheet.

    Args:
        ws (openpyxl.worksheet.worksheet.Worksheet): The worksheet.
        cell_address (str): Cell reference (e.g., "A1").
        url (str): The hyperlink URL.
        display_text (str): Text to display in the cell.
        color (str, optional): Hex color for the link text. Defaults to "0000FF" (blue).
        underline (bool, optional): Whether to underline the text. Defaults to True.
    """
    cell = ws[cell_address]
    cell.value = display_text
    cell.hyperlink = url
    cell.font = Font(color=color, underline="single" if underline else None)


def excel_formatting(jobs_list:list[Job], path = "jobs.xlsx"):
    """Formats the excel by calling functions to format the excel  """
    df = pd.DataFrame([vars(a) for a in jobs_list])
    df[["Käsitelty"]] = ""
    df =  move_column_to_last(df, "text")
    df =  move_column_to_last(df, "link")

    df = colour_excel(df) 

    path = df_to_excel(df)

    wb = read_excel_sheet(path)
    ws = wb["Sheet1"]
    ws = auto_adjust_column_width(ws, skip_columns=["text"])
    for ind in ws.iter_rows(min_row=2): 
        add_hyperlink(ws, ind[0].coordinate, ind[-1].value, ind[0].value) 
    wb.save(path)
    print("k")



if __name__ == '__main__':
    jobs_list = load()
    excel_formatting(jobs_list )
