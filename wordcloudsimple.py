#Change the file name before using
import os
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
text = open(path.join(d, 'NYTIMES.csv')).read()
wordcloud = WordCloud().generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
wordcloud = WordCloud(max_font_size=50).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()