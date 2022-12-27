from pytest_bdd import scenarios, scenario, given, when, then
from pathlib import Path
import pytest
import sys,os

sys.path.append(os.getcwd()) #current working directory
from main import gen_random

featureFileDir='myfeatures'
featureFile='gen_random_feature.feature'
BASE_DIR=Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)


@scenario(FEATURE_FILE,'A new array will be created from random numbers provided by the user')
def testing_gen_random():
    pass

@given('I have the numbers 10, 1, 3',target_fixture='params')
def params():
    return 10,1,3

@when('Array get created with gen_random',target_fixture='created_array')
def created_array():
    return list(set(gen_random(10,1,3)))

@then('I expect the result to be array with random numbers 1-3 which set will be [1,2,3]')
def created_array(created_array):
    assert created_array==[1,2,3]


