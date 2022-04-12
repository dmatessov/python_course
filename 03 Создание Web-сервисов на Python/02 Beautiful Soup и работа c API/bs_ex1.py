from bs4 import BeautifulSoup
import unittest


def parse(path_to_file):
    # Поместите ваш код здесь.
    # ВАЖНО!!!
    # При открытии файла, добавьте в функцию open необязательный параметр
    # encoding='utf-8', его отсутствие в коде будет вызвать падение вашего
    # решения на грейдере с ошибкой UnicodeDecodeError
    f = open(path_to_file, 'r', encoding="utf-8")
    html = f.read()
    soup = BeautifulSoup(html, 'lxml')

    # найти её тело (это <div id="bodyContent">) и внутри него подсчитать:
    body = soup.find(id="bodyContent")

    imgs = 0
    headers = 0
    for child in body.descendants:
        if child.name == 'img':
            try:
                width = int(child['width'])
            except:
                width = 0
            if width >= 200:
                imgs = imgs + 1
        if child.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            if child.text[0] in ['E', 'T', 'C']:
                headers = headers + 1

    linkslen = 0
    links = body.find_all("a")
    for tag in links:
        curlen = 1
        for tag in tag.find_next_siblings():
            if tag.name != 'a':
                break
            curlen += 1
        if curlen > linkslen:
            linkslen = curlen
        tag = tag.find_next("a")

    lists = 0
    for child in body.find_all(['ul', 'ol']):
        parent = child.find_parent(['ul', 'ol'])
        if parent is None:
            lists = lists + 1

    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()
