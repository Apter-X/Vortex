NAME = 'Avito'
URL = ''
PREFIX = 'https://www.avito.ma/fr/maroc/voitures-à_vendre?o='
QUERY_PARAMS = None
REQUEST_HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 '
                  'Safari/537.36 '
}
LINK = {
    'tag': 'a',
    'element': {'class': 'oan6tk-1 iZTmPK'}
}
MAP = {
    'br': ['find_regex', ['script', {'id': '__NEXT_DATA__'}],
           '"key":"brand","label":"Marque","value":"(.+?)"'],
    'md': ['find_regex', ['script', {'id': '__NEXT_DATA__'}],
           '"key":"model","label":"Modèle","value":"(.+?)"'],
    'yr': ['find_regex', ['script', {'id': '__NEXT_DATA__'}],
           '"key":"regdate","label":"Année-Modèle","value":"(.+?)"'],
    'km': ['find_regex', ['script', {'id': '__NEXT_DATA__'}],
           '"key":"mileage","label":"Kilométrage","value":"(.+?)"'],
    'fl': ['find_regex', ['script', {'id': '__NEXT_DATA__'}],
           '"key":"fuel","label":"Type de carburant","value":"(.+?)"'],
    'fp': ['find_regex', ['script', {'id': '__NEXT_DATA__'}],
           '"key":"pfiscale","label":"Puissance fiscale","value":"(.+?) CV"'],
    'transmission': ['find_regex', ['script', {'id': '__NEXT_DATA__'}],
                     '"key":"bv","label":"Boite de vitesses","value":"(.+?)"'],
    'pr': ['find_regex', ['script', {'id': '__NEXT_DATA__'}],
           '"price":\\{"value":([0-9]+?),'],
    'pt': ['find_regex', ['script', {'id': '__NEXT_DATA__'}],
           '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}'],
    'ph': ['find_regex', ['script', {'id': '__NEXT_DATA__'}],
           '"phone":"([05|06|07][\\d]*)",|"phone": "([05|06|07][\\d]*)",'],
    'doors': ['find_regex', ['script', {'id': '__NEXT_DATA__'}],
              '"key":"doors","label":"Nombre de portes","value":"(.+?)"'],
    'origin': ['find_regex', ['script', {'id': '__NEXT_DATA__'}],
               '"key":"v_origin","label":"Origine","value":"(.+?)"'],
    'first_owner': ['find_regex', ['script', {'id': '__NEXT_DATA__'}],
                    '"key":"first_owner","label":"Première main","value":"(.+?)"']
}
