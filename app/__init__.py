from strategies import telecontact, charika
from app.modules.factory import Factory
from app.modules.vortex import Vortex
from app.modules.logger import build_regex


def main():
    engine = Vortex(telecontact)
    factory = Factory('schema', engine)
    # factory.extract(1, 2)

    expression = build_regex("app.modules.logger")
    factory.logger.find_all(expression)


if __name__ == "__main__":
    main()
