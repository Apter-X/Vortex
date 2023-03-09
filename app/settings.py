import os
from pathlib import Path

from modules.system import System, BColors, clear, argv
from modules.logger import Logger
from modules.database import Database
from modules.mapper import Mapper
from modules.vortex import Vortex
from modules.factory import Factory

from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
system = System(str(BASE_DIR))

config = system.read_yml('/configs/logconfig.yml', from_root=True)
log = Logger(config)

db = Database({
    'host': os.environ.get('HOST'),
    'database': os.environ.get('DATABASE'),
    'user': os.environ.get('USER'),
    'password': os.environ.get('PASSWORD'),
    'port': os.environ.get('PORT')
})

factory = Factory(log, db)
