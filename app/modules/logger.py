import logging
import logging.config
import os


class Logger:
    def __init__(self):
        path = os.path.dirname(__file__)
        root_path = path[:-7]
        conf_path = root_path + "configs\\logconfig.yml"
        self.log_path = root_path + "loginfo.log"

        with open(conf_path, 'r') as stream:
            try:
                config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
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
        with open(self.log_path) as fp:
            lines = fp.read().splitlines()

        q = re.compile(regular_expression)
        for line in lines:
            key_val = q.findall(line)
            if key_val:
                print(line)
