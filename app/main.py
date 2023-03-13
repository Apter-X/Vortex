from settings import db, factory, Vortex, Mapper, argv


def main():
    if len(argv) > 1:
        target = str(argv[1])
        current = int(argv[2])
        end = int(argv[3])
    else:
        target = "avito"
        current = 1
        end = 30

    schema_record = db.fetch_assoc(f"""SELECT * FROM schemas WHERE schemas_name = '{target.title()}'""")

    schema = {
        "name": schema_record.schemas_name,
        "url": schema_record.schemas_url,
        "prefix": schema_record.schemas_url_prefix,
        "queries": schema_record.schemas_query_params,
        "headers": schema_record.schemas_request_headers,
        "link": schema_record.schemas_link,
        "map": schema_record.schemas_map,
        "base": schema_record.schemas_base
    }

    mapper = Mapper(schema)
    engine = Vortex(mapper)
    factory.engine = engine
    factory.start(current, end, schema['base'])
    # factory.try_set_links("https://www.moteur.ma/fr/voiture/achat-voiture-occasion/")
    # factory.try_target("https://www.moteur.ma/fr/voiture/achat-voiture-occasion/detail-annonce/417911/nissan-micra-.html")


if __name__ == '__main__':
    main()
