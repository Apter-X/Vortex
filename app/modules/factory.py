import time
import msvcrt
from datetime import datetime
from random import randint


class Factory:
    def __init__(self, logger, db, engine=None):
        self.logger = logger
        self.db = db
        self.engine = engine
        self.data = {}
        self.startTime = datetime.now()

    def start(self, current, end):
        try_count = 0
        while current <= end and try_count < 3:
            request = self.engine.build_request(current)
            self.logger.info(f'Start extraction from {self.engine.strategy.NAME} the page number {current}')
            current += 1
            self.engine.suck_page(request)
            self.engine.set_links()
            for link in self.engine.links:
                request = self.engine.strategy.URL + link
                self.engine.suck_page(request)
                self.data = self.engine.map.map_by_schema()
                self.logger.info(self.data)
                try:
                    self.db.store_brute_data(self.data, self.engine.strategy.NAME)
                    try_count = 0
                except Exception as e:
                    self.logger.error(e)
                    try_count += 1
                time.sleep(randint(1, 3))
            self.engine.links = set()
        self.logger.warning('Extraction over')

    def try_set_links(self, link):
        self.engine.suck_page(link)
        self.engine.set_links()
        print(self.engine.links)
        print(len(self.engine.links))

    def try_target(self, link):
        self.engine.suck_page(link)
        data = self.engine.map_by_strategy()
        print(data)

    def try_store_target(self, link):
        self.engine.suck_page(link)
        data = self.engine.map_by_strategy()
        self.db.store_brute_data(data, self.engine.strategy.NAME)
        print(data)

    def start_links_first(self, current, end):
        try_count = 0
        while current <= end and try_count < 3:
            request = self.engine.build_request(current)
            self.logger.info(f'Start extraction from {self.engine.strategy.NAME} the page number {current}')
            current += 1
            self.engine.suck_page(request)
            self.engine.set_links()
            print(len(self.engine.links))
            print(self.engine.links)

        for link in self.engine.links:
            request = self.engine.strategy.URL + link
            self.engine.suck_page(request)
            self.data = self.engine.map.map_by_schema()
            self.logger.info(self.data)
            try:
                self.db.store_brute_data(self.data, self.engine.strategy.NAME)
                try_count = 0
            except Exception as e:
                self.logger.error(e)
                try_count += 1
            time.sleep(randint(1, 3))
        self.engine.links = set()
        self.logger.warning('Extraction over')

    def watch(self, request):
        while True:
            try:
                self.engine.suck_page(request)
                self.engine.set_links()
                self.logger.info(f"Links: {len(self.engine.links)}")
                time.sleep(2)
            except Exception as e:
                self.logger.warning(e)
            except KeyboardInterrupt:
                print("[+] Saving links...")
                for link in self.engine.links:
                    self.logger.info(self.data)
                break

    def __del__(self):
        self.logger.info("Execution Time: {}".format(datetime.now() - self.startTime))
