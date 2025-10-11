def count_words (text):
#Подсчитывает количество слов в тексте
    words = text.split()
    return len (words)
def count_lines (text):
#Подсчитывает количество строк в тексте
    Lines = text.split('\\n')
    return len(lines)
def analyze_sentiment(text):
#\"\"\"Анализирует тональность текста\"\"\"
    positive_words = ['хорошо', 'отлично', 'прекрасно']
    negative_words = ['плохо', 'ужасно', 'отвратительно']
    score = 0
    for word in text.lower().split():
        if word in positive_words:
            score += 1
# Пока не завершено -нужно добавить negative words