import os
import json
import win32gui


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


def alter_window(hwnd, x=None, y=None, x_delta=None, y_delta=None,
                 width=None, height=None, width_delta=None, height_delta=None):
    bbox = win32gui.GetWindowRect(hwnd)
    window_x, window_y = bbox[0], bbox[1]

    new_x = x if x is not None else window_x + x_delta
    new_y = y if y is not None else window_y + y_delta
    new_width = width if width is not None else width + width_delta
    new_height = height if height is not None else height + height_delta
    if new_width < 10:
        new_width = 10
    if new_height < 10:
        new_height = 10
    
    win32gui.MoveWindow(hwnd, new_x, new_y, new_width, new_height, True)


def milliseconds_to_minute_format(milliseconds):
    raw_seconds = milliseconds / 1000
    minutes = int(raw_seconds / 60)
    seconds = int(raw_seconds - minutes * 60)
    return "{}:{}".format(minutes, str(int(seconds)).rjust(2, "0"))
