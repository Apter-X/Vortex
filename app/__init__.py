from configs import database
from strategies import telecontact, charika
from modules.database import Database
from app.modules.vortex import Vortex


def main():
    vrt = Vortex(telecontact)
    request = vrt.build_request(1)
    vrt.suck_page(request)
    vrt.map_links()
    for link in vrt.links:
        print(link)


if __name__ == "__main__":
    main()
