import requests
import datetime

ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'


def calc_age(uid):
    # на выходе получаем список пар (<возраст>, <количество друзей с таким возрастом>),
    # отсортированный по убыванию по второму ключу (количество друзей) и по возрастанию
    # по первому ключу (возраст). Например:
    # [(26, 8), (21, 6), (22, 6), (40, 2), (19, 1), (20, 1)]

    if not uid.isdigit():
        p1 = {'access_token': ACCESS_TOKEN, 'v': '5.71', 'user_ids': uid, 'name_case': 'nom'}
        r1 = requests.get('https://api.vk.com/method/users.get',p1)
        uid = r1.json().get('response')[0].get('id')

    p2 = {'access_token': ACCESS_TOKEN, 'v': '5.71', 'user_id': uid, 'fields': 'bdate'}
    r2 = requests.get('https://api.vk.com/method/friends.get',p2)
    friends = r2.json().get('response').get('items')

    now = datetime.datetime.now()
    resp = dict()

    for f in friends:
        bdate = f.get('bdate')
        if bdate is not None:
            if len(bdate) > 5:
                y = int(bdate[-4:])
                age = now.year - y;
                value = resp.get(age)
                if value is None:
                    value = 0
                resp[age] = value + 1
                # print(f.get('id'), )
    sorted_x = sorted(resp.items(), key=lambda kv: (kv[1], -kv[0]), reverse=True)
    return sorted_x

if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
