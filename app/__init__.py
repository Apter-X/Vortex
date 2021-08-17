from strategies import telecontact, charika
from app.modules.factory import Factory
from app.modules.vortex import Vortex
from helpers import regex


def main():
    engine = Vortex(telecontact)
    factory = Factory(engine)
    factory.extract(1, 1)


if __name__ == '__main__':
    main()
