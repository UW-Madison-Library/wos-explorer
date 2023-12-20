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

def test_get_custom_values_list(single_article):
    print(single_article.values(["title", "keywords"]))
    custom_values = ["Synthesis and colloid-chemical properties of new quaternary ammonium compounds", "SURFACTANTS"]
    assert single_article.values(["title", "keywords"]) == custom_values

def test_get_doi(single_article):
    assert single_article.doi() == "10.1134/S004057950705034X"
