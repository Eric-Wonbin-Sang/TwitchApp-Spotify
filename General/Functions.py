import os
import json


def str_to_length(base_str, length, do_dots=True):
    ret_str = base_str.ljust(length)[:length]
    if do_dots and len(base_str) + 3 >= length:
        return ret_str[:-3] + "..."
    return ret_str


def get_curr_parent_dir():
    return os.path.dirname(os.getcwd()).replace("\\", "/")


def parse_json(json_path):
    if not os.path.exists(json_path):
        raise FileExistsError
    with open(json_path) as f:
        return json.load(f)


def get_pretty_time(some_datetime):
    return some_datetime.strftime("%Y/%m/%d %I:%M%p")


def tab_str(some_str, tab_count):
    return ("\t" * tab_count) + some_str.replace("\n", "\n" + ("\t" * tab_count))
