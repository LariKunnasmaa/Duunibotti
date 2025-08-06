import pandas as pd
from duunitori.pickle_helper import load, pickle_save
from duunitori.class_job import Job
from duunitori.class_excel import df_to_excel, colour_excel

def small_data_cleaning(df:pd.DataFrame):
    df = df.sort_values(by='remote', ascending=False)
    df["checked"] = ""
    df = df.drop(["text", "model"], axis=1)
    return df


def excel_mani(jobs_list:list[Job]):
    df = pd.DataFrame([vars(a) for a in jobs_list])
    df = colour_excel(df)   
    df_to_excel(df)



if __name__ == '__main__':
    jobs_list = load()
    excel_mani(jobs_list)
