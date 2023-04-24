# Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# 📌 Возвращается строка в нижнем регистре.
def only_alphabet(text: str) -> str:
    chars = [char for char in text.lower() if char in 'abcdefghijklmnopqrstuvwxyz ']
    return ''.join(chars)


if __name__ == '__main__':
    import doctest
    doctest.testfile('doctest_task01.txt', verbose=True)
