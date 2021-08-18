from strategies import telecontact, charika
from app.modules.factory import Factory
from app.modules.vortex import Vortex
from helpers import regex


def main():
    factory = Factory()
    while True:
        print("*----------------------------------*")
        print("    + Menu Principal +")
        print("(1) - Débuter le Scraping")
        print("(2) - Consulter le fichier log")
        print("*----------------------------------*")
        choice = input("Veuillez choisir le numéro correspondant : ")
        if choice == '1':
            print("*----------------------------------*")
            print("    + Menu Scraper +")
            print("(1) - Telecontact")
            print("(2) - Charika")
            print("*----------------------------------*")
            choice = input("Veuillez choisir le numéro correspondant : ")
            base = None
            start_at = None
            end_at = None
            if choice == '1':
                base = telecontact
                start_at = input("A partir de la page : ")
                end_at = input("Jusqu'à la page : ")
            elif choice == '2':
                base = charika
                start_at = input("A partir de la page : ")
                end_at = input("Jusqu'à la page : ")
            else:
                print('\033[93m' + "Réponse incorrect ! Veuillez réessayer. (1)" + '\033[0m')
            if start_at and end_at:
                try:
                    start_at = int(start_at)
                    end_at = int(end_at)
                except ValueError:
                    print('\033[93m' + f"Réponse incorrect ! Veuillez réessayer. (2)" + '\033[0m')
                else:
                    engine = Vortex(base)
                    factory.__init__(engine)
                    factory.extract(start_at, end_at)
            else:
                print('\033[93m' + "Réponse incorrect ! Veuillez réessayer. (3)" + '\033[0m')

        elif choice == '2':
            print("*----------------------------------*")
            print("    + Menu log +")
            print("N.B: Laissez ce champ vide pour consulter tout le fichier log.")
            print("Ex.: ([0-9]{4})-([0-1][0-9])-([0-3][0-9]).([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9]),"
                  "([0-9]{3}).-.(app.modules.logger).-.(DEBUG)")
            print("*----------------------------------*")
            print("Veuillez utiliser une \"regular expression\" afin d'affiner votre recherche.")
            expression = input()
            factory.logger.find_all(expression)
        else:
            print('\033[93m' + "Réponse incorrect ! Veuillez réessayer. (4)" + '\033[0m')


if __name__ == '__main__':
    main()
