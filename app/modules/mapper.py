import re


class Mapper:
    def __init__(self, schema):
        self.schema = schema
        self.map = self.schema['map']
        self.soup = None
        self.links = set()

    def set_links(self):
        results = self.soup.find_all(self.schema['link']["tag"], self.schema['link']["element"])
        for result in results:
            self.links.add(result.get("href"))
        try:
            self.links.remove('')
        except KeyError as e:
            print('No empty link found.', e)

    def map_by_schema(self):
        funcs = self.load_funcs()
        mapped_object = {}
        for target in self.map:
            if self.map[target][0] == "find_child":
                data = funcs[self.map[target][0]](self.map[target][1][0], self.map[target][1][1],
                                                  self.map[target][2][0], self.map[target][2][1])
                mapped_object[target] = data
            elif self.map[target][0] == "find_precisely" or self.map[target][0] == "find_regex":
                data = funcs[self.map[target][0]](self.map[target][1][0], self.map[target][1][1],
                                                  self.map[target][2])
                mapped_object[target] = data
            else:
                data = funcs[self.map[target][0]](self.map[target][1][0], self.map[target][1][1])
                mapped_object[target] = data
        if mapped_object:
            return mapped_object

    def load_funcs(self):
        stored_funcs = {
            'find': self.find,
            'find_child': self.find_child,
            'find_all': self.find_all,
            'get_href': self.get_href,
            'find_precisely': self.find_precisely,
            'find_regex': self.find_regex
        }
        return stored_funcs

    def find(self, tag, target):
        result = self.soup.find(tag, target)
        if result and result.text.strip():
            return result.text.strip()

    def find_child(self, tag, target, child_tag, child_target):
        result = self.soup.find(tag, target).findChild(child_tag, child_target)
        if result and result.text.strip():
            return result.text.strip()

    def find_all(self, tag, target):
        result = self.soup.find_all(tag, target)
        if result:
            map_data = ' '.join(map(lambda a: a.text.strip(), result))
            return map_data

    def get_href(self, tag, target):
        result = self.soup.find(tag, target)
        if result:
            return result.get("href")

    def get_value(self, tag, target):
        result = self.soup.find(tag, target)
        if result:
            return result.get("value")

    def find_precisely(self, tag, target, n):
        result = self.soup.find_all(tag, target)
        if result:
            map_data = map(lambda a: a.text.strip(), result)
            for i, data in enumerate(map_data):
                # print(i, data) # list all finds
                if i == n:
                    return data

    def find_regex(self, tag, target, regex):
        result = self.soup.find(tag, target)
        if result:
            match = re.search(regex, str(result))

            if match:
                try:
                    group = match.group(1)
                except IndexError as e:
                    group = match.group()
                return group
            else:
                return None
