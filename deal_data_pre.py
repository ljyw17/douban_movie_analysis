# -*- coding: utf-8 -*-
import pandas

if __name__=="__main__":
    file_path = "movie_dataset.xlsx"
    df = pandas.read_excel(file_path, header=0)
    df = df.drop(['5星人数', '4星人数', '3星人数', '2星人数', '1星人数', '短评数量', '影评数量', '豆瓣网址', '官方网址', 'IMDb链接', '宣传海报链接', '总分（评分×评价人数）'], axis=1)
    for i in range(len(df)):
        df["制片国家/地区"][i] = str(df["制片国家/地区"][i]).split(" / ")[0]
        df["上映日期"][i] = str(df["上映日期"][i]).split("-")[0]
        df["上映日期"][i] = str(df["上映日期"][i]).split("(")[0]
        df["上映日期"][i] = str(df["上映日期"][i]).split("/")[0]
        if int(df["评分"][i]) == 0:
            df = df.drop(i, axis=0)
    df = df.rename(columns={"上映日期": "上映年份"})
    df = df.reset_index(drop=True)
    df.to_excel("movie_dataset_done.xlsx", encoding="utf_8_sig", index=0)