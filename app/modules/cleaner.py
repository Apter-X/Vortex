from modules.logger import Logger
from modules.data import Data
import unicodedata
import re
import numpy as np
import pandas as pd
import operator


def cast_int(x):
    try:
        return int(x)
    except Exception as e:
        x = re.sub('\s|\D', '', x)
        return int(x)


def get_mileage(km):
    try:
        km_min, km_max = str(km).replace(' ', '').split('-')
        mil = int((int(km_max) - int(km_min)) * np.random.rand(1)) + int(km_min)
        return int(mil)
    except Exception as e:
        return int(600000)


def get_date(date):
    date = date.split('T')[0]
    return pd.to_datetime(date)


def get_year(date):
    year = pd.to_datetime(date, format='%Y')
    return year


def get_age(date):
    age = round(date.days / 365, 1)
    return age


class Cleaner:
    def __init__(self, data=None):
        self.log = Logger()
        if data:
            self.data = data
        else:
            self.data = Data()

    # normalize textual column
    def normalize_text(self, arr_labels, unicode="NFC"):
        for n in arr_labels:
            try:
                self.data.frame[n] = self.data.frame[n].map(lambda x: unicodedata.normalize(unicode, x).upper())
            except Exception as e:
                self.log.error(e)

    # remove irrelevant features
    def remove_features(self, arr_labels):
        try:
            self.data.frame = self.data.frame.drop(arr_labels, axis=1)
        except Exception as e:
            self.log.error(e)

    def keep_features(self, arr_labels):
        try:
            self.data.frame.drop(self.data.frame.columns.difference(arr_labels), 1, inplace=True)
        except Exception as e:
            self.log.error(e)

    # remove the duplicates
    def remove_duplicates(self, arr_labels, keep="first"):
        try:
            self.data.frame = self.data.frame.drop_duplicates(arr_labels, keep=keep)
        except Exception as e:
            self.log.error(e)

    def remove_na(self):
        try:
            self.data.frame.dropna(inplace=True)
        except Exception as e:
            self.log.error(e)

    def replace_values(self, arr_values, new_value):
        for v in arr_values:
            try:
                self.data.frame.replace({v: new_value}, inplace=True)
            except Exception as e:
                self.log.error(e)

    def replace_str(self, arr_labels, arr_str, new_str):
        for n in arr_labels:
            for s in arr_str:
                try:
                    self.data.frame[n] = self.data.frame[n].map(lambda x: x.replace(s, new_str))
                except Exception as e:
                    self.log.error(e)

    def rename_column(self, obj_names):
        try:
            self.data.frame.rename(columns=obj_names, inplace=True)
        except Exception as e:
            self.log.error(e)

    def sort_data(self, by, ascending=False):
        try:
            self.data.frame = self.data.frame.sort_values(by=by, ascending=ascending)
        except Exception as e:
            self.log.error(e)

    def convert(self, arr_labels, new_type):
        for n in arr_labels:
            try:
                self.data.frame[n] = self.data.frame[n].astype(new_type)
            except Exception as e:
                self.log.error(e)

    def apply_axis_rule(self, new_label, rule):
        try:
            self.data.frame[new_label] = self.data.frame.apply(rule, axis=1)
        except Exception as e:
            self.log.error(e)

    def apply_rule(self, label, rule, new_label=None):
        if new_label:
            try:
                self.data.frame[new_label] = self.data.frame[label].apply(rule)
            except Exception as e:
                self.log.error(e)
        else:
            for n in label:
                try:
                    self.data.frame[n] = self.data.frame[n].apply(rule)
                except Exception as e:
                    self.log.error(e)

    def merge_data(self, new_data, on, how="outer"):
        try:
            self.data.frame = self.data.frame.merge(new_data, on=on, how=how)
        except Exception as e:
            self.log.error(e)

    def remove_by_condition(self, condition):
        try:
            self.data.frame.drop(self.data.frame[condition].index, inplace=True)
        except Exception as e:
            self.log.error(e)

    def keep_by_condition(self, condition):
        try:
            self.data.frame = self.data.frame[condition]
        except Exception as e:
            self.log.error(e)

    def keep_what_is_in(self, arr_values, on):
        try:
            self.data.frame = self.data.frame[self.data.frame[on].isin(arr_values)]
        except Exception as e:
            self.log.error(e)

    def round_data(self, arr_labels, by=None):
        for n in arr_labels:
            try:
                self.data.frame[n] = round(self.data.frame[n], by)
            except Exception as e:
                self.log.error(e)

    def operator_feat(self, a, b, operation, new_label):
        switcher = {
            "add": operator.add,
            "sub": operator.sub,
            "mul": operator.mul,
            "div": operator.truediv
        }
        op = switcher.get(operation, "Invalid operator")
        try:
            self.data.frame[new_label] = op(self.data.frame[a], self.data.frame[b])
        except:
            try:
                self.data.frame[new_label] = op(self.data.frame[a], b)
            except Exception as e:
                self.log.error(e)

    def map_data(self, mapper, label_1, label_2=None):
        mapper = mapper.astype(str)  # stringify <null> data to compare "=="
        if label_2:
            for old_1, old_2, new_1, new_2 in zip(mapper[mapper.columns[0]], mapper[mapper.columns[1]],
                                                  mapper[mapper.columns[2]], mapper[mapper.columns[3]]):
                self.data.frame.loc[(self.data.frame[label_1] == old_1)
                                    & (self.data.frame[label_2] == old_2), label_1] = new_1
                self.data.frame.loc[(self.data.frame[label_1] == new_1)
                                    & (self.data.frame[label_2] == old_2), label_2] = new_2
        else:
            for old, new in zip(mapper[mapper.columns[0]], mapper[mapper.columns[1]]):
                self.data.frame.loc[(self.data.frame[label_1] == old), label_1] = new
        self.replace_values(['nan'], np.nan)  # reestablish stringified nan to <null>

    def remove_by_number(self, arr_label, min_model):
        model_freq = self.data.frame.groupby(arr_label).size().reset_index(name='nb')
        self.data.frame = self.data.frame.merge(model_freq, on=arr_label)
        self.data.frame = self.data.frame[self.data.frame['nb'] > min_model]
        self.data.frame = self.data.frame.drop(['nb'], axis=1)
