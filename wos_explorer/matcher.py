import sys
import json
import re

def collect_values(contents, values):
    if isinstance(contents, dict):
        collect_values(list(contents.values()), values)
    elif isinstance(contents, list):
        for item in contents:
            collect_values(item, values)
    else:
        values.append(contents)
    return values

def contains_phrase(contents, pattern):
    for value in collect_values(contents, []):
        if (isinstance(value, str) and pattern.search(value)):
            return True
    return False

def match_articles(phrase, filepath):
    matches = []
    pattern = re.compile(phrase, re.IGNORECASE)
    with open(filepath) as file:
        for line in file:
            article = json.loads(line)
            if contains_phrase(article, pattern):
                matches.append(article)
    return matches
