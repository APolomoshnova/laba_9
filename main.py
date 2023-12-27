import string
import random
import threading

text = None
result = None


def input_text():
    input_type = input(
        "Выберите тип ввода данных: \n1. вручную\n2. сгенерировать случайным образом\nВведите тип ввода данных: ")
    if input_type == '1':
        text_input = input("Введите текст: ")
    elif input_type == '2':
        n = int(input("Введите длину генерируемого текста: "))
        text_input = ''.join(random.choice(string.ascii_letters + string.punctuation + " ") for _ in range(n))
    else:
        print("Неверный тип ввода данных")
        text_input = None
    return text_input


def count(text_input):
    cnt_lowercase = 0
    cnt_uppercase = 0
    cnt_punctuation = 0
    cnt_whitespace = 0

    for char in text_input:
        if char.islower():
            cnt_lowercase += 1
        elif char.isupper():
            cnt_uppercase += 1
        elif char in ['.', ',', '!', '?', ':', ';']:
            cnt_punctuation += 1
        elif char.isspace():
            cnt_whitespace += 1

    return cnt_lowercase, cnt_uppercase, cnt_punctuation, cnt_whitespace


def input_text_thread():
    global text
    text = input_text()


def count_text_thread():
    global result
    result = count(text)


if __name__ == '__main__':
    while True:
        print("\nМеню:")
        print("1. Ввод исходных данных")
        print("2. Решение задания")
        print("3. Результат работы алгоритма")
        print("4. Завершение работы программы")

        point = input("Введите пункт меню: ")

        if point == "1":
            input_thread = threading.Thread(target=input_text_thread)
            input_thread.start()
            input_thread.join()
        elif point == "2":
            if text:
                count_thread = threading.Thread(target=count_text_thread)
                count_thread.start()
                count_thread.join()
                print("Исходные данные: ", text)
                print("Задание решено")
            else:
                print("Исходные данные не введены")
        elif point == "3":
            if result:
                cnt_lowercase, cnt_uppercase, cnt_punctuation, cnt_whitespace = result
                print("Результат:")
                print("Количество строчных букв:", cnt_lowercase)
                print("Количество прописных букв:", cnt_uppercase)
                print("Количество знаков препинания:", cnt_punctuation)
                print("Количество пробелов:", cnt_whitespace)
            else:
                print("Входные данные не сгенерированы")
        elif point == "4":
            print("Программа завершена")
            break
        else:
            print("Выберите верный пункт меню")