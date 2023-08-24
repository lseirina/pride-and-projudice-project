import os

from wordcloud import WordCloud
import matplotlib.pyplot as plt

file_path = os.path.join("/mnt/c", "_wsl/venv/test0/gutenberg.org_files_1342_1342-0.txt")

with open(file_path, encoding="utf-8") as file:
    text = file.read()

wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=100).generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
print("Current working directory:", os.getcwd())
plt.savefig("my_word_cloud.png")
