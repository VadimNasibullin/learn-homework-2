"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():


    with open('referat.txt', 'r', encoding='utf-8') as ref:
        for line in ref:
            print('Длинна строки:', len(line))


    with open('referat.txt', 'r', encoding='utf-8') as ref:
        all = ref.read()
        print('Колличество слов в тексте: ', len(all.split()))


    with open('referat.txt', 'r', encoding='utf-8') as ref:
        for line in ref:
            repl = ref.read()
            repl = repl.replace('.', '!')


    with open('referat2.txt', 'w', encoding='utf-8') as ref:
        ref.write(repl)
              







if __name__ == "__main__":
    main()
