import os
import logging
import json
from .article import Article
from .reference_list import ReferenceList


logger = logging.getLogger(__name__)


class ArticleCollection:

    def __init__(self, filepath):
        self.filepath = filepath

    def __iter__(self):
        logger.info("Opening File: %s" % self.filepath)
        with open(self.filepath, 'r') as file:
            count = 0
            for line in file:
                yield Article(line)
                
                count += 1
                if count % 100000 == 0:
                    logger.info("Articles Read in File: " + str(count))

            logger.info("Total Articles Read in File: " + str(count))

    def select(self, criteria, output_filepath):
        with open(output_filepath, 'w') as output_file:
            for article in self:
                if article.matches(criteria):
                    output_file.write(json.dumps(article.data) + '\n')
                else:
                    continue
        return ArticleCollection(output_filepath)

    def reference_list(self):
        reflist = ReferenceList()
        for article in self:
            for year, ids in article.reference_list():
                for id in ids:
                    reflist.add(year, id)
        return reflist
