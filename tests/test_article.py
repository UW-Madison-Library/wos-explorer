from wos_explorer.matchers import IdMatcher, PhraseMatcher
from wos_explorer.article_collection import ArticleCollection

def test_reference_parsing(single_article):
    assert single_article.references() is not None
    assert len(single_article.references()) == 8

def test_reference_parsing_when_empty(single_article_no_refs):
    assert single_article_no_refs.references() is not None
    assert len(single_article_no_refs.references()) == 0

def test_reference_list_parsing(single_article):
    assert single_article.reference_list() is not None
    assert len(single_article.reference_list()) == 7

def test_reference_list_parsing_when_empty(single_article_no_refs):
    assert single_article_no_refs.references() is not None
    assert len(single_article_no_refs.references()) == 0
