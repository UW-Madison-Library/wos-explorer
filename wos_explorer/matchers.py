import re


class IdMatcher:

    def __init__(self, ids):
        self.ids = ids

    def matches(self, article):
        if article['id'] in self.ids:
            return True
        else:
            return False


class PhraseMatcher:

    def __init__(self, phrase):
        self.pattern = re.compile(phrase, re.IGNORECASE)

    def matches(self, article):
        for value in article.values():
            if (isinstance(value, str) and self.pattern.search(value)):
                return True
        return False
