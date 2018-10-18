import sys
import json
import re
from .filecollector import FileCollector
from .listcollector import ListCollector

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

def match_phrase(phrase, filepath):
    matches = []
    pattern = re.compile(phrase, re.IGNORECASE)
    with open(filepath) as file:
        for line in file:
            article = json.loads(line)
            if contains_phrase(article, pattern):
                matches.append(article)
    return matches

def match_ids(ids, input_filepath, output_filepath=None):
    collector = FileCollector(output_filepath) if output_filepath else ListCollector()
    with open(input_filepath) as input_file:
        for line in input_file:
            article = json.loads(line)
            if article['id'] in ids:
                collector.collect(article)
    return collector.close()
