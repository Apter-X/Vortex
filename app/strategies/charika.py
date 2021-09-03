NAME = 'Charika'
URL = 'https://charika.ma/'
PREFIX = 'societes-'
QUERY_PARAMS = None
REQUEST_HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 '
                  'Safari/537.36 '
}
LINK = {
    'tag': 'a',
    'element': {'class': 'goto-fiche'}
}
MAP = {
    'name': ['find', ['a', {'class': 'goto-fiche'}]],
    'address': ['find', ['label', None]],
    'description': ['find', ['div', {'class': 'truncate-m'}]],
    'tel1': ['find_precisely', ['div', {'class': 'col-sm-11 col-xs-11 nopadding'}], 1],
    'fax': ['find_precisely', ['div', {'class': 'col-sm-11 col-xs-11 nopadding'}], 2],
    'email': ['find_precisely', ['div', {'class': 'col-sm-11 col-xs-11 nopadding'}], 3],
    'legal_form': ['find_precisely', ['td', {'class': 'col-xs-7 nopaddingleft'}], 2],
    'capital': ['find_precisely', ['td', {'class': 'col-xs-7 nopaddingleft'}], 3]
}
