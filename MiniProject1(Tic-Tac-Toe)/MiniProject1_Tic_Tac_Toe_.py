from functions import *

print("""Игра Крестики-Нолики

Работа для SkillFactory FullStack

Правила игры:
  Игроки ставят фигуры по очереди.
  Побеждлает игрок, первый выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали. 

Что бы поставвить фигуру укажите номер ячейк:""")

field_template()

while True:
    print("""Выберите режим:
1) Player VS Player
2) Player VS PC
3) Выход""")
    try:
        mod = int(input("Введите номер режима:"))
    except ValueError:
        print("\nОшибка(номер режима не должен содержать символы)\n")
        continue
    
    if mod == 1:
        print("\n***Player VS Player***")
        start_game(1)
    elif mod == 2:
        print("\n***Player VS PC***")
        start_game(2)
    elif mod == 3:
        print("\n***Завершение работы***\n")
        break
    else:
        print("\nОшибка(неверный номер режима)\n")