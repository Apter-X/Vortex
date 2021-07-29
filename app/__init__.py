from configs import database
from strategies import telecontact, charika
from modules.database import Database
from app.modules.vortex import Vortex
from app.modules.logger import Logger
from random import randint
import time


def main():
    # db = Database(database.DATABASE)
    vrt = Vortex(telecontact)
    log = Logger()

    request = vrt.build_request(1)
    vrt.suck_page(request)
    vrt.set_links()
    for link in vrt.links:
        request = vrt.strategy.URL + link
        vrt.suck_page(request)
        data = vrt.map_by_strategy()
        # db.store_data(data, vrt.strategy.NAME)
        time.sleep(randint(1, 3))

    # db.fetch(""" SELECT * FROM companies """)
    # db.disconnect()


if __name__ == "__main__":
    main()
