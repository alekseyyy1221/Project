def count_words (text):
#Подсчитывает количество слов в тексте
    words = text.split()
    return len (words)
def count_lines (text):
#Подсчитывает количество строк в тексте
    Lines = text.split('\\n')
    return len(lines)
def count_characters (text):
#\"\"\"Подсчитывает количество символов (без пробелов)\"\"\"
    return len(text.replace("", "").replace("\n", ""))