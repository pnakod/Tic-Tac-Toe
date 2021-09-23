import random

# Подсказка номеров ячеек
def field_template():
    print("""
  -------------
  | 1 | 2 | 3 |
  -------------
  | 4 | 5 | 6 |
  -------------
  | 7 | 8 | 9 |
  -------------
""")

# Шаблон поля
def shab(matrix_inp = None):
    print("""
  -------------
  | {} | {} | {} |
  -------------
  | {} | {} | {} |
  -------------
  | {} | {} | {} |
  -------------
""".format(*matrix_inp))

# Декоратор функции хода
def decor_step(func):
    def wrapper(matrix_inp = None, count = None):
        shab(matrix_inp)
        return func(matrix_inp, count)
    return wrapper

# Ход играков
@decor_step
def step_player(matrix_inp = None, count = None):
    matrix_loc = matrix_inp.copy() 
    try:
        choice = int(input("У кажите номер ячейки:"))
    except ValueError:
        print("\nОшибка(неверный номер ячейки)\n")
        field_template()
        return matrix_loc

    if choice < 1 or choice > 9:
        print("\nОшибка(неверный номер ячейки)\n")
        field_template()
        return matrix_loc

    if matrix_loc[choice - 1] != "-":
        print("\nОшибка(ячейка уже занята)\n")
        return matrix_loc
    else:
        if count == 0:
            matrix_loc[choice - 1] = "X"
        elif count == 1: 
            matrix_loc[choice - 1] = "O"
    
    return matrix_loc

# Ход компьютера
@decor_step
def step_pc(matrix_inp = None, count = None):
    matrix_loc = matrix_inp.copy() 
    matrix_choice = []
    for index, i in enumerate(matrix_loc):
        if i == "-":
            matrix_choice.append(index)   
    choice = random.choice(matrix_choice)
    matrix_loc[choice] = "O"
    return matrix_loc

# Проверка победы
def cheak_win(matrix_inp):
    if (matrix_inp[0] == matrix_inp[1] and  matrix_inp[0] == matrix_inp[2] and  matrix_inp[0] != "-") or \
       (matrix_inp[3] == matrix_inp[4] and  matrix_inp[3] == matrix_inp[5] and  matrix_inp[3] != "-") or \
       (matrix_inp[6] == matrix_inp[7] and  matrix_inp[6] == matrix_inp[8] and  matrix_inp[6] != "-") or \
       (matrix_inp[0] == matrix_inp[3] and  matrix_inp[0] == matrix_inp[6] and  matrix_inp[0] != "-") or \
       (matrix_inp[1] == matrix_inp[4] and  matrix_inp[1] == matrix_inp[7] and  matrix_inp[1] != "-") or \
       (matrix_inp[2] == matrix_inp[5] and  matrix_inp[2] == matrix_inp[8] and  matrix_inp[2] != "-") or \
       (matrix_inp[0] == matrix_inp[4] and  matrix_inp[0] == matrix_inp[8] and  matrix_inp[0] != "-") or \
       (matrix_inp[2] == matrix_inp[4] and  matrix_inp[2] == matrix_inp[6] and  matrix_inp[2] != "-"):
        return 1
    elif "-" not in matrix_inp:
        return 2
    else:
        return 0

# Старт игры
def start_game(mod_inp):
    matrix = ["-" for i in range(9)]
    count = 0
    while True:
        matrix_new = []
        if count > 1:
            count = 0
        # Режим с 2 игроками, ход
        if mod_inp == 1:
            if count == 0:
                print("\nХод первого игрока!(X)")
            if count == 1:
                print("\nХод второго игрока!(O)")
            matrix_new = step_player(matrix, count)

        # Режим с пк, ход
        elif mod_inp == 2:
            if count == 0:
                print("\nХод игрока!(X)")
                matrix_new = step_player(matrix, count)
            if count == 1:
                print("\nХод компьютера!(O)")
                matrix_new = step_pc(matrix, count)

        if matrix_new != matrix:
            matrix = matrix_new
             # Режим с 2 игроками, проверка победы
            if mod_inp == 1:
                if cheak_win(matrix) == 1:
                    if count == 0:
                        shab(matrix)
                        print("\nПобедил первый игрок!(X)\n\n")
                        break
                    if count == 1:
                        shab(matrix)
                        print("\nПобедил второй игрок!(O)\n\n")
                        break        
            
            # Режим с пк, проверка победы
            elif mod_inp == 2:
                if cheak_win(matrix) == 1:
                    if count == 0:
                        shab(matrix)
                        print("\nВы победили!\n\n")
                        break
                    if count == 1:
                        shab(matrix)
                        print("\nВы проиграли!\n\n")
                        break

             # Ничья
            if cheak_win(matrix) == 2:
                    shab(matrix)
                    print("\nНичья!\n\n")
                    break

        else:
            continue

        count += 1
