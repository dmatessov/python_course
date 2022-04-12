class BookIOErrors(Exception):
    pass


class NotExistingExtensionError(BookIOErrors):
    """если вызываемый метод у класса книги отсутствует"""
    pass


class PermissionDeniedError(BookIOErrors):
    """для ситуаций, когда запись в книгу запрещена,"""
    pass


class PageNotFoundError(BookIOErrors):
    """для ситуаций, когда методы обращаются к несуществующей странице"""
    pass


class TooLongTextError(BookIOErrors):
    """для ситуаций, когда записываемый текст не помещается на странице"""
    pass


class Book:
    def __init__(self, title, content=None):
        self.title = title
        self.content = content or []
        self.size = len(self.content)

    def read(self, page):
        raise NotImplementedError

    def write(self, page, text):
        raise NotImplementedError


class Novel(Book):
    """класс описывающий книгу и методы работы с ней"""

    def __init__(self, author, year, title, content=None):
        """конструктор"""
        super().__init__(title, content)
        self.author = author  # имя автора (строка)
        self.year = year  # год издания (целое)
        self.bookmark = dict()  # закладки (словарь {читатель:номер страницы})

    def read(self, page):
        """возвращает страницу"""
        if (page >= 0) and (page < len(self.content)):
            return self.content[page]
        else:
            raise PageNotFoundError

    def set_bookmark(self, person, page):
        """устанавливает закладку в книгу book"""
        self.bookmark[person] = page

    def get_bookmark(self, person):
        """получает номер страницы установленной закладки в книге book"""
        try:
            return self.bookmark[person]
        except KeyError:
            raise PageNotFoundError

    def del_bookmark(self, person):
        """удаляет закладку читателя person, если она установлена"""
        try:
            self.bookmark.pop(person)
        except KeyError:
            pass

    def write(self, page, text):
        """делает запись текста text на страницу page """
        raise PermissionDeniedError


class Notebook(Book):
    """класс описывающий тетрадь и методы работы с ней"""

    # -- max_sign, максимальное количество знаков, которые можно написать на странице
    # (целое, по умолчанию = 2000). В случае возникновения ситуаций, описанных в
    # предыдущем задании, должны выбрасываться соответствующие исключения.
    # -- size, количество страниц (по умолчанию - 12), если при создании экземпляра
    # класса в параметре content передается не пустой список, значение этого атрибута
    # устанавливается равной длине переданного списка. Если атрибут content не передан
    # явно, то создается список пустых строк размером size.
    def __init__(self, title, size=12, max_sign=2000, content=None):
        """конструктор"""

        if content is None:
            self.size = size
            content = [""] * size
        else:
            for page in content:
                if len(page) > max_sign:
                    raise TooLongTextError
            self.size = len(content)
        self.max_sign = max_sign

        super().__init__(title, content)

    def read(self, page):
        """возвращает страницу с номером page"""
        if (page >= 0) and (page < len(self.content)):
            return self.content[page]
        else:
            raise PageNotFoundError

    def write(self, page, text):
        if (page >= 0) and (page < len(self.content)):
            new_text = self.content[page] + text
            if len(new_text) > self.max_sign:
                raise TooLongTextError
            else:
                self.content[page] = new_text
        else:
            raise PageNotFoundError
        """делает запись текста text на страницу с номером page """


class Person:
    """класс описывающий человека и методы работы с книгой"""

    def __init__(self, name):
        """конструктор"""
        self.name = name

    def read(self, book, page):
        """читаем страницу с номером page в книге book"""
        return book.read(page)

    def write(self, book, page, text):
        """пишем на страницу с номером page в книге book"""
        book.write(page, text)

    def set_bookmark(self, book, page):
        """устанавливаем закладку в книгу book на страницу с номером page"""
        try:
            book.set_bookmark(self, page)
        except AttributeError:
            raise NotExistingExtensionError

    def get_bookmark(self, book):
        """получаем номер страницы установленной закладки в книге book"""
        try:
            return book.get_bookmark(self)
        except AttributeError:
            raise NotExistingExtensionError

    def del_bookmark(self, book):
        """удаляет закладку из книги book"""
        try:
            book.del_bookmark(self)
        except AttributeError:
            raise NotExistingExtensionError
