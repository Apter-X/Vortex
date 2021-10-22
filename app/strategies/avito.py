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
    'element': {'class': 'oan6tk-1 jkKPKg'}
}
MAP = {
    'br': ['find_precisely', ['span', {'class': 'sc-1x0vz2r-0 dVPTCB'}], 4],
    'md': ['find_precisely', ['span', {'class': 'sc-1x0vz2r-0 dVPTCB'}], 5],
    'yr': ['find_precisely', ['span', {'class': 'sc-1x0vz2r-0 dVPTCB'}], 3],
    'km': ['find_precisely', ['span', {'class': 'sc-1x0vz2r-0 dVPTCB'}], 2],
    'fl': ['find_precisely', ['span', {'class': 'sc-1x0vz2r-0 gEZokL'}], 0],
    'fp': ['find_precisely', ['span', {'class': 'sc-1x0vz2r-0 gEZokL'}], 1],
    'transmission': ['find_precisely', ['span', {'class': 'sc-1x0vz2r-0 gEZokL'}], 2],
    'pr': ['find', ['p', {'class': 'sc-1x0vz2r-0 dUNDMm'}]],
    'author': ['find', ['p', {'class': 'sc-1x0vz2r-0 fQAjsC sc-1ii0n73-5 dCqFdX'}]]
}
