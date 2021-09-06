def num_translate():
    translate = {'null': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь','nine': 'девять', 'ten': 'десять'}
    number = (translate.get(input('введите число на англ')))
    return(number)


print(num_translate())
