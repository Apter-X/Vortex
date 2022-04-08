import time
import msvcrt
from datetime import datetime
from random import randint

from modules.analyzer import Analyzer
from modules.database import Database
from modules.logger import Logger


class Factory(Database):
    def __init__(self, engine=None):
        super().__init__()
        self.logger = Logger()
        self.analyze = Analyzer()
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
                self.data = self.engine.map_by_strategy()
                self.logger.info(self.data)
                try:
                    self.analyze.append(link, self.data)
                    # self.store_brute_data(self.data, self.engine.strategy.NAME)
                    try_count = 0
                except Exception as e:
                    self.logger.error(e)
                    try_count += 1
                time.sleep(randint(1, 3))
            self.engine.links = set()
        self.analyze.save_to_csv('analyze_start.csv')
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
        self.store_brute_data(data, self.engine.strategy.NAME)
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
            self.data = self.engine.map_by_strategy()
            self.logger.info(self.data)
            try:
                self.analyze.append(link, self.data)
                # self.store_brute_data(self.data, self.engine.strategy.NAME)
                try_count = 0
            except Exception as e:
                self.logger.error(e)
                try_count += 1
            time.sleep(randint(1, 3))

        self.analyze.save_to_csv('analyze_start_links.csv')
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
                    self.analyze.append(link, self.data)
                self.analyze.save_to_csv('../data/auto_save_analyzer.csv')
                break

    def __del__(self):
        self.logger.info("Execution Time: {}".format(datetime.now() - self.startTime))
