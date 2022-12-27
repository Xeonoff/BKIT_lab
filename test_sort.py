from pytest_bdd import scenario, given, when, then
from pathlib import Path
import pytest
import sys,os

sys.path.append(os.getcwd()) #current working directory
from main import sort

featureFileDir='myfeatures'
featureFile='sort_feat.feature'
BASE_DIR=Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)


@scenario(FEATURE_FILE,'Data need to be sorted by abs')
def testing_sort():
    pass

@given('Some data',target_fixture='data')
def data():
    return [4, -30, 100, -100, 123, 1, 0, -1, -4]

@when('Data get sorted with sort',target_fixture='using_sort')
def using_sort(data):
    return sort(data)

@then('Data is sorted')
def using_sort(using_sort):
    assert using_sort==[123, 100, -100, -30, 4, -4, 1, -1, 0]


