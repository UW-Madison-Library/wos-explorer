from wos_explorer.matchers import *
from .helpers import article_by_id

def test_optional_single_char_match():
    # Abstract text data contains "learning alogrithms" plural, with an "s".
    # Abstract text data contains "neural network" singular, without an "s".
    article = article_by_id("WOS-000379940600013")

    pluarl_criteria   = PhraseMatcher("learning algorithm.?", ["abstract_text"])
    assert article.matches(pluarl_criteria)

    singular_criteria = PhraseMatcher("neural network.?", ["abstract_text"])
    assert article.matches(singular_criteria)

def test_matching_with_hyphenation():
    # The title of this article includes "cross-point" with a hyphen.
    article = article_by_id("WOS-000379940600013")

    with_hyphen_criteria = PhraseMatcher("cross-point", ["title"])
    assert article.matches(with_hyphen_criteria)

    without_hyphen_criteria = PhraseMatcher("cross point", ["title"])
    assert not article.matches(without_hyphen_criteria)

    optional_hyphen_criteria = PhraseMatcher("cross-?point", ["title"])
    assert article.matches(optional_hyphen_criteria)

def test_midtoken_optional_matching():
    # The "id" field of this article is "WOS:000379940600013" with a colon.
    # The "alt_id" field (added for testing) of this article is "WOS000379940600013" without a colon.
    article = article_by_id("WOS-000379940600013")

    exact_criteria = PhraseMatcher("WOS:000379940600013", ["id"])
    assert article.matches(exact_criteria)

    optional_colon_criteria = PhraseMatcher("WOS:?000379940600013", ["id"])
    assert article.matches(optional_colon_criteria)

    optional_anychar_criteria = PhraseMatcher("WOS.?000379940600013", ["id"])
    assert article.matches(optional_anychar_criteria)

    exact_criteria = PhraseMatcher("WOS000379940600013", ["alt_id"])
    assert article.matches(exact_criteria)

    optional_colon_criteria = PhraseMatcher("WOS:?000379940600013", ["alt_id"])
    assert article.matches(optional_colon_criteria)

    optional_anychar_criteria = PhraseMatcher("WOS.?000379940600013", ["alt_id"])
    assert article.matches(optional_anychar_criteria)

def test_reference_searching():
    article = article_by_id("WOS-000482104200082")
    criteria = PhraseMatcher("machine* learning", ["references"])
    assert article.matches(criteria)
