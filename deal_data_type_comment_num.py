# -*- coding: utf-8 -*-
import pandas, numpy

if __name__=="__main__":
    file_path = "movie_dataset_done.xlsx"
    df = pandas.read_excel(file_path, header=0)
    type_df = pandas.DataFrame()
    type_df["类型"] = numpy.nan
    type_df["平均评分"] = numpy.nan

    row = 0
    for i in range(len(df)):
        types = df["类型"][i].split("/")
        for type in types:
            if type not in type_df["类型"].to_list():
                type_df.loc[row] = numpy.nan
                type_df["类型"][row] = type
                row += 1

    for i in range(len(type_df)):
        type = type_df["类型"][i]
        temp_list = list()
        for j in range(len(df)):
            if type in df["类型"][j]:
                temp_list.append(df["评分"][j])
        if len(temp_list) < 1000:
            type_df = type_df.drop(i, axis=0)
            continue
        type_df["平均评分"][i] = numpy.mean(temp_list)
    type_df = type_df.reset_index(drop=True)

    type_df.to_excel("type_rate.xlsx", encoding="utf_8_sig", index=0)