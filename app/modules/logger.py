import logging
import logging.config
from modules.system import System
import re


class Logger(System):
    def __init__(self):
        super().__init__()
        config = self.read_yml('configs/logconfig.yml', True)
        logging.config.dictConfig(config)
        self.log = logging.getLogger(__name__)
        self.results = []

    def debug(self, msg):
        self.log.debug(msg)

    def info(self, msg):
        self.log.info(msg)

    def warning(self, msg):
        self.log.warning(msg)

    def error(self, msg):
        self.log.error(msg)

    def critical(self, msg):
        self.log.critical(msg)

    def find_all(self, regular_expression):
        lines = self.get_file_lines('loginfo.log', True)
        q = re.compile(regular_expression)
        for line in lines:
            key_val = q.findall(line)
            if key_val:
                self.results.append(line)
                print(line)
