import json

class Article:

    def __init__(self, raw_json):
        self.data = json.loads(raw_json)

    def __getitem__(self, arg):
        return self.data[arg]

    def values(self):
        return self._collect_values(self.data, [])

    def matches(self, criteria):
        return criteria.matches(self)

    def _collect_values(self, contents, values):
        if isinstance(contents, dict):
            self._collect_values(list(contents.values()), values)
        elif isinstance(contents, list):
            for item in contents:
                self._collect_values(item, values)
        else:
            values.append(contents)
        return values
