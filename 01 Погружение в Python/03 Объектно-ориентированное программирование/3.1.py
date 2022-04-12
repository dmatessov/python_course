class Matrix:
    MAX_SIZE = 1000

    def __init__(self, max_size=None):
        self.max_size = max_size or self.MAX_SIZE
        self._items = [None]
        self._size = 1

    def append(self, element=None):
        if element is not None:
            try:
                next_free = self._items.index(None)
                self._items[next_free] = element
                # - в случае, когда добавляемый элемент, занимает место первого
                # элемента в последней строке матрицы, матрицу необходимо "расширить",
                # увеличив размер матрицы на 1 (добавить один столбец и одну строку),
                # при этом добавленные в матрицу элементы сдвигаются к началу таким образом,
                # чтобы между ними не было "нулевых" элементов.
                if next_free == self._size * (self._size - 1):
                    if self._size < self.max_size:
                        for _ in range(2 * self._size + 1):
                            self._items.append(None)
                        self._size += 1
            except ValueError:
                # Попытка добавить элемент в полностью заполненную матрицу
                # (не имеющей "нулевых" элементов) вызывает исключение IndexError
                raise IndexError

    def pop(self):
        if self._size == 1 and self._items[0] is None:
            # при попытке извлечь элемент из матрицы размером size=1, заполненную "нулевым"
            # элементом, выбрасывается исключение IndexError
            raise IndexError
        else:
            index = self._items.index(None) - 1
            value = self._items[index]
            self._items[index] = None
            # в случае, когда после извлечения элемента, количество добавленных элементов
            # можно разместить в матрице меньшего размера, таким образом, что последняя
            # строка полученной матрицы будет содержать только пустые элементы, матрицу
            # необходимо "сжать" (уменьшить ее размер на 1) перед тем, как вернуть извлекаемое значение
            if index == (self._size * (self._size - 3)) + 2:
                for _ in range((2 * self._size) - 1):
                    self._items.pop()
                self._size -= 1
            return value

    def __str__(self):
        s = ""
        for i in range(self._size):
            new_line = ""
            for j in range(self._size):
                if j == 0:
                    new_line = str(self._items[i*self._size + j])
                else:
                    new_line = new_line + " " + str(self._items[i*self._size + j])
            if s == "":
                s = new_line
            else:
                s = s + "\n" + new_line
        return s

    @classmethod
    def from_iter(cls, iter_obj, max_size=None):
        import collections
        if isinstance(iter_obj, collections.Iterable):
            m = Matrix(max_size)
            for e in iter_obj:
                m.append(e)
            return m
        else:
            raise TypeError

