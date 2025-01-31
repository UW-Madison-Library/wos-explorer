from os import path
from wos_explorer.article import Article

def article_by_id(id):
    raw_json = open(path.join(path.dirname(__file__), "examples", "searching", id + ".json")).read()
    return Article(raw_json)
