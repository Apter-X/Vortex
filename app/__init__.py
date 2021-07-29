from configs import database
from strategies import telecontact, charika
from modules.database import Database
from app.modules.vortex import Vortex
from random import randint
import time


def main():
    db = Database(database.DATABASE)
    vrt = Vortex(telecontact)

    request = vrt.build_request(1)
    vrt.suck_page(request)
    vrt.map_links()
    for link in vrt.links:
        request = telecontact.URL + link
        vrt.suck_page(request)
        data = vrt.map_by_strategy()
        print(data)
        db.store_data(data, telecontact.NAME)
        time.sleep(randint(1, 3))

    db.fetch(""" SELECT * FROM companies """)
    db.disconnect()


if __name__ == "__main__":
    main()
