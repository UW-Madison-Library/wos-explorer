from os import path
from wos_explorer.article_collection import ArticleCollection

import pytest

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
