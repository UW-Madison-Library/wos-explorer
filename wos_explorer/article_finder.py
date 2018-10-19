import logging
from .article import Article

logger = logging.getLogger(__name__)

def match_articles(input_filepath, matcher, collector):
    count = 0
    logger.info("Opening File: %s" % input_filepath)
    with open(input_filepath) as input_file:
        for line in input_file:
            count += 1
            article = Article(line)
            if matcher.matches(article):
                collector.collect(article)

            if count % 100000 == 0:
                logger.info("Articles Read in File: " + str(count))

    logger.info("Total Articles Read in File: " + str(count))

    return collector.close()
