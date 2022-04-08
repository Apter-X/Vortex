import pandas as pd
from datetime import datetime


class Analyzer:
    def __init__(self):
        self.frame = pd.DataFrame(columns=('Time', 'Link', 'Data'))

    def append(self, link,  data):
        local = datetime.now()
        to_append = {'Time': local.strftime("%m/%d/%Y - %H:%M:%S"),
                     'Link': link, 'Data': [data]}
        to_append = pd.DataFrame(to_append)

        self.frame = self.frame.append(to_append, ignore_index=True)

    def save_to_csv(self, path):
        self.frame.to_csv(path)
