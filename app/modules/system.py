import os
import subprocess
import yaml


class System:
    def __init__(self):
        path = os.path.dirname(__file__)
        self.root = path[:-7]

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
