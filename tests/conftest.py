from os import path
from wos_explorer.article_collection import ArticleCollection
from wos_explorer.article import Article

import pytest

@pytest.fixture()
def single_article_path(example_path):
    return path.join(example_path + '/single-article.json')

@pytest.fixture()
def single_article(single_article_path):
    return Article(open(single_article_path).read())

@pytest.fixture()
def single_article_no_refs(example_path):
    return Article(open(path.join(example_path + '/single-article-no-references.json')).read())

@pytest.fixture()
def example_path():
    return path.join(path.dirname(path.abspath(__file__)), 'examples')

@pytest.fixture()
def articles_sample():
    return path.join(example_path(), 'articles-sample.json')

@pytest.fixture()
def output_filepath(tmpdir):
    return str(tmpdir.join("matched-articles.json"))

@pytest.fixture()
def articles_sample_reflist(tmpdir, articles_sample):
    return ArticleCollection(articles_sample).reference_list()
