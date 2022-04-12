def create_matrix(size):
    """
    Функция принимает на вход размер квадратной матрицы. Возвращает 'пустую' матрицу
    размером size x size, (все элементы матрицы имеют значение равное 0).
    :param size: int > 0
    :return: list
    """
    new_matrix = []
    for _ in range(size):
        new_line = []
        for _ in range(size):
            new_line.append(None)
        new_matrix.append(new_line)
    return new_matrix


def add_element(element, matrix):
    """
    Функция добавляет element в матрицу matrix и при необходимости изменяет размер
    матрицы. Возвращает полученную матрицу.
    :param element: string
    :param matrix: list
    :return: list
    """
    if element is not None:
        # в случае, когда добавляемый элемент, занимает место первого элемента в последней строке матрицы,
        # матрицу необходимо "расширить"
        done = False
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] is None:
                    if (i == len(matrix) - 1) and (j == 0):
                        new_matrix = create_matrix(len(matrix) + 1)
                        for k in range(len(matrix)):
                            for l in range(len(matrix)):
                                add_element(matrix[k][l],new_matrix)
                        add_element(element, new_matrix)
                        matrix = new_matrix
                    else:
                        matrix[i][j] = element
                    done = True
                    break
            if done:
                break
    return matrix


def matrix_to_string(matrix):
    """
    Функция создает строковое представление matrix - строку, в которой строки матрицы
    разделены переносом строки, а элементы строки разделены пробелами.
    :param matrix: list
    :return: string
    """
    s = ""
    for i in range(len(matrix)):
        new_line = ""
        for j in range(len(matrix)):
            if j == 0:
                new_line = str(matrix[i][j])
            else:
                new_line = new_line + " " + str(matrix[i][j])

        if (s == ""):
            s = new_line
        else:
            s = s + "\n" + new_line
    return s
