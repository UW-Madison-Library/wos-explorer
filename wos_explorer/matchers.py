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


class AffiliationMatcher:

    def __init__(self, institution_names):
        self.names = set(institution_names)

    def matches(self, article):
        if article["addresses"] is not None:
            affil_addrs = filter(affiliated_address, [address for address in article["addresses"]])
            orgs = {org for address in affil_addrs for org in address["organizations"]}
            if len(self.names & orgs) > 0:
                return True
        return False

def affiliated_address(address):
    return address["organizations"] is not None
