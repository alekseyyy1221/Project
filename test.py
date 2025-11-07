#!/usr/bin/env python3
from Text_analyzer_aleksey1221 import *
text = "Это хороший текст. Все отлично работает!"
print (f"Слов: {count_words (text)}")
print (f"Тональность: {analyze_sentiment(text)}")
