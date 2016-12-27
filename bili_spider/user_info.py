def deal_name(name):
    return name


def deal_gender(gender):
    if gender == 'icon gender male':
        return 1
    else:
        if gender == 'icon gender female':
            return 0
        else:
            return -1


def deal_level(level):
    return int(level)

