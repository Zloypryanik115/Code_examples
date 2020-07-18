#функция binary_sum, которая принимает на вход два двоичных числа (в виде строк) и возвращает их сумму

def binary_sum(binary_arg1, binary_arg2):
    dec_arg1 = int(binary_arg1, 2)
    dec_arg2 = int(binary_arg2, 2)
    result = dec_arg1 + dec_arg2
    return format(result, 'b')
    
#функция fib, находящую положительные Числа Фибоначчи. Аргументом функции является порядковый номер числа.

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
    
#функция is_palindrome, которая принимает на вход слово, определяет является ли оно палиндромом и возвращает логическое значение

def is_palindrome(string):
    return string == string[::-1]

#функции:
#
#is_degenerated должна возвращать истину, если отрезок вырожден в точку (начало и конец совпадают);
#is_vertical должна возвращать "истину", если отрезок — вертикальный;
#is_horizontal должна возвращать "истину", если отрезок — горизонтальный;
#is_inclined должна возвращать "истину", если отрезок — наклонный (не вертикальный и не горизонтальный).

def is_degenerated(line):
    point1 = line[0]
    point2 = line[1]
    return point1[0] == point2[0] and point1[1] == point2[1]


def is_vertical(line):
    point1 = line[0]
    point2 = line[1]
    return point1[0] == point2[0] and point1[1] != point2[1]


def is_horizontal(line):
    point1 = line[0]
    point2 = line[1]
    return point1[0] != point2[0] and point1[1] == point2[1]


def is_inclined(line):
    point1 = line[0]
    point2 = line[1]
    return point1[0] != point2[0] and point1[1] != point2[1]

#две функции, которые "вращают" тройку(кортеж из трёх элементов) влево и вправо

def rotate_left(triple):
    return triple[1:] + triple[:1]


def rotate_right(triple):
    return triple[2:] + triple[:2]


def rotate_left_1(triple):
    elem1, elem2, elem3 = triple
    return (elem2, elem3, elem1)


def rotate_right_1(triple):
    elem1, elem2, elem3 = triple
    return (elem3, elem1, elem2)


#функция is_power_of_three, которая определяет, является ли переданное число натуральной степенью тройки.
def is_power_of_three(number):
    while number > 1:
        number = number / 3
    return number == 1


#функция diff, которая принимает два угла (int) со значениями в диапазоне от 0 до 360, и возвращает наименьшую разницу между ними.
def diff(angle1, angle2):
    norm_angle1 = angle1 % 360
    norm_angle2 = angle2 % 360
    buff_diff = abs(norm_angle1 - norm_angle2)
    return min(buff_diff, 360 - buff_diff)


#функция fizz_buzz, которая возвращает строку с числами (через пробел) в диапазоне от begin до end включительно. При этом:
#
#Если число делится без остатка на 3, то вместо него выводится слово Fizz
#Если число делится без остатка на 5, то вместо него выводится слово Buzz
#Если число делится без остатка и на 3, и на 5, то вместо числа выводится слово FizzBuzz
#В остальных случаях в строку добавляется само число

def fizz_buzz(begin, end):
    result = ''
    while begin <= end:
        if begin % 3 == 0 and begin % 5 == 0:
            result = result + 'FizzBuzz' +' '
        elif begin % 3 == 0:
            result = result + 'Fizz' + ' '
        elif begin % 5 == 0:
            result = result + 'Buzz' + ' '
        else:
            result = result + str(begin) + ' '
        begin += 1
    return result.strip(' ')
