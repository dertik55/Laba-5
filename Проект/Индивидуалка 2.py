import re

def check_zh_i_sh(words):
    # Объединяем слова в одну строку
    text = ' '.join(words)
    
    # Находим все слова, содержащие "жи" или "ши"
    incorrect_patterns = re.findall(r'\bw*ж[и]w*|\bw*ш[и]w*', text)
    
    # Проверяем, есть ли неправильные сочетания
    if incorrect_patterns:
        print("Найдены слова с неправильными буквосочетаниями:")
        for word in incorrect_patterns:
            print(word)
    else:
        print("Все буквосочетания 'жи' и 'ши' записаны правильно.")

# Пример использования
words = ["жирный", "шишка", "жить", "шифр", "жизнерадостный", "шизофрения", "жужжать"]
check_zh_i_sh(words)


