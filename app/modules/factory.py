from app.modules.database import Database
from app.modules.logger import Logger
from random import randint
import time


class Factory(Database):
    def __init__(self, engine=None):
        super().__init__()
        self.logger = Logger()
        self.engine = engine
        self.data = {}

    def start(self, current, end):
        while current <= end:
            request = self.engine.build_request(current)
            self.logger.info(f'Start extraction from {self.engine.strategy.NAME} the page number {current}')
            current += 1
            self.engine.suck_page(request)
            self.engine.set_links()
            for link in self.engine.links:
                request = self.engine.strategy.URL + link
                self.engine.suck_page(request)
                self.data = self.engine.map_by_strategy()
                self.store_brute_data(self.data, self.engine.strategy.NAME)
                self.logger.info(self.data)
                time.sleep(randint(1, 3))
            self.engine.links = set()
        self.logger.warning('Extraction over')

    def try_target(self, link):
        self.engine.suck_page(link)
        data = self.engine.map_by_strategy()
        print(data)

    def __del__(self):
        self.disconnect()
