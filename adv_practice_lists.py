from operator import sub, mul, add, truediv


#функция is_continuous_sequence, которая проверяет, является ли переданная последовательность целых чисел возрастающей непрерывно (не имеющей пропусков чисел)
def is_continuous_sequence(sequence_list):
    if len(sequence_list) < 2:
        return False
    sequence = []
    for i in range(sequence_list[0], sequence_list[-1] + 1):
        sequence.append(i)
    if sequence == sequence_list:
        return True
    return False


#функция compare_version, которая сравнивает переданные версии version1 и version2. Если version1 > version2, то функция должна вернуть 1, если version1 < version2, то -1, если же version1 = version2 — 0.
def compare_version(version1, version2):
    major_version1, minor_version1 = version1.split('.')
    major_version2, minor_version2 = version2.split('.')
    if int(major_version1) > int(major_version2):
        return 1
    if int(major_version1) == int(major_version2):
        if int(minor_version1) == int(minor_version2):
            return 0
        if int(minor_version1) > int(minor_version2):
            return 1
        return -1
    return -1

#функция length_of_last_word, которая возвращает длину последнего слова переданной на вход строки.
#Словом считается любая последовательность не содержащая пробелы, символы перевода строки \n и табуляции \t.
def length_of_last_word(string):
    counter = 0
    for i in string.strip(' '):
        counter += 1
        if i == '\n' or i == '/t' or i == ' ':
            counter = 0
    return counter

#функция hamming_weight, которая считает вес Хэмминга.Вес Хэмминга это количество единиц в двоичном представлении числа.

def hamming_weight(dec_num):
    bin_num = format(dec_num, 'b')
    counter = 0
    for i in bin_num:
        if i != '1':
            continue
        counter += 1
    return counter

#функция same_parity_filter, которая принимает на вход список и возвращает новый список, состоящий из элементов, у которых такая же чётность, как и у первого элемента исходного списка.

def same_parity_filter(lst):
    result = []
    if lst:
        ost = lst[0] % 2
        for i in lst:
            if i % 2 == ost:
                result.append(i)
    return result
#функция find_longest_length,
#принимающая на вход строку и возвращающая
#длину максимальной последовательности
#из неповторяющихся символов. Подстрока может
#в строке qweqrty, можно выделить следующие подстроки: qwe, weqrty.

def find_longest_length(string):
    i = 0
    substrings_dict = {}
    seen_chars = {}
    substring = ''
    while i < len(string):
        if string[i] in seen_chars:
            substrings_dict[substring] = len(substring)
            i = seen_chars[string[i]] + 1
            seen_chars = {}
            substring = ''
            continue
        substring += string[i]
        seen_chars[string[i]] = i
        i += 1
    substrings_dict[substring] = len(substring)
    return max(substrings_dict.values())

#функцию chunked, которая принимает на вход число и последовательность.
#Число которое задает размер чанка (куска). Функция должна вернуть список,
#состоящий из чанков указанной размерности. При этом список должен
#делиться на куски-списки, строка — на строки, кортеж — на кортежи.

def chunked(chunk_length, items):
    result = []
    i = 0
    while i < len(items):
        result.append(items[i: i + chunk_length])
        i += chunk_length
    return result

#В данном упражнении необходимо реализовать стековую машину,
#то есть алгоритм, проводящий вычисления
#по обратной польской записи.Например, выражение (1 + 2) * 4 + 3
#в постфиксной нотации будет выглядеть так: 1 2 + 4 * 3 +,
#а результат вычисления: 15. Другой пример - выражение: 7 - 2 * 3,
#в постфиксной нотации: 7 2 3 * -, результат: 1.
#функцию rpn_calc, которая принимает список, каждый элемент
#которого содержит число или знак операции (+, -, *, /).
#Функция должна вернуть результат вычисления
#по обратной польской записи.


def rpn_calc(items):
    operators = {'+': add, '-': sub, '*': mul, '/': truediv}
    stack = []
    for item in items:
        if item in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operators[item](operand1, operand2))
        else:
            stack.append(item)
    return stack[0]
#функция mirror_matrix, которая принимает двумерный список (матрицу)
#и изменяет его (по месту) таким образом, что правая половина
#матрицы становится зеркальной копией левой половины,
#симметричной относительно вертикальной оси матрицы.
#Если ширина матрицы — нечётная,
#то "средний" столбец не должен быть затронут.


def mirror_matrix(matrix):
    for i, _ in enumerate(matrix[:]):
        buffer = matrix.pop(i)
        length = len(buffer) // 2
        if len(buffer) % 2 == 0:
            matrix_string = buffer[:length] + buffer[length - 1::-1]
        else:
            matrix_string = buffer[:length] + buffer[length::-1]
        matrix.insert(i, matrix_string)
   
#функция summary_ranges, которая находит в списке непрерывные
#возрастающие последовательности чисел и возвращает список
#с их перечислением.

def summary_ranges(source):
    fitting_sequences = []
    sub_result = []
    result = []
    i = 1
    while i < len(source):
        if source[i - 1] - source[i] == -1:
            if not fitting_sequences:
                fitting_sequences.append(source[i - 1])
            fitting_sequences.append(source[i])
        elif fitting_sequences:
            sub_result.append(fitting_sequences)
            fitting_sequences = []
        if i == len(source) - 1 and fitting_sequences:
            sub_result.append(fitting_sequences)
        i += 1
    for item in sub_result:
        result.append(('{}->{}').format(min(item), max(item)))
    return result

