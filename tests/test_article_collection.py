from wos_explorer.matchers import *
from wos_explorer.article_collection import ArticleCollection

def test_article_parsing(articles_sample):
    assert sum(1 for article in ArticleCollection(articles_sample)) == 10

def test_id_matching(articles_sample, output_filepath):
    ids = ["WOS:000251423400047", "WOS:000249481100010", "WOS:not-in-sample-set"]
    matches = ArticleCollection(articles_sample).select(IdMatcher(ids), output_filepath)
    assert sum(1 for article in matches) == 2
    assert sum(1 for line in open(output_filepath)) == len(ids) - 1

def test_citation_matching(articles_sample, output_filepath):
    ids = ["WOS:000084608600019"]
    matches = ArticleCollection(articles_sample).select(CitationMatcher(ids), output_filepath)
    assert sum(1 for article in matches) == 2
    assert sum(1 for line in open(output_filepath)) == 2

def test_case_insensitive_phrase_matching(articles_sample, output_filepath):
    matches = ArticleCollection(articles_sample).select(PhraseMatcher('baker'), output_filepath)
    assert sum(1 for article in matches) == 1

def test_phrase_matching_in_field_multiple(articles_sample, output_filepath):
    matches = ArticleCollection(articles_sample).select(PhraseMatcher("properties", ["title"]), output_filepath)
    assert sum(1 for article in matches) == 2

def test_phrase_matching_in_field_single(articles_sample, output_filepath):
    matches = ArticleCollection(articles_sample).select(PhraseMatcher("properties", ["abstract_text"]), output_filepath)
    assert sum(1 for article in matches) == 1

def test_phrase_matching_in_multiple_fields(articles_sample, output_filepath):
    matches = ArticleCollection(articles_sample).select(PhraseMatcher("primary", ["title", "abstract_text"]), output_filepath)
    assert sum(1 for article in matches) == 2

def test_phrase_matching_in_word_boundaries(articles_sample, output_filepath):
    matches = ArticleCollection(articles_sample).select(PhraseMatcher("of the", ["abstract_text"]), output_filepath)
    assert sum(1 for article in matches) == 2

def test_phrase_matching_word_boundary_start(articles_sample, output_filepath):
    # Don't match "synthesis" in a search for "thesis"
    matches = ArticleCollection(articles_sample).select(PhraseMatcher("thesis", ["title"]), output_filepath)
    assert sum(1 for article in matches) == 0

def test_phrase_matching_for_wildcard(articles_sample, output_filepath):
    matches = ArticleCollection(articles_sample).select(PhraseMatcher("of the*", ["abstract_text"]), output_filepath)
    assert sum(1 for article in matches) == 3

def test_querying_using_boolean_or(articles_sample, output_filepath):
    matchers = [PhraseMatcher("synthesis", ["title"]), PhraseMatcher("animal studies", ["title"])]
    matches = ArticleCollection(articles_sample).select(Query(matchers, "or"), output_filepath)
    assert sum(1 for article in matches) == 2

def test_querying_using_boolean_and(articles_sample, output_filepath):
    matchers = [PhraseMatcher("similar*", ["abstract_text"]), PhraseMatcher("abnormal", ["abstract_text"])]
    matches = ArticleCollection(articles_sample).select(Query(matchers, "and"), output_filepath)
    assert sum(1 for article in matches) == 2

def test_querying_using_multiple_queries(articles_sample, output_filepath):
    query1 = Query([PhraseMatcher("similar", ["abstract_text"]), PhraseMatcher("similarities", ["abstract_text"])], "or")
    query2 = Query([PhraseMatcher("fetal",   ["abstract_text"]), PhraseMatcher("cells",        ["abstract_text"])], "or")
    matches = ArticleCollection(articles_sample).select(Query([query1, query2], "and"), output_filepath)
    assert sum(1 for article in matches) == 2

def test_querying_using_boolean_not(articles_sample, output_filepath):
    matches = ArticleCollection(articles_sample).select(PhraseMatcher("nuclear", ["abstract_text"], True), output_filepath)
    assert sum(1 for article in matches) == 9

def test_query_with_boolean_not(articles_sample, output_filepath):
    query = Query([PhraseMatcher("abnormal", ["abstract_text"]), PhraseMatcher("ultrasound", ["abstract_text"], True)], "and")
    matches = ArticleCollection(articles_sample).select(query, output_filepath)
    assert [a["id"] for a in matches] == ["WOS:000252158100008"]

def test_nested_query(articles_sample, output_filepath):
    matchers    = [PhraseMatcher("synthesis"), PhraseMatcher("morphological")]
    inner_query = Query([PhraseMatcher("animal"), PhraseMatcher("bone")], "and")
    outer_query = Query([*matchers, inner_query], "or")
    matches     = ArticleCollection(articles_sample).select(outer_query, output_filepath)
    assert sum(1 for article in matches) == 3

def test_leftside_truncation(articles_sample, output_filepath):
    matches = ArticleCollection(articles_sample).select(PhraseMatcher("*perties", ["abstract_text"]), output_filepath)
    assert sum(1 for article in matches) == 1

def test_affiliation_matching_from_set(affiliated_sample, output_filepath):
    uwmadison_names = {"University of Wisconsin Madison", "Univ Wisconsin", "University Wisconsin Health"}
    matches = ArticleCollection(affiliated_sample).select(AffiliationMatcher(uwmadison_names), output_filepath)
    assert sum(1 for article in matches) == 1

def test_affiliation_matching_from_list(affiliated_sample, output_filepath):
    uwmadison_names = ["University of Wisconsin Madison", "Univ Wisconsin", "University Wisconsin Health"]
    matches = ArticleCollection(affiliated_sample).select(AffiliationMatcher(uwmadison_names), output_filepath)
    assert sum(1 for article in matches) == 1

def test_source_title_matching(articles_sample, output_filepath):
    journal_titles = ["THEORETICAL FOUNDATIONS OF CHEMICAL ENGINEERING", "DOWN BEAT"]
    matches = ArticleCollection(articles_sample).select(SourceTitleMatcher(journal_titles), output_filepath)
    assert sum(1 for article in matches) == 2

def test_case_insensitive_source_title_matching(articles_sample, output_filepath):
    journal_titles = ["Theoretical Foundations of Chemical Engineering", "Down Beat"]
    matches = ArticleCollection(articles_sample).select(SourceTitleMatcher(journal_titles), output_filepath)
    assert sum(1 for article in matches) == 2

def test_reflist_ids(articles_sample_reflist):
    assert len(articles_sample_reflist.ids()) == 42

def test_reflist_years(articles_sample_reflist):
    expected_years = ['1960', '1974', '1980', '1985', '1986', '1988', '1989', '1994', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007']
    assert sorted(articles_sample_reflist.years()) == expected_years

def test_reflist_values(articles_sample_reflist):
    assert 'WOS:000246234400039.13' in articles_sample_reflist['1960']

def test_reflist_iteration(articles_sample_reflist):
    assert sum(1 for reference in articles_sample_reflist) == 20

def test_reference_list_ids(single_article_path):
    expected = ['000303524000001.127', 'WOS:000074141300003', 'WOS:000076444100008', 'WOS:000084608600019', 'WOS:000169756700007', 'WOS:000185914300012', 'WOS:000264798000005.30', 'WOS:A1997XH27400004']
    ref_list = ArticleCollection(single_article_path).reference_list()
    assert sorted(ref_list.ids()) == expected

def test_reference_list_years(single_article_path):
    expected = ['1996', '1997', '1998', '1999', '2000', '2001', '2003']
    ref_list = ArticleCollection(single_article_path).reference_list()
    assert sorted(ref_list.years()) == expected

def test_doi_matching(articles_sample, output_filepath):
    dois = ["10.1007/s00383-007-2029-0", "10.1134/S004057950705034X", "10.1007/second-one"]
    matches = ArticleCollection(articles_sample).select(IdentifierMatcher("doi", dois), output_filepath)
    assert sum(1 for _ in matches) == 3
