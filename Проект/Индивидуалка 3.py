def modify_word(word):
    # Удаляем первую букву 'о', если она есть
    if 'о' in word:
        word = word.replace('о', '', 1)  # Удаляем только первое вхождение
    
    # Удаляем последнюю букву 'л', если она есть
    if word.endswith('л'):
        word = word[:-1]  # Удаляем последний символ
    
    return word

# Пример использования
input_word = "колобок"
modified_word = modify_word(input_word)
print(modified_word)  # Вывод: "кобок"
