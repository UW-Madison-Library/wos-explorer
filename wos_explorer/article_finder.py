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
    matches = []
    with open(input_filepath) as input_file:
        output_file = None if output_filepath is None else open(output_filepath, 'w')
        for line in input_file:
            article = json.loads(line)
            if article['id'] in ids:
                if output_filepath is None:
                    matches.append(article)
                else:
                    output_file.write(line)
        if output_file is not None:
            output_file.close()
    return matches
