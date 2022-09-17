"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():


    dictionary = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Михаил', 'age': 32, 'job': 'Manager'},
        {'name': 'Валентина', 'age': 29, 'job': 'clerk'}
        ]

    import csv


    with open('dictionary.csv', 'w', encoding='utf-8',newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=',')
        writer.writeheader()
        for dictionary in dictionary:
            writer.writerow(dictionary)        




if __name__ == "__main__":
    main()
