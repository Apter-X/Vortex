import urllib.parse
import requests
from bs4 import BeautifulSoup


class Vortex:
    def __init__(self, mapper):
        self.map = mapper
        self.stats = {
            "num_results": 0
        }

    def build_request(self, page):
        request = self.map.schema.url
        if self.map.schema.prefix:
            request += self.map.schema.prefix

        if self.map.schema.queries:
            request += urllib.parse.urlencode(self.map.schema.queries)
            request += f"&page={page}"
        else:
            request += str(page)
        print(f"[+] request:{request}")
        return request

    def suck_page(self, request):
        rsp = ""
        try:
            rsp = requests.get(request, headers=self.map.schema['headers'])

            if rsp.status_code != 200:
                raise (Exception(f"REQUEST FAILED WITH STATUS CODE {rsp.status_code}"))
        except Exception as e:
            print("Error while get page results", e)

        self.map.soup = BeautifulSoup(rsp.content, features="lxml")
