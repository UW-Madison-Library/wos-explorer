from collections import defaultdict


class ReferenceList:

    def __init__(self):
        self.references = defaultdict(set)

    def __getitem__(self, arg):
        return self.references[arg]

    def __iter__(self):
        for year, ids in self.references.items():
            yield (year, ids)

    def __len__(self):
        return len(self.references)

    def ids(self):
        return {id for ids in self.references.values() for id in ids}

    def add(self, year, id):
        self.references[year].add(id)

    def years(self):
        return self.references.keys()
