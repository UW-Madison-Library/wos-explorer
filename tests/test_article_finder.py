from __future__ import print_function
from wos_explorer import article_finder

def test_case_insensitive_phrase_matching(articles_sample):
    phrase = 'baker'
    articles = article_finder.match_phrase(phrase, articles_sample)
    assert len(articles) == 1

def test_wosid_matching(articles_sample):
    ids = ["WOS:000251423400047", "WOS:000249481100010", "WOS:not-in-sample-set"]
    articles = article_finder.match_ids(ids, articles_sample)
    assert len(articles) == 2

def test_matching_with_output_file(articles_sample, tmpdir):
    ids = ["WOS:000251423400047", "WOS:000249481100010"]
    output_filepath = str(tmpdir.join("matched-articles.json"))
    article_finder.match_ids(ids, articles_sample, output_filepath)
    articles = article_finder.match_ids(ids, output_filepath)
    assert len(articles) == 2