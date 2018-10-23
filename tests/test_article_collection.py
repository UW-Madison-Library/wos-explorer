from wos_explorer.matchers import IdMatcher, PhraseMatcher
from wos_explorer.article_collection import ArticleCollection

def test_article_parsing(articles_sample):
    assert sum(1 for article in ArticleCollection(articles_sample)) == 10

def test_id_matching(articles_sample, output_filepath):
    ids = ["WOS:000251423400047", "WOS:000249481100010", "WOS:not-in-sample-set"]
    matches = ArticleCollection(articles_sample).select(IdMatcher(ids), output_filepath)
    assert sum(1 for article in matches) == 2
    assert sum(1 for line in open(output_filepath)) == len(ids) - 1

def test_case_insensitive_phrase_matching(articles_sample, output_filepath):
    matches = ArticleCollection(articles_sample).select(PhraseMatcher('baker'), output_filepath)
    assert sum(1 for article in matches) == 1

