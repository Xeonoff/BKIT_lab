from pytest_bdd import scenarios, scenario, given, when, then
from pathlib import Path
import pytest
import sys,os

sys.path.append(os.getcwd()) #current working directory
from main import cm_timer

featureFileDir='myfeatures'
featureFile='cm_timer_feature.feature'
BASE_DIR=Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)


@scenario(FEATURE_FILE,'The program will fall asleep for the time specified by the user')
def testing_cm_timer():
    pass

@given('I have the number 3 - it is sleeping time',target_fixture='params')
def params():
    return 3

@when('Program will fall asleep with cm_timer and return sleeping time',target_fixture='created_timer')
def created_timer(params):
    return cm_timer(params)

@then('I expect the result to be same seconds as user specified')
def created_timer(created_timer):
    assert created_timer == 3


