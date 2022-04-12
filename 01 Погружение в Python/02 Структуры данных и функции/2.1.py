import string


def gen_ticket_number(count, series, length=6):
    """
    генератор номеров билетов, входные параметры: count - количество билетов,
    series - номер серии, необязательный аргумент length - количество цифр
    в номере, по умолчанию равен 6, выход - строка вида: <номер билета> <серия билета>
    """
    num_generator = gen_number(length)
    series_generator = gen_series(series)
    cur_series = next(series_generator)
    for _ in range(count):
        try:
            cur_number = next(num_generator)
        except StopIteration:
            num_generator = gen_number(length)
            cur_number = next(num_generator)
            cur_series = next(series_generator)
        yield cur_number + " " + cur_series


def gen_series(series):
    """
    генератор серий лотерейных билетов начиная с series по "ZZ" включительно, входные
    параметры: series -  - номер серии, выход - строка, состоящая из двух заглавных
    букв латинского алфавита
    """

    start_series = series.upper()
    base_siquence = string.ascii_uppercase
    # или можно использовать любую последовательность
    cur_position_1 = base_siquence.find(start_series[0])
    cur_position_2 = base_siquence.find(start_series[1])

    while (cur_position_1 < len(base_siquence)):
        while (cur_position_2 < len(base_siquence)):
            yield base_siquence[cur_position_1] + base_siquence[cur_position_2]
            cur_position_2 += 1
        cur_position_1 += 1
        cur_position_2 = 0


def gen_number(length=6):
    """
    генератор номеров лотерейных билетов в одной серии, входные параметры:
    необязательный аргумент length - количество цифр в номере, по умолчанию равен 6
    """
    s = ""
    for i in range(length):
        s = s + "9"
    max_number = int(s)

    for i in range(max_number):
        s = str(i + 1)
        while len(s) < length:
            s = "0" + s
        yield s