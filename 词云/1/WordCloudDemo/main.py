#coding:utf-8
'''
1.wordcloud制作词云时，首先要对对文本数据进行分词，使用process_text（）方法，这一步的主要任务是去除停用词；
2.第二步是计算每个词在文本中出现的频率，生成一个哈希表。词频用于确定一个词的重要性
3.根据词频的数值按比例生成一个图片的布局，类IntegralOccupancyMap 是该词云的算法所在，是词云的数据可视化方式的核心。
生成词的颜色、位置、方向等
4.最后将词按对应的词频在词云布局图上生成图片，核心方法是generate_from_frequencies,不论是generate（）还是generate_from_text（）
都最终用到generate_from_frequencies,完成词云上各词的着色,默认是随机着色
5.词语的各种增强功能大都可以通过wordcloud的构造函数实现，里面提供了22个参数，还可以自行扩展。
'''
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import jieba
import numpy as np
from PIL import Image

#获取当前文件路径
my_path = os.path.dirname(__file__)
text_filename = my_path + "/lkqbg.txt"            #txt文件路径
stopwords_filename =  my_path + "/stopwords.txt"  #停用词文件路径
userdict_filename =  my_path + "/userdict.txt"   #用户词典文件路径  
image_filename =  my_path + "/lkq.jpg"            #背景图片路径  
cloud_filename =  my_path + "/cloud.png"          #标签云路径

#读入背景图片
abel_mask = np.array(Image.open(image_filename))

#读取要生成词云的文件
text_from_file_with_path = open(text_filename,encoding= 'utf-8').read()

#通过jieba分词进行分词并通过空格分隔和停用词清洗

stoplist = []
for line in open(stopwords_filename,encoding= 'utf-8').readlines():
    stoplist.append(line)  #line.strip().decode('utf-8', 'ignore')

#导入自定义词典，一个词占一行；每一行分三部分：词语+词频+词性（可省略，ns为地点名词），用空格隔开
#自定义词典举例：
#云计算 5
#李小福 2 nr
#创新办 3 i
#easy_install 3 eng
#好用 300
#韩玉赏鉴 3 nz
jieba.load_userdict(userdict_filename)
wordlist_after_jieba = jieba.cut(text_from_file_with_path, cut_all = True)
wordlist_after_jieba = [word for word in list(wordlist_after_jieba) if word not in stoplist] #去停用词
wl_space_split = " ".join(wordlist_after_jieba)
#my_wordcloud = WordCloud().generate(wl_space_split) 默认构造函数
my_wordcloud = WordCloud(
            background_color='white',     # 设置背景颜色
            mask = abel_mask,             # 设置背景图片
            max_words = 3000,             # 设置最大实现的字数
            stopwords = STOPWORDS,        # 设置停用词
            font_path = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',# 设置字体格式，如不设置显示不了中文
            max_font_size = 80,           # 设置字体最大值
            random_state = 30,            # 设置有多少种随机生成状态，即有多少种配色方案
            scale= .5
            ).generate(wl_space_split)

# 根据图片生成词云颜色
image_colors = ImageColorGenerator(abel_mask)
my_wordcloud.recolor(color_func = image_colors)

# 以下代码显示图片
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
my_wordcloud.to_image().save('t.png')