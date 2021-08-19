import os
import subprocess
import yaml


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


class System:
    def __init__(self):
        path = os.path.dirname(__file__)
        self.root = path[:-11]

    def load_file(self, path, from_root=False):
        if from_root:
            path = self.root + path
        with open(path) as file:
            return file

    def read_file(self, path, from_root=False):
        if from_root:
            path = self.root + path

        with open(path) as file:
            return file.read()

    def get_file_lines(self, path, from_root=False):
        if from_root:
            path = self.root + path

        with open(path) as file:
            lines = file.read().splitlines()
        return lines

    def read_yml(self, path, from_root=False):
        if from_root:
            path = self.root + path

        with open(path, 'r') as stream:
            try:
                yaml_file = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        return yaml_file

    def execute_bat(self, path, from_root=False):
        if from_root:
            path = self.root + path

        subprocess.call([fr'{path}'])
