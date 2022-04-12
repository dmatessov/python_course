from bs4 import BeautifulSoup
from os import path
import re

PAGES_ACCESSIBLE = dict()
CONTIGUITY = dict()

def parse(path_to_file):
    f = open(path_to_file, 'r', encoding="utf-8")
    html = f.read()
    f.close()
    soup = BeautifulSoup(html, 'lxml')

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


def page_exists(path_, page):
    global PAGES_ACCESSIBLE
    res = PAGES_ACCESSIBLE.get(page)
    if res is None:
        res = path.exists(path.join(path_, page))
        PAGES_ACCESSIBLE.update({page: res})
    return res


def unroll_tree(node, tree):
    parent = tree.get(node)
    if parent is not None:
        return unroll_tree(parent, tree) + [node]
    else:
        return [node]


def get_contiguity(path_, page):
    global CONTIGUITY
    res = CONTIGUITY.get(page)
    if res is None:
        with open(path.join(path_, page), encoding="utf-8") as file:
            links = re.findall(r"(?<=/wiki/)[\w()]+", file.read())
            file.close()
        unique_links = set(links)
        accessible_links = list()
        for link in unique_links:
            if page_exists(path_, link) & (link != page):
                accessible_links.append(link)
        res = set(accessible_links)
        CONTIGUITY.update({page: res})
    return sorted(res)

def build_bridge(path_, start_page, end_page):
    """возвращает список страниц, по которым можно перейти по ссылкам со start_page на
    end_page, начальная и конечная страницы включаются в результирующий список"""
    # дерево узлов, добавляем в него начальный узел из которого будет поиск
    # нужно для того, чтобы потом построить последовательность между начальной и конечной страницами
    tree = dict()
    tree.update({start_page: None})

    found = False

    queue = list()
    queue.append(start_page)
    while queue:
        next_node = queue.pop(0)
        for node in get_contiguity(path_, next_node):

            if node == end_page:
                tree.update({node: next_node})
                found = True
                break
            else:
                if tree.get(node) is None:
                    tree.update({node: next_node})
                    queue.append(node)
            if found:
                break
    return unroll_tree(end_page, tree)


def get_statistics(path, start_page, end_page):
    """собирает статистику со страниц, возвращает словарь, где ключ - название страницы,
    значение - список со статистикой страницы"""

    # получаем список страниц, с которых необходимо собрать статистику
    pages = build_bridge(path, start_page, end_page)
    # напишите вашу реализацию логики по сбору статистики здесь
    statistic = dict()
    return statistic


# result = build_bridge('wiki/', 'The_New_York_Times', 'Stone_Age')
result = build_bridge('wiki/', 'The_New_York_Times', 'Woolwich')
print(result)

