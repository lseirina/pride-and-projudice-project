import os
import string
from collections import Counter
import matplotlib.pyplot as plt


file_path = os.path.join("/mnt/c", "_wsl/venv/test0/gutenberg.org_files_1342_1342-0.txt")

with open(file_path, encoding="utf-8") as file:
    text = file.read()

translator = str.maketrans("", "", string.punctuation)
text = text.translate(translator)

text = text.lower()
words = text.split()

words_count = Counter(words)
common_words = words_count.most_common()
filtered_common_words = [(word, count) for word, count in common_words if len(word)>= 5]
filtered_common_words = filtered_common_words[:10]
words, count = zip(*filtered_common_words)

plt.bar(words, count)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Most Common Words in Pride and Prejudice")
plt.xticks(rotation=45)
print("Current working directory:", os.getcwd())
plt.savefig("my_plot.png")


