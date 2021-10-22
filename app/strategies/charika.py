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
    'element': {'style': 'color:#D97B46'}
}
MAP = {
    'name': ['find', ['a', {'style': 'cursor: default; text-decoration: none'}]],
    'address': ['find', ['label', None]],
    'about': ['find', ['div', {'class': 'truncate-m'}]],
    'tel1': ['find_precisely', ['span', {'class': 'marketingInfoTelFax'}], 1],
    'tel2': ['find_precisely', ['span', {'class': 'marketingInfoTelFax'}], 2],
    'email': ['find_precisely', ['a', {'target': '_blank'}], 1],
    # 'website': ['find_precisely', ['a', {'target': '_blank'}], 2],
    'legal_form': ['find_precisely', ['td', {'class': 'col-xs-7 nopaddingleft'}], 2],
    'capital': ['find_precisely', ['td', {'class': 'col-xs-7 nopaddingleft'}], 3]
}

