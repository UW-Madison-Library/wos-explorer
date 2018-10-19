import logging
from collections import defaultdict
from .article import Article

logger = logging.getLogger(__name__)

def match_articles(input_filepath, criteria, collection):
    count = 0

    logger.info("Opening File: %s" % input_filepath)
    with open(input_filepath) as input_file:
        for line in input_file:

            count += 1
            article = Article(line)
            if article.matches(criteria):
                collection.add(article)

            if count % 100000 == 0:
                logger.info("Articles Read in File: " + str(count))

    logger.info("Total Articles Read in File: " + str(count))

    return collection.close()

def collect_cited_references(article_collection):
    references_by_year = defaultdict(list)
    for article in article_collection:
        for reference in article['references']:
            references_by_year[reference['year']].append(reference['id'])
    return references_by_year
