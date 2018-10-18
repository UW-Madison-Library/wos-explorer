import json

class FileCollector:

    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(self.filepath, 'w')

    def collect(self, article):
        self.file.write(json.dumps(article.data) + '\n')

    def close(self):
        self.file.close
