from wordcloud import WordCloud
import PIL .Image as image
import numpy as np
import jieba, pandas

def trans_CN(text):
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result

if __name__=="__main__":
    file_path = r"Pure Hearts Into Chinese Showbiz.xlsx"
    df = pandas.read_excel(file_path, header=0)
    text = ""
    for i in range(len(df)):
        text += df["short"][i]
    text = trans_CN(text)
    wordcloud = WordCloud(
        font_path = r"C:\Windows\Fonts\msyh.ttc"
    ).generate(text)
    image_produce = wordcloud.to_image()
    image_produce.show()
    image_produce.save("{}.jpg".format(file_path.split(".")[0]))