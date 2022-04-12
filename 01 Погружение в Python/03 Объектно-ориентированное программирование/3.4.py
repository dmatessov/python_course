class NovelWithTable(Novel):
    def __init__(self, author, year, title, content=None, table=None):
        super().__init__(author, year, title, content)
        self.table = table or dict()

    def search(self, chapter):
        try:
            return self.table[chapter]
        except KeyError:
            raise PageNotFoundError

    def add_chapter(self, chapter, page):
        self.table[chapter] = page
        # if page in self.content:
        #     self.table[chapter] = page
        # else:
        #     raise PageNotFoundError

    def remove_chapter(self, chapter):
        self.table.pop(chapter)
        # try:
        #     self.table.pop(chapter)
        # except KeyError:
        #     raise PageNotFoundError


class AdvancedPerson(Person):

    def search(self, book, chapter):
        try:
            return book.search(chapter)
        except NotImplementedError:
            raise NotExistingExtensionError

    def read(self, book, page):
        if isinstance(page, str):
            pn = self.search(book, page)
        else:
            pn = page
        return super().read(book, pn)

    def write(self, book, page, text):
        if isinstance(page, str):
            pn = self.search(book, page)
        else:
            pn = page
        super().write(book, pn, text)
