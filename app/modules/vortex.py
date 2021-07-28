import urllib.parse
import requests
import logging
from app.modules.mapper import Mapper
from bs4 import BeautifulSoup


class Vortex(Mapper):
    def __init__(self, strategy):
        super().__init__(strategy)
        self.stats = {
            "num_results": 0
        }

    def build_request(self, page):
        request = self.strategy.URL
        if self.strategy.PREFIX:
            request += self.strategy.PREFIX

        if self.strategy.QUERY_PARAMS:
            request += urllib.parse.urlencode(self.strategy.QUERY_PARAMS)
            request += f"&page={page}"
        else:
            request += str(page)
        print(f"[+] request:{request}")
        return request

    def suck_page(self, request):
        rsp = ""
        try:
            rsp = requests.get(request, headers=self.strategy.REQUEST_HEADERS)
            if rsp.status_code != 200:
                raise (Exception("REQUEST FAILED WITH STATUS CODE {rsp.status_code}"))

        except Exception as e:
            print("Error while get page results", e)

        self.soup = BeautifulSoup(rsp.content, features="lxml")
