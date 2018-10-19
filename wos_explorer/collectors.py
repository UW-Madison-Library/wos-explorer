import json


class FileCollector:

    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(self.filepath, 'w')

    def add(self, article):
        self.file.write(json.dumps(article.data) + '\n')

    def close(self):
        self.file.close


class ListCollector:

    def __init__(self):
        self.articles = []

    def add(self, article):
        self.articles.append(article)

    def close(self):
        return self.articles
