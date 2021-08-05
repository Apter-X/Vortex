from configs import database
from strategies import telecontact, charika
from modules.database import Database
from app.modules.vortex import Vortex
from app.modules.system import System
from app.modules.logger import Logger, build_regex
from random import randint
import time


def main():
    # db = Database(database.DATABASE)
    vrt = Vortex(telecontact)
    log = Logger()

    # sys = System()
    # path_desktop = sys.root[:-19]
    # logstash_path = path_desktop + "ElasticStack\\logstash-7.13.4\\bin\\logstash.bat"
    # sys.execute_bat(logstash_path)

    # expression = build_regex("urllib3.connectionpool", "DEBUG")
    # print(expression)
    # log.find_all(expression)

    # request = vrt.build_request(1)
    # vrt.suck_page(request)
    # vrt.set_links()
    # for link in vrt.links:
    #     request = vrt.strategy.URL + link
    #     vrt.suck_page(request)
    #     data = vrt.map_by_strategy()
        # db.store_data(data, vrt.strategy.NAME)
        # time.sleep(randint(1, 3))

    # db.fetch(""" SELECT * FROM businesses """)
    # db.disconnect()


if __name__ == "__main__":
    main()
