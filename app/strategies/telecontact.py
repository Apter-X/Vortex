NAME = 'Telecontact'
URL = 'https://www.telecontact.ma'
PREFIX = '/trouver/index.php?'
QUERY_PARAMS = {
    'nxo': 'moteur',
    'nxs': 'process',
    'string': '',
    'ou': 'casablanca',
    'aproximite': '',
    'produit': ''
}
REQUEST_HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 '
                  'Safari/537.36 '
}
LINK = {
    'tag': 'a',
    'element': {'class': 'moodalbox'}
}
MAP = {
    'name': ['find_child', ['a', {'itemtype': 'https://schema.org/WebPage'}], ['span', {'itemprop': 'name'}]],
    'legal_form': ['find', ['td', {'class', 'forme_td'}]],
    'capital': ['find', ['td', {'class': 'capi_td'}]],
    'effective': ['find', ['td', {'class': 'effic_td'}]],
    'year': ['find', ['td', {'class', 'annee_creation_td'}]],
    'type': ['find', ['td', {'class', 'type_eta_td'}]],
    'website': ['get_href', ['a', {'class', 'btn-results-products'}]],
    'telephone': ['find_all', ['div', {'class', 'letel'}]],  # Need to be clean
    'address': ['find_precisely', ['div', {'class': 'col-xs-12'}], 5],
    'about': ['find', ['p', {'itemprop': 'description'}]],
    'services': ['find_all', ['a', {'class': 'rubrique-client'}]],
    'activities': ['find_all', ['a', {'style': 'margin:2px;font-size: 17px;'}]]
}
