import pandas as pd
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt

shape_mask = np.array(Image.open("word-cloud/shape.png"))

df = pd.read_csv('word-cloud/wordcloud_results.csv')
tag_dict= dict(zip(df.TagName, df.Count))
print(tag_dict)

wordcloud = WordCloud(background_color='white', mask=shape_mask)
wordcloud.generate_from_frequencies(tag_dict)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
