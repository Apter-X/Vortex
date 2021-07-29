import yaml
import logging
import logging.config
import os


class Logger:
    def __init__(self):
        conf_path = os.path.dirname(__file__)
        conf_path = conf_path[:-7]
        conf_path = conf_path + "configs\\log.yml"

        with open(conf_path, 'r') as stream:
            try:
                self.config = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def initialize(self):
        logging.config.dictConfig(self.config)
        logging.info('All good!')
