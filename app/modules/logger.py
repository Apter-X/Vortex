import yaml
import logging
import logging.config
import os


class Logger:
    def __init__(self):
        conf_path = os.path.dirname(__file__)
        conf_path = conf_path[:-7]
        conf_path = conf_path + "configs\\logconfig.yml"

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
