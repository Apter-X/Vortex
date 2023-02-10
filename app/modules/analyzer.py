import pandas as pd
from datetime import datetime
from modules.cleaner import Cleaner


class Analyzer:
    def __init__(self):
        self.frame = pd.DataFrame(columns=('Time', 'Link', 'Data'))
        self.clean = Cleaner

    def append(self, link,  data):
        local = datetime.now()
        to_append = {'Time': local.strftime("%m/%d/%Y - %H:%M:%S"),
                     'Link': link, 'Data': [data]}
        to_append = pd.DataFrame(to_append)

        self.frame = self.frame.append(to_append, ignore_index=True)

    def save_to_csv(self, path):
        self.clean.data.frame = self.frame
        self.clean.remove_duplicate()
        self.clean.data.frame.export_to_csv(path)
