from wos_explorer import match_articles

def test_case_insensitive_matching(articles_sample):
    phrase = 'baker'
    articles = match_articles(phrase, articles_sample)
    assert len(articles) == 1

# def test_botcount(sample_log):
#     stats = analyze_log_file(sample_log)
#     assert stats['bot_count'] == 10
