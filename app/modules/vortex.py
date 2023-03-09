import urllib.parse
import requests
from bs4 import BeautifulSoup


class Vortex:
    def __init__(self, mapper):
        self.map = mapper
        self.soup = None
        self.stats = {
            "num_results": 0
        }

    def build_request(self, page):
        request = self.map.strategy.URL
        if self.map.strategy.PREFIX:
            request += self.map.strategy.PREFIX

        if self.map.strategy.QUERY_PARAMS:
            request += urllib.parse.urlencode(self.map.strategy.QUERY_PARAMS)
            request += f"&page={page}"
        else:
            request += str(page)
        print(f"[+] request:{request}")
        return request

    def suck_page(self, request):
        rsp = ""
        try:
            rsp = requests.get(request, headers=self.map.strategy.REQUEST_HEADERS)
            if rsp.status_code != 200:
                raise (Exception(f"REQUEST FAILED WITH STATUS CODE {rsp.status_code}"))

        except Exception as e:
            print("Error while get page results", e)

        self.soup = BeautifulSoup(rsp.content, features="lxml")
