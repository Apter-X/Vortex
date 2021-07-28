NAME = "Charika"
URL = "https://charika.ma"
PREFIX = "/societes-"
QUERY_PARAMS = None
REQUEST_HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 "
                  "Safari/537.36 "
}
ARTICLE = {
    "tag": "div",
    "element": {"class": "panel-body"}
}
STRATEGY = {
    "name": ["find", ["a", {"class": "goto-fiche"}]],
    "address": ["find", ["label", None]],
    "description": ["find", ["div", {"class": "truncate-m"}]],
    "prestation": ["find_all", ["label", {"class": "truncate"}]]
}
