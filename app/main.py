from settings import db, log
from modules import Vortex, Mapper, Factory, argv


def main():
    # engine = None
    # target = str(argv[1])
    # current = int(argv[2])
    # end = int(argv[3])
    #
    # if target == 'charika':
    #     engine = Vortex(charika)
    # elif target == 'telecontact':
    #     engine = Vortex(telecontact)
    # elif target == 'avito':
    #     engine = Vortex(avito)

    # factory = Factory(engine)
    # factory.start(current, end)
    # factory.try_target('https://www.avito.ma/fr/autre_secteur/voitures/Avito_Bi3_liya_Citroen_Berlingo_47465395.htm')
    schema = db.fetch("""SELECT * FROM schemas WHERE schemas_name = 'Avito'""")
    print(schema)
    exit(0)

    engine = Vortex
    mapper = Mapper(schema)


if __name__ == '__main__':
    main()
