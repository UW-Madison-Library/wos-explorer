import json
from .reference_list import ReferenceList


class Article:

    def __init__(self, raw_json):
        self.data = json.loads(raw_json)

    def __getitem__(self, arg):
        return self.data[arg]

    def values(self, fields = []):
        if len(fields) == 0:
            return self._collect_values(self.data, [])
        else:
            data = dict()
            for field in fields:
                data[field] = self.data[field]
            return self._collect_values(data, [])

    def matches(self, criteria):
        return criteria.matches(self)

    def references(self):
        return [] if self['references'] is None else self['references']

    def reference_list(self):
        reflist = ReferenceList()
        for reference in self.references():
            year = reference['year'] if reference['year'] is not None else ''
            id   = reference['id']   if reference['id']   is not None else ''
            reflist.add(year, id)
        return reflist

    def _collect_values(self, contents, values):
        if isinstance(contents, dict):
            self._collect_values(list(contents.values()), values)
        elif isinstance(contents, list):
            for item in contents:
                self._collect_values(item, values)
        else:
            if contents is not None:
                values.append(str(contents))
        return values
