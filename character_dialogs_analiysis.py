import os

import nltk
nltk.download("punkt")
from nltk.tokenize import sent_tokenize

from textblob import TextBlob

import matplotlib.pyplot as plt

file_path = os.path.join("/mnt/c", "_wsl/venv/test0/gutenberg.org_files_1342_1342-0.txt")

with open(file_path, encoding='utf-8') as file:
    text = file.read()

sentences = sent_tokenize(text)

speakers = []
for sentence in sentences:
    if ":" in sentence:
        speaker = sentence.split(":")[0].strip()
        speakers.append(speaker)

dialogues = {}
for sentence, speaker in zip(sentences, speakers):
    if speaker in dialogues:
        dialogues[speaker].append(sentence)
    else:
        dialogues[speaker] = [sentence]


character_analysis = {}
for speaker, dialogue in dialogues.items():
    num_lines = len(dialogue)
    average_sentence_length = sum(len(sent.split()) for sent in dialogue) / len(dialogue)
    sentiment_scores = [TextBlob(sent).sentiment.polarity for sent in dialogue]
    average_sentiment = sum(sentiment_scores) / num_lines
    character_analysis[speaker] = {
        "num_lines": num_lines,
        "average_sentence_length": average_sentence_length,
        "average_sentiment": average_sentiment
    }
speakers = list(character_analysis.keys())
average_sentiment = [character_analysis[speaker]["average_sentiment"] for speaker in speakers]
if num_lines == 1:
    plt.bar(speakers, average_sentiment)
    plt.xlabel("Character")
    plt.ylabel("Average Sentiment")
    plt.title("Average Sentiment of characters in novel")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("temper_plot.png")

