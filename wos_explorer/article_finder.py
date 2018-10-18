from .article import Article

def match_articles(input_filepath, matcher, collector):
    with open(input_filepath) as input_file:
        for line in input_file:
            article = Article(line)
            if matcher.matches(article):
                collector.collect(article)
    return collector.close()
