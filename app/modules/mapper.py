from regex import regex as re


class Mapper:
    def __init__(self, schema):
        self.schema = schema
        self.map = schema.MAP
        self.soup = None
        self.links = set()

    def set_links(self):
        results = self.soup.find_all(self.schema.LINK["tag"], self.schema.LINK["element"])
        for result in results:
            self.links.add(result.get("href"))

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
            matches = re.finditer(regex, str(result))
            for matchNum, match in enumerate(matches, start=1):
                try:
                    return match.group(1)
                except Exception as e:
                    return match.group()
                # print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum,
                #                                                                     start=match.start(),
                #                                                                     end=match.end(),
                #                                                                     match=match.group()))
                #
                # for groupNum in range(0, len(match.groups())):
                #     groupNum = groupNum + 1
                #
                #     print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
                #                                                                     start=match.start(groupNum),
                #                                                                     end=match.end(groupNum),
                #                                                                     group=match.group(groupNum)))
