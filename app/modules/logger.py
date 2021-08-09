import logging
import logging.config
from app.modules.system import System
import re


def build_regex(name, level='DEBUG|INFO|WARNING|ERROR|CRITICAL', y='[0-9]{4}', m='[0-1][0-9]', d='[0-3][0-9]',
                h='[0-1][0-9]|[2][0-3]', mi='[0-5][0-9]', s='[0-5][0-9]', ms='[0-9]{3}'):
    expression = '('
    expression += y
    expression += ')-('
    expression += m
    expression += ')-('
    expression += d
    expression += ').('
    expression += h
    expression += '):('
    expression += mi
    expression += '):('
    expression += s
    expression += '),('
    expression += ms
    expression += ').-.('
    expression += name
    expression += ').-.('
    expression += level
    expression += ')'
    return expression


class Logger(System):
    def __init__(self):
        super().__init__()
        config = self.read_yml('configs\\logconfig.yml', True)
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
