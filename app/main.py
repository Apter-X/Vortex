import sys

from modules.factory import Factory
from modules.vortex import Vortex
from modules.data import Data
from modules.cleaner import Cleaner

from strategies import telecontact, charika, avito


def main():
    engine = Vortex(avito)
    # target = str(sys.argv[1])
    # current = int(sys.argv[2])
    # end = int(sys.argv[3])
    #
    # if target == 'charika':
    #     engine = Vortex(charika)
    # elif target == 'telecontact':
    #     engine = Vortex(telecontact)
    # elif target == 'avito':
    #     engine = Vortex(avito)

    factory = Factory(engine)
    # factory.start(current, end)
    # factory.try_target('https://www.avito.ma/fr/massira_2/voitures/Peugeot_207_diesel__49529496.htm')
    # factory.try_set_links('https://www.avito.ma/fr/maroc/v%C3%A9hicules-%C3%A0_vendre')

    # factory.start(1, 10)
    # factory.start_links_first(1, 10)

    # factory.watch('https://www.avito.ma/fr/maroc/voitures-à_vendre')

    clean = Cleaner()
    clean.data.import_csv('../data/auto_save_analyzer.csv')

    clean.data.log_count_data()
    clean.remove_duplicates(['Link'])
    clean.data.log_count_data()


if __name__ == '__main__':
    main()
