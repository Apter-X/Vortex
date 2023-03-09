import time
import datetime


def now():
    return datetime.datetime.now().date()


def to_date(t):
    return datetime.datetime.fromtimestamp(t)


def to_timestamp(t):
    return time.mktime(datetime.datetime.strptime(t, "%Y-%m-%d").timetuple())


def normalize_string(string):
    return string.replace('_', '').replace('-', '').replace(' ', '').replace('é', '').upper()


def first_dic_value(dic):
    return list(dic.values())[0]
