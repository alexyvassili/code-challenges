"""Дан access.log от nginx. Напишите программу, которая в реальном времени
    парсит лог и показывает топ 10 самых медленных ручек. При добавлении
    в файл новых строк скользящее окно может меняться, из него могут
    выбывать ручки или добавляться новые. При этом окно остается
    равным 10 записей.
    Пояснение от куратора
        - за скорость ручки принимается максимальное полученное значение.
        - выводим топ на каждой итерации
    Лог нгинха перепечатывать лень
"""
from collections import Counter


class LogStatistic:
    def __init__(self):
        self.statistic = Counter()

    def add(self, resource, req_time):
        self.statistic[resource] = max(self.statistic[resource], req_time)

    def show_top(self, top=10):
        n = 1
        for resource, req_time in self.statistic.most_common(top):
            print(f"{n}. {resource} - {req_time}")
            n += 1


log_statistic = LogStatistic()


def get_req_time(req_time_str):
    req_time_str = req_time_str.strip()  # ' 0.342 '
    req_time = float(req_time_str)  # 0.342
    req_time = int(req_time * 1000)  # 342
    return req_time


def parse_line(line):
    line_splitted = line.split('"')
    resource = line_splitted[1]
    req_time = get_req_time(line_splitted[4])
    return resource, req_time


def parse_log(logname: str, log_statistic: LogStatistic):
    with open(logname) as f:
        for line in f:
            resource, req_time = parse_line(line.strip())
            log_statistic.add(resource, req_time)
            log_statistic.show_top()
