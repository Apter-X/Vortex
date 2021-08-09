class Mapper:
    def __init__(self, strategy):
        self.strategy = strategy
        self.map = strategy.MAP
        self.soup = None
        self.links = set()

    def set_links(self):
        results = self.soup.find_all(self.strategy.LINK["tag"], self.strategy.LINK["element"])
        for result in results:
            self.links.add(result.get("href"))

    def map_by_strategy(self):
        funcs = self.load_funcs()
        mapped_object = {}
        for target in self.map:
            if self.map[target][0] == "find_child":
                data_child = funcs[self.map[target][0]](self.map[target][1][0], self.map[target][1][1],
                                                        self.map[target][2][0], self.map[target][2][1])
                mapped_object[target] = data_child
            else:
                data = funcs[self.map[target][0]](self.map[target][1][0], self.map[target][1][1])
                mapped_object[target] = data
        if mapped_object:
            return mapped_object

    def load_funcs(self):
        stored_funcs = {
            "find": self.find,
            "find_child": self.find_child,
            "find_all": self.find_all,
            "get_href": self.get_href,
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
