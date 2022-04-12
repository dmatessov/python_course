class Book:
    def __init__(self, title, content=None):
        self.title = title
        self._content = content or []
        self.size = len(self._content)

    def read(self, page):
        raise NotImplementedError

    def write(self, page, text):
        raise NotImplementedError

    def __getitem__(self, item):
        if (item > 0) and (item <= len(self._content)):
            return self._content[item - 1]
        else:
            raise PageNotFoundError

    def __setitem__(self, key, value):
        if (key > 0) and (key <= len(self._content)):
            self._content[key - 1] = value
        else:
            raise PageNotFoundError

    def __len__(self):
        return len(self._content)

    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __eq__(self, other):
        return len(self) == len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __ge__(self, other):
        return len(self) >= len(other)



class Page:
    def __init__(self, text=None, max_sign=2000):
        self._text = '' if text is None else text
        self.max_sign = max_sign

    def __len__(self):
        return len(self._text)

    def __lt__(self, other):
        if isinstance(other, str) or isinstance(other, Page):
            return len(self) < len(other)
        else:
            raise TypeError

    def __gt__(self, other):
        if isinstance(other, str) or isinstance(other, Page):
            return len(self) > len(other)
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, str) or isinstance(other, Page):
            return len(self) == len(other)
        else:
            raise TypeError

    def __le__(self, other):
        if isinstance(other, str) or isinstance(other, Page):
            return len(self) <= len(other)
        else:
            raise TypeError

    def __ge__(self, other):
        if isinstance(other, str) or isinstance(other, Page):
            return len(self) >= len(other)
        else:
            raise TypeError

    def __str__(self):
        return self._text

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        if isinstance(other, str):
            return other + self._text
        else:
            raise TypeError

    def __add__(self, other):
        if isinstance(other, str) or isinstance(other, Page):
            new_text = self._text + other
            if len(new_text) > self.max_sign:
                raise TooLongTextError
            self._text = new_text
            return self
        else:
            raise TypeError