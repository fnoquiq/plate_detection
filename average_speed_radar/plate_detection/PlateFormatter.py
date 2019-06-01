import re


def is_plate_format(string):
    return __is_contain_plate_size(string)


def __is_contain_plate_size(string):
    prog = re.compile('[A-Z]{3}[-][0-9]{4}')
    result = prog.search(string)

    if result is not None:
        return True
