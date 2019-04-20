import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image

def DrawWordcloud(read_name):
    image = Image.open('timg.jpg')#作为背景形状的图
    graph = np.array(image)

    #参数分别是指定字体、背景颜色、最大的词的大小、使用给定图作为背景形状
    # max_words 要显示的词的最大个数
    # scale: float(default=1)  # 按照比例进行放大画布，如设置为1.5，则长和宽都是原来画布的1.5倍
    # mask: 如果参数为空，则使用二维遮罩绘制词云。如果 mask 非空，遮罩形状被 mask 取代
    wc = WordCloud(font_path = 'C:\\windows\\Fonts\\msyhbd.ttc',  #'C:\\windows\\Fonts\\simhei.ttf'
                   background_color = 'White',
                   max_words = 3000,
                   mask = graph,
                   random_state=30,
                   scale= 0.5)

    tb = pd.read_csv(read_name) #读取词频文件CSV（逗号分割）到DataFrame
    words = list(tb.word)  #词表
    values = tb.val #词频表

    dic = {}
    for key,val in zip(words, values):
        dic[key] = val

    wc.generate_from_frequencies(dic) #根据给定词频生成词云
    image_color = ImageColorGenerator(graph)
    plt.imshow(wc)
    plt.axis("off") #不显示坐标轴
    plt.show()
    wc.to_file('Wordcloud.png')#保存的图片命名为Wordcloud.png

if __name__=='__main__':

    DrawWordcloud("word_lst.csv")

