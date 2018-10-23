# Web of Science Explorer

Utility scripts to find article records within the Web of Science data set.

## Overview

This code provides a few wrapper objects for Web of Science (WOS) JSON data files. The `Article` class will wrap an individual JSON record found on one line of a WOS JSON article data file.

```python
article = Article(raw_json)
print(article['id'], article['title'])
```

The `ArticleCollection` object will wrap the files themselves and behaves like an iterator.

```python
filepath = '/path/to/articles.json'
for article in ArticleCollection(filepath):
    print(article['id'], article['title'])
```
