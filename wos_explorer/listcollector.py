class ListCollector:

    def __init__(self):
        self.articles = []

    def collect(self, article):
        self.articles.append(article)

    def close(self):
        return self.articles
