from strategies import telecontact, charika
from app.modules.factory import Factory
from app.modules.vortex import Vortex
from helpers import regex


def main():
    factory = Factory()
    while True:
        print("__Menu Principal__ :")
        print("(1) - Débuter le Scraping")
        print("(2) - Consulter le fichier log")
        choice = input("Veuillez choisir le numéro correspondant : ")
        if choice == '1':
            print("__Menu Scraper__ :")
            print("(1) - Telecontact")
            print("(2) - Charika")
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
                print("Réponse incorrect ! Veuillez réessayer. (1)")
            if start_at and end_at:
                start_at = int(start_at)
                end_at = int(end_at)
                if type(start_at) is not int or type(end_at) is not int:
                    print("Réponse incorrect ! Veuillez réessayer. (2)")
                else:
                    engine = Vortex(base)
                    factory.__init__(engine)
                    factory.extract(start_at, end_at)
            else:
                print("Réponse incorrect ! Veuillez réessayer. (3)")

        elif choice == '2':
            print("__Menu Log__ :")
            print("Veuillez utiliser une \"regular expression\" afin d'affiner votre recherche.")
            print("N.B: Laissez ce champ vide pour consulter tout le fichier log.")
            print("Ex.: ([0-9]{4})-([0-1][0-9])-([0-3][0-9]).([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9]),"
                  "([0-9]{3}).-.(app.modules.logger).-.(DEBUG)")
            expression = input()
            factory.logger.find_all(expression)
        else:
            print("Réponse incorrect ! Veuillez réessayer. (4)")


if __name__ == '__main__':
    main()
