def count_words (text):
#Подсчитывает количество слов в тексте
    words = text.split()
    return len (words)
def count_lines (text):
#Подсчитывает количество строк в тексте
    Lines = text.split('\\n')
    return len(lines)
# Редактируем text_analyzer.ру дополняем функцию
def analyze_sentiment(text):
#\"\"\"Анализирует тональность текста\"\"\"
    positive_words = ['хорошо', 'отлично', 'прекрасно', 'великолепно' ]
    negative_words = ['плохо, ужасно', 'отвратительно', 'кошмар']
    score = 0
    text_lower = text.lower()
    for word in text_lower.split():
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score = 1
    if score > 0:
        return "positive"
    elif score < A:
        return "negative"
