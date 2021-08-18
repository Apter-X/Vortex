from app.configs import database as config
from app.modules.database import Database
from app.modules.logger import Logger
from random import randint
import time


class Factory(Database):
    def __init__(self, engine=None):
        super().__init__(config.LOGIN)
        self.logger = Logger()
        self.engine = engine
        self.data = {}
        self.stage = {}

    def extract(self, current, end):
        while current <= end:
            request = self.engine.build_request(current)
            self.logger.info(f'Start extraction from page {current}')
            current += 1
            self.engine.suck_page(request)
            self.engine.set_links()
            for link in self.engine.links:
                request = self.engine.strategy.URL + link
                self.engine.suck_page(request)
                self.data = self.engine.map_by_strategy()
                print(self.data)
                # self.transform()
                # self.store_brute_data(self.data, self.engine.strategy.NAME)
                time.sleep(randint(1, 3))
        self.logger.warning('Extraction over')

    def transform(self):
        for table in self.engine.strategy.SCHEMA:
            for key in self.engine.strategy.SCHEMA[table]:
                self.stage[key] = self.data[key]
            self.load(table)
            self.stage = {}

        for table_assoc in self.engine.strategy.ASSOCIATIONS:
            for table in self.engine.strategy.ASSOCIATIONS[table_assoc]:
                assoc1 = self.ids[table]
                # self.stage = self.ids[table]
        print(self.stage)
        self.stage = {}
        self.ids = {}

    def load(self, table):
        self.ids[table] = self.store_data(table, self.stage, table+'_id')

    def elastic_pipe(self):
        path_desktop = self.logger.root[:-19]
        logstash_path = path_desktop + 'ElasticStack\\logstash-7.13.4\\bin\\logstash.bat'
        self.logger.execute_bat(logstash_path)

    def __del__(self):
        self.disconnect()
