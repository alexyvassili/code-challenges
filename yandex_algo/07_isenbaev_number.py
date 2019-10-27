"""Определим число Исенбаева следующим образом.
    У самого Владислава это число равняется нулю.
    У тех, кто играл с ним в одной команде, оно равняется единице.
    У тех, кто играл с однокомандниками Владислава, но не
    играл с ним самим, это число равняется двум, и так далее.
    Помогите автоматизировать процесс вычисления чисел Исенбаева,
    чтобы каждый олимпиадник в УрГУ мог знать, насколько
    близок он к чемпиону ACM ICPC.
    Исходные данные
    В первой строке записано целое число n - количество команд (1<=n<=100).
    В каждой из следующих строк записаны составы этих команд в виде фамилий
    трех участников. Фамилия каждого участника - непустая строка, состоящая
    из английских букв, длиной не более 20 символов.
    Первая буква фамилии заглавная, все остальные - строчные.
    Фамилия Владислава - "Isenbaev"
    Результат
    Для каждого участника, представленного во входных данных, выведите
    в отдельной строке через пробел его фамилию и число Исенбаева.
    Если это число не определено, выведите вместо него "undefined".
    Участники должны быть упорядочены по фамилии в лексикографическом порядке.
    Пример ввода см. в приложенном файле
"""
from collections import defaultdict, deque
from itertools import combinations


INPUT_FILE = "07_isenbaev_number_input.txt"
ROOT_PERSON = "Isenbaev"


def load_commands_from_file(input_file):
    with open(input_file) as f:
        nums_commands = int(next(f).strip())
        for line in f:
            yield line.strip().split()


def load_command(command, connected):
    for man1, man2 in combinations(command, 2):
        connected[man1].add(man2)
        connected[man2].add(man1)


def switch_isenbaev_numbers(connected, root_person):
    isenbaev_numbers = dict()
    isenbaev_numbers[root_person] = 0
    deq = deque()
    deq.append(root_person)
    while deq:
        person = deq.popleft()
        for connected_man in connected[person]:
            if connected_man not in isenbaev_numbers:
                isenbaev_numbers[connected_man] = isenbaev_numbers[person] + 1
                deq.append(connected_man)
    return isenbaev_numbers


def print_isenbaev_numbers(isenbaev_numbers, connected):
    for person in sorted(connected):
        isenbaev_num = isenbaev_numbers.get(person, 'undefined')
        print(f'{person} {isenbaev_num}')


def process_isenbaev_numbers():
    connected = defaultdict(set)
    for command in load_commands_from_file(INPUT_FILE):
        load_command(command, connected)
    isenbaev_numbers = switch_isenbaev_numbers(connected, ROOT_PERSON)
    print_isenbaev_numbers(isenbaev_numbers, connected)

process_isenbaev_numbers()

# Вывод:
# Ayzenshteyn 2
# Burmistrov 3
# Chevdar 3
# Cormen undefined
# Dublennykh 2
# Fominykh 1
# Isenbaev 0
# Ivankov 2
# Kurpilyanskiy 3
# Leiserson undefined
# Oparin 1
# Rivest undefined
# Samsonov 2
# Toporov 1
