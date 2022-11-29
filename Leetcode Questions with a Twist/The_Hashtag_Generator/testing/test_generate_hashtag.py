import pytest
from solve_problem import generate_hashtag
import pandas as pd

# All words must have their first letter capitalized.
def test_generate_hashtag_StartWithHash():

    test_string = 'hello world'
    test_result = generate_hashtag(test_string)

    assert test_result == '#HelloWorld'


 # If the final result is longer than 140 chars it must return false.
def test_generate_hashtag_ReturnFalseWhenLenBiggerThan140():

    test_string = 'a' * 140
    test_result = generate_hashtag(test_string)

    assert test_result == False


# If the input or the result is an empty string it must return false.
def test_generate_hashtag_ReturnFalseIfEmptyString():

    test_string = ''
    test_result = generate_hashtag(test_string)

    assert test_result == False