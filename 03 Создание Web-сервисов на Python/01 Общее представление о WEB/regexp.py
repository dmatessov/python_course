def calculate(data, findall):
    matches = findall(r"([abc])([+-]{0,1})=([abc]{0,1})([+-]{0,1}\d{0,})")  # Если придумать хорошую регулярку, будет просто
    for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        # Если бы могло быть только =, вообще одной строкой все считалось бы, вот так:
        m = int(s+'1')
        if s == '':
            k = 0
        else:
            k = 1
        data[v1] = k * data[v1] + m * (data.get(v2, 0) + int(n or 0))

    return data
