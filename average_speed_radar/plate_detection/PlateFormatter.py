def is_plate_format(string):
    return __is_contain_plate_size(string)


def __is_contain_plate_size(string):
    if len(string) == 7 or len(string) == 8:
        return True
    return False
