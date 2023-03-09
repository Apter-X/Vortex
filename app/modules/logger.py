import logging
import logging.config
import re


class Logger:
    def __init__(self, config):
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

    """ lines = system.get_file_lines('loginfo.log', True) """
    def regex_log(self, lines, regular_expression):
        q = re.compile(regular_expression)
        for line in lines:
            key_val = q.findall(line)
            if key_val:
                self.results.append(line)
        return self.results
