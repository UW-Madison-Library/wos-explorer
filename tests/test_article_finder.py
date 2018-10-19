from wos_explorer import article_finder
from wos_explorer.collectors import FileCollector, ListCollector
from wos_explorer.matchers import IdMatcher, PhraseMatcher

def test_case_insensitive_phrase_matching(articles_sample):
    phrase = 'baker'
    articles = article_finder.match_articles(articles_sample, PhraseMatcher(phrase), ListCollector())
    assert len(articles) == 1

def test_wosid_matching(articles_sample):
    ids = ["WOS:000251423400047", "WOS:000249481100010", "WOS:not-in-sample-set"]
    articles = article_finder.match_articles(articles_sample, IdMatcher(ids), ListCollector())
    assert len(articles) == 2

def test_matching_with_output_file(articles_sample, tmpdir):
    ids = ["WOS:000251423400047", "WOS:000249481100010"]
    output_filepath = str(tmpdir.join("matched-articles.json"))
    article_finder.match_articles(articles_sample, IdMatcher(ids), FileCollector(output_filepath))

    num_lines = sum(1 for line in open(output_filepath))
    assert num_lines == len(ids)

    articles = article_finder.match_articles(output_filepath, IdMatcher(ids), ListCollector())
    parsed_ids = [article['id'] for article in articles]
    assert sorted(parsed_ids) == sorted(ids)

def test_collecting_references(articles_sample):
    ids = ["WOS:000250583700033", "WOS:000246216800044"]
    articles = article_finder.match_articles(articles_sample, IdMatcher(ids), ListCollector())
    refs_by_year = article_finder.collect_cited_references(articles)
    assert "WOS:000084608600019" in refs_by_year["2000"]
