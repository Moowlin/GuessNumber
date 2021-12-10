# ---------------------------------------------------------------
# Program by Olga N.
#
# Vesion     Date      Info
# 1.0       12/07/21   разработана первая часть игры
#
# ---------------------------------------------------------------

from random import randint
from math import log, ceil

answersYES = ['y', 'yes']
answersNO = ['n', 'no']
answersGreater = ['>']
answersLess = ['<']
answersExit = ['x', 'exit']
# ======================================= def NumRangeValidation =======================================================
def NumRangeValidation():
    '''Определяем диапазон чисел, проверяем корректность ввода числа пользователем'''

    while True:
        try:
            NumRange = int(input('Определяем границы диапазона, укажите целое число до 1000000 '))
            if NumRange <= 0:
                print('Введите целое положительное число')
            if NumRange in range(1, 1000001):
                return NumRange
                break
        except ValueError:
            print('Введите целое положительное число')
# ================================================= def GUESS_1 ========================================================
def guess1():
    '''Пользователь угадывает загаданное программой число'''

    NumRange = NumRangeValidation()       # Определяем диапазон чисел, проверяем корректность ввода числа пользователем
    NumControl = randint(1, NumRange)     # Загадываем контрольное число
    count = 0                             # Заводим счетчик попыток угадать

    # Цикл угадываения числа:
    print(f'Угадайте загаданное число в диапазоне [1; {NumRange}] ')
    while True:
        count += 1
        # Проверка ввода числе пользователем
        try:
            Num = 0
            Num = int(input(f'Укажите целое положительное чсило в диапазоне [1; {NumRange}] '))
            # Сверяем введенное число с контрольным
            if Num > NumControl:
                print('Ваше число больше загаданного, попробуйте еще разок')
                continue
            if Num < NumControl:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                continue
            if Num == NumControl:
                print(f'Поздравляем! Вы угадали за {count} попыток')
                if count == ceil(log(NumRange, 2)):
                    print("Хороший результат")
                elif count < ceil(log(NumRange, 2)):
                    print("Отличный результат")
                elif count > ceil(log(NumRange, 2)):
                    print("Можно улучшить результат. Попробуйте еще раз.")
                break

            if Num not in range(1, NumRange + 1):
                print('Вы указали недопустимый ответ')
        except ValueError:
            print('Вы указали недопустимый ответ')
# ================================================= def GUESS_2 ========================================================


# ================================================= def CHOICE =========================================================
def choice():
    '''Выбор параметра запуска игры'''
    answers = ['2', 'x', 'exit', '1']
    answer = ""
    while answer not in answers:
        print("В игре есть два режима:",
              "1 - программа загадывает число, а вы пробуете его отгадать",
              "2 - вы загадывайте число, а программа пробует его отгадать",
              "Укажите желаемый режим или eXit для выхода", sep="\n")
        answer = input().lower().strip()
    return answer
# ===================================================== MAIN ===========================================================
print("Добро пожаловать в числовую угадайку!")
answer = choice()           # Выбор параметра запуска игры

while answer not in (answersYES + answersNO + answersExit):
    if answer == '1':       # если параметр 1 - запускам guess1
        guess1()
    elif answer == '2':     # если параметр 2 - запускаем guess2
        print("режим №2 еще не реализован =)")
#        guess2()

    answer = input("Хотите сыграть еще раз? y/n ").strip().lower()
    if answer in answersYES:
        answer = choice()
    elif answer in answersNO:
        print("Спасибо, что играли в числовую угадайку!")

    else:
        print("Непонятный ответ")