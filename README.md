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

Because references are an important field, calling `article.references()` is preferable to using the `dict` style accessor `article['references']`. Using the method form will always return a list. Even when the raw JSON has a null value for references, the article object will always return an empty list so it is safe to iterate over the field.

The `ReferenceList` object is a data structure that wraps the references for either an `Article` or `ArticleCollection` object. It behaves as an iterable object wrapper around a dictionary in which the keys are years when references were published and each year's value is a `Set` of WOS ids.

`ReferenceList` objects also have convenience methods to return all their years or ids.

```python
filepath = '/path/to/articles.json'
print( ArticleCollection(filepath).reference_list().years() )
# => ['1996', '1997', '1998', '1998', '1999', '2000', '2001', '2003']
```
