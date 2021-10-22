from strategies import telecontact, charika, avito
from modules.factory import Factory
from modules.vortex import Vortex
import sys


def main():
    engine = None
    target = str(sys.argv[1])
    current = int(sys.argv[2])
    end = int(sys.argv[3])

    if target == 'charika':
        engine = Vortex(charika)
    elif target == 'telecontact':
        engine = Vortex(telecontact)
    elif target == 'avito':
        engine = Vortex(avito)

    factory = Factory(engine)
    factory.start(current, end)
    # factory.try_target('https://www.avito.ma/fr/autre_secteur/voitures/Avito_Bi3_liya_Citroen_Berlingo_47465395.htm')


if __name__ == '__main__':
    main()
