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


class SourceTitleMatcher:

    def __init__(self, source_titles):
        self.source_titles = set(source_titles)

    def matches(self, article):
        if article["source_title"] is not None and article["source_title"] in self.source_titles:
            return True
        return  False


class CitationMatcher:

    def __init__(self, cited_articled_ids):
        self.cited_articled_ids = set(cited_articled_ids)

    def matches(self, article):
        reference_ids = [reference["id"] for reference in article.references()]
        if len( self.cited_articled_ids.intersection(reference_ids) ) > 0:
            return True
        else:
            return False
