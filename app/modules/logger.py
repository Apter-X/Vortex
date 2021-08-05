import logging
import logging.config
from app.modules.system import System
import re

# ([0-9]{4})-([0-1][0-9])-([0-3][0-9]).([0-1][0-9]|[2][0-3]):
# ([0-5][0-9]):([0-5][0-9]),([0-9]{3}).-.(urllib3.connectionpool).-.(DEBUG)
def build_regex(name, level, y=None, m=None, d=None, h=None, mi=None, s=None, ms=None):
    expression = "("
    if y:
        expression += y
    else:
        expression += "[0-9]{4}"
    expression += ")-("
    if m:
        expression += m
    else:
        expression += "[0-1][0-9]"
    expression += ")-("
    if d:
        expression += d
    else:
        expression += "[0-3][0-9]"
    expression += ").("
    if h:
        expression += h
    else:
        expression += "[0-1][0-9]|[2][0-3]"
    expression += "):("
    if mi:
        expression += mi
    else:
        expression += "[0-5][0-9]"
    expression += "):("
    if s:
        expression += s
    else:
        expression += "[0-5][0-9]"
    expression += "),("
    if ms:
        expression += ms
    else:
        expression += "[0-9]{3}"
    expression += ").-.("
    expression += name
    expression += ").-.("
    expression += level
    expression += ")"

    return expression


class Logger(System):
    def __init__(self):
        super().__init__()
        config = self.read_yml("configs\\logconfig.yml", True)
        logging.config.dictConfig(config)
        self.log = logging.getLogger(__name__)

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
        lines = self.get_file_lines("loginfo.log", True)
        q = re.compile(regular_expression)
        for line in lines:
            key_val = q.findall(line)
            if key_val:
                print(line)
