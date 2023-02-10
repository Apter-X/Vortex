from modules.logger import Logger
import pandas as pd


def xls_to_csv(xls_path, csv_path):
    data_xls = pd.read_excel(xls_path)
    data_xls.to_csv(csv_path, encoding='utf-8', index=False)


def json_to_csv(json_path, csv_path):
    data_json = pd.read_json(json_path)
    data_json.to_csv(csv_path, encoding='utf-8', index=False)


class Data:
    def __init__(self):
        self.frame = pd.DataFrame
        self.log = Logger()

    def get_var(self, var):
        self.frame = pd.DataFrame([var])
        return self.frame

    def import_json(self, path):
        self.frame = pd.read_json(path,)
        return self.frame

    def import_csv(self, path):
        self.frame = pd.read_csv(path, low_memory=False)
        return self.frame

    def duplicate_data(self, n):
        duplicate = [pd.DataFrame()]
        while n > 0:
            duplicate.append(self.frame)
            n -= 1
        self.frame = pd.concat(duplicate)

    def concat_data(self, arr_data):
        arr_data.append(self.frame)
        self.frame = pd.concat(arr_data)

    def log_describe(self, includes='all'):
        describe = self.frame.describe(include=includes)
        self.log.info('Describe data... \n' + describe.to_string())

    def log_count_data(self):
        count_data = self.frame.count()
        self.log.info('Counting data... \n' + count_data.to_string())

    def log_isna_sum(self):
        sum_data = self.frame.isna().sum()
        self.log.info('Calculating the sum of "NaN" data... \n' + sum_data.to_string())

    def log_isnull_sum(self):
        sum_data = self.frame.isnull().sum()
        self.log.info('Calculating the sum of "NULL" data... \n' + sum_data.to_string())

    # Calculate mean of all the values of the column
    def log_mean_val(self, name):
        val = self.frame[name].mean()
        self.log.info(f'The mean of the column is: {val} rounded to {round(val)}')

    def log_types(self):
        all_types = self.frame.dtypes
        self.log.info('All types in data... \n' + all_types.to_string())

    def log_shape(self):
        shape = self.frame.shape
        self.log.info('Shape: ' + str(shape))

    def export_to_csv(self, path):
        self.frame.to_csv(path, encoding='utf-8', index=False)

    def export_to_json(self, path):
        self.frame.to_json(path)

    def export_to_xlsx(self, path):
        self.frame.to_excel(path)
