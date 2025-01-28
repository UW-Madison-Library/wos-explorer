import re
from nltk.util import ngrams
from nltk import word_tokenize


class Query:

    def __init__(self, matchers, operator):
        self.matchers = matchers
        self.operator = operator

    def matches(self, article):
        individual_matches = [matcher.matches(article) for matcher in self.matchers]
        if (self.operator == "or"):
            return any(individual_matches)
        else:
            return all(individual_matches)


class IdMatcher:

    def __init__(self, ids):
        self.ids = ids

    def matches(self, article):
        if article['id'] in self.ids:
            return True
        else:
            return False


class PhraseMatcher:

    def __init__(self, phrase, fields = [], exclude_phrase = False):
        self.search_tokens  = [p if p[len(p) - 1] == "*" else p.strip() + "$" for p in phrase.split()]
        self.search_tokens  = [p[1:].strip() if p[0] == "*" else "^" + p.strip() for p in self.search_tokens]
        self.patterns       = [re.compile(search_str, re.IGNORECASE) for search_str in self.search_tokens]
        self.fields         = fields
        self.exclude_phrase = exclude_phrase

    def matches(self, article):
        values = article.values(self.fields)

        # Convert the document's fields into lists of words (simple whitespace split)
        article_terms = [word_tokenize(field_val) for field_val in values if field_val is not None]

        # For each set of words from each field being searched in the article...
        for term_set in article_terms:
            # Convert the words into n-grams sized according to the search phrase's token count
            n_grams = ngrams(term_set, len(self.patterns))

            # Search the document's n-gram items for matches against the search phrase's patterns. The n-gram tuple order
            # must match the phrase pattern order.
            if any([ all([self.patterns[i].search(g) for i, g in enumerate(gram)]) for gram in n_grams ]):
                return False if self.exclude_phrase else True

        # If this line is hit, no tuples matched, so the current document is not a match.
        return True if self.exclude_phrase else False


class AffiliationMatcher:

    def __init__(self, names, field = None):
        self.search_field = field if field is not None else "organizations"
        self.names = set(names)

    def matches(self, article):
        if article["addresses"] is not None:
            affil_addrs = filter(lambda addr: addr[self.search_field] is not None, article["addresses"])
            matches = set()
            for address in affil_addrs:
                if type(address[self.search_field]) == list:
                    matches.update(address[self.search_field])
                else:
                    matches.add(address[self.search_field])

            if len(self.names & matches) > 0:
                return True

        return False


class SourceTitleMatcher:

    def __init__(self, source_titles):
        self.source_titles = set([title.lower() for title in source_titles])

    def matches(self, article):
        if article["source_title"] is not None and article["source_title"].lower() in self.source_titles:
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


class IdentifierMatcher:

    def __init__(self, type, identifiers):
        self.type = type
        self.identifiers = set(identifiers)

    def matches(self, article):
        if article["identifiers"] is not None:
            type_identifiers = filter(lambda id: id["type"] == self.type, article["identifiers"])
            id_values = {type_identifier["value"] for type_identifier in type_identifiers}
            if len(self.identifiers & id_values) > 0:
                return True
        return False
