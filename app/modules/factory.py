import time
from datetime import datetime
from random import randint


class Factory:
    def __init__(self, logger, db, engine=None):
        self.logger = logger
        self.db = db
        self.engine = engine
        self.data = {}
        self.startTime = datetime.now()
        self.stats = {
            "num_results": 0
        }

    def start(self, current, end, base=1):
        try_count = 0
        while current <= end and try_count < 3:
            request = self.engine.build_request(current)
            self.logger.info(f"Start extraction from {self.engine.map.schema['name']} the page number {current}")
            self.engine.suck_page(request)
            self.engine.map.set_links()
            for link in self.engine.map.links:
                request = self.engine.map.schema['url'] + str(link).replace(self.engine.map.schema['url'], '')
                try:
                    self.engine.suck_page(request)
                except Exception as e:
                    self.logger.error('Error while get page results ' + str(e))

                self.data = self.engine.map.map_by_schema()
                self.logger.info(self.data)
                try:
                    # self.db.store_brute_data(self.data, self.engine.schema.name, link)
                    try_count = 0
                except Exception as e:
                    self.logger.error(e)
                    try_count += 1
                time.sleep(randint(1, 3))
            self.engine.links = set()
            current += base

        if try_count > 2:
            self.logger.error('An error occurred while scraping!')
        else:
            self.logger.info('Extraction over successfully.')

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

    def try_set_links(self, link):
        self.engine.suck_page(link)
        self.engine.map.set_links()
        print(self.engine.map.links)
        print(len(self.engine.map.links))

    def try_target(self, link):
        self.engine.suck_page(link)
        data = self.engine.map.map_by_schema()
        print(data)

    def try_store_target(self, link):
        self.engine.suck_page(link)
        data = self.engine.map.map_by_schema()
        self.db.store_brute_data(data, self.engine.map.schema['name'])
        print(data)

    def __del__(self):
        self.logger.info("Execution Time: {}".format(datetime.now() - self.startTime))
