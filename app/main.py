from settings import db, factory, Vortex, Mapper, argv


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

    schema_record = db.fetch_assoc("""SELECT * FROM schemas WHERE schemas_name = 'Avito'""")

    schema = {
        "name": schema_record.schemas_name,
        "url": schema_record.schemas_url,
        "prefix": schema_record.schemas_url_prefix,
        "queries": schema_record.schemas_query_params,
        "headers": schema_record.schemas_request_headers,
        "link": schema_record.schemas_link,
        "map": schema_record.schemas_map
    }

    mapper = Mapper(schema)
    engine = Vortex(mapper)
    factory.engine = engine
    # factory = Factory(engine)
    # factory.start(current, end)
    factory.try_target("https://www.avito.ma/fr/yacoub_el_mansour/voitures_d'occasion/Volkswagen_touareg_Diesel_2016_52023842.htm")


if __name__ == '__main__':
    main()
