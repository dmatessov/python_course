from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get("https://www.cbr.ru/scripts/XML_daily.asp?date_req=" + date)
    soup = BeautifulSoup(response.content, "xml")
    cur_from_nominal = 1
    cur_from_value = Decimal(1)
    cur_to_nominal = 1
    cur_to_value = Decimal(1)
    if cur_from != "RUR":
        cur_from_tag = soup.find("CharCode", text=cur_from)
        if cur_from_tag != None:
            cur_from_nominal = Decimal(cur_from_tag.find_next_siblings("Nominal")[0].text.replace(',','.'))
            cur_from_value = Decimal(cur_from_tag.find_next_siblings("Value")[0].text.replace(',','.'))

    cur_to_tag = soup.find("CharCode", text=cur_to)
    if cur_to_tag != None:
        cur_to_nominal = Decimal(cur_to_tag.find_next_siblings("Nominal")[0].text.replace(',','.'))
        cur_to_value = Decimal(cur_to_tag.find_next_siblings("Value")[0].text.replace(',','.'))

    result = Decimal(amount * (cur_to_nominal * cur_from_value)/(cur_from_nominal * cur_to_value)).quantize(cur_to_value)

    # Использовать переданный requests
    # ...
    #result = Decimal('3754.8057')
    return result  # не забыть про округление до 4х знаков после запятой
