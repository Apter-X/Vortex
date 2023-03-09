from app.modules.system import clear
from app.modules.factory import Factory
from app.modules.vortex import Vortex
from app.strategies import telecontact, charika

factory = Factory()

while True:
    clear()
    print("*----------------------------------*")
    print("    + Menu Principal +")
    print("(1) - Débuter le Scraping")
    print("(2) - Consulter le fichier log")
    print("(3) - Quitter")
    print("*----------------------------------*")
    choice = input("Veuillez choisir le numéro correspondant : ")
    if choice == '1':
        clear()
        print("*----------------------------------*")
        print("    + Menu Scraper +")
        print("(1) - Telecontact")
        print("(2) - Charika")
        print("(3) - Retour")
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
        elif choice == '3':
            pass
        else:
            print('\033[93m' + "Réponse incorrect ! Veuillez réessayer. (1)" + '\033[0m')
            input()
        if start_at and end_at:
            try:
                start_at = int(start_at)
                end_at = int(end_at)
            except ValueError:
                print('\033[93m' + f"Réponse incorrect ! Veuillez réessayer. (2)" + '\033[0m')
                input()
            else:
                clear()
                engine = Vortex(base)
                factory.__init__(engine)
                factory.start(start_at, end_at)
                input()

    elif choice == '2':
        clear()
        print("*----------------------------------*")
        print("    + Menu log +")
        print("(1) - Afficher le fichier log")
        print("(2) - Chercher par expression lambda")
        print("(3) - Retour")
        print("*----------------------------------*")
        choice = input("Veuillez choisir le numéro correspondant : ")
        if choice == '1':
            factory.logger.find_all('')
            input()
        elif choice == '2':
            print("Ex.: ([0-9]{4})-([0-1][0-9])-([0-3][0-9]).([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9]),"
                  "([0-9]{3}).-.(app.modules.logger).-.(DEBUG)")
            print("Veuillez utiliser une expression lambda afin d'affiner votre recherche.")
            expression = input()
            factory.logger.find_all(expression)
            input()
        elif choice == '3':
            pass
        else:
            print('\033[93m' + "Réponse incorrect ! Veuillez réessayer. (3)" + '\033[0m')
            input()
    elif choice == '3':
        break
    else:
        print('\033[93m' + "Réponse incorrect ! Veuillez réessayer. (4)" + '\033[0m')
        input()
