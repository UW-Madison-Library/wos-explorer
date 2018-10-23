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

def test_reflist_ids(articles_sample_reflist):
    assert len(articles_sample_reflist.ids()) == 42

def test_reflist_years(articles_sample_reflist):
    expected_years = ['1960', '1974', '1980', '1985', '1986', '1988', '1989', '1994', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007']
    assert sorted(articles_sample_reflist.years()) == expected_years

def test_reflist_values(articles_sample_reflist):
    assert 'WOS:000246234400039.13' in articles_sample_reflist['1960']

def test_reflist_iteration(articles_sample_reflist):
    assert sum(1 for reference in articles_sample_reflist) == 20
