def single_root_words(root_word, *other_words):
    same_words = []
    words = list(other_words)

    # преобразвание строки `root_word` в нижний регистр, преобразование`i`-го элемент списка `words` в нижний регистр,
    # проверка, содержится ли строка `root_word` в строке `words[i]`, проверка, содержится ли строка `words[i]` в строке `root_word`.

    for i in range(len(words)):
        if root_word.lower() in words[i].lower() or words[i].lower() in root_word.lower():
            same_words.append(words[i])
    # возвращаем образованный список

    return (same_words)


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# вывод результата.
print(result1)
print(result2)