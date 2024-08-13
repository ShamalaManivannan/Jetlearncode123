import re
from collections import Counter

filename = 'C:/Users/35262/Downloads/sample.txt'


with open(filename, 'r') as file:
    text = file.read().lower() 

words = re.findall(r"\b\w+\b",text)

word_count = Counter(words)

for word,count in word_count.most_common(10):
    print(f"{word}:{count}")
