import time

user_config = {
    'name': "//span[@id='h-name']/text()",
    'gender': "//span[@id='h-gender']/@class",
    'level': "//a[@class='h-level m-level']/@lvl",
    'register_time': "//div[@class='item regtime']/span[@class='text']/text()",
    'location': "//div[@class='item geo']/span[@class='text guest']/text()"
}

extend_config = {
    'head_img': "//div[@class='h-avatar']/img/@src",
    'sign': "//div[@class='h-sign']/text()",
    'birthday': "//div[@class='item birthday']/span[@class='text guest']/text()",
    'follow_num': "//a[@class='item data-gz']/span[@class='quantity']/text()",
    'fans_num': "//a[@class='item data-fs']/span[@class='quantity space-fans']/text()"
}


def deal_user_info(data):

    for key in data.keys():
        try:
            func = "deal_" + str(key)
            data[key] = eval(func)(data[key])
        except Exception as e:
            print(key, e)
    return data


def deal_name(name):
    if name:
        return name
    else:
        return ''


def deal_gender(gender):
    if gender == 'icon gender male':
        return 1
    else:
        if gender == 'icon gender female':
            return 0
        else:
            return -1


def deal_level(level):
    if str(level).isdigit():
        return int(level)
    else:
        return 0


def deal_register_time(register_time):
    date_structs = str(register_time).replace("注册于 ", "").split('-')
    date_structs = map(int, date_structs)
    date_structs = tuple(date_structs) + (0, 0, 0, 0, 0, 0)
    return time.mktime(date_structs)


def deal_head_img(head_img):
    return head_img


def deal_sign(sign):
    return str(sign)


def deal_birthday(birthday):
    return birthday


def deal_follow_num(follow_num):
    if str(follow_num).isdigit():
        return int(follow_num)
    else:
        return 0


def deal_fans_num(fans_num):
    if str(fans_num).isdigit():
        return int(fans_num)
    else:
        return 0


def deal_location(location):
    return location

