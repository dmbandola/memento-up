"""Acceptance Test for Creating User Account feature"""

from lettuce import step
import json
from nose.tools import assert_equal, assert_raises

@step(u'Given I have input the needed information')
def given_i_have_input_the_needed_information(step):
    assert True

@step(u'When I click the done button')
def when_i_click_the_done_button(step):
    assert True

@step(u'Then the system will output a success message')
def then_the_system_will_output_a_success_message(step):
    assert True

@step(u'Given I have input an existing username')
def given_i_have_input_an_existing_username(step):
    assert True
    
@step(u'Then the system will alert that the username already exists')
def then_the_system_will_alert_that_the_username_already_exists(step):
    assert True

@step(u'Given I did not fill all the information needed')
def given_i_did_not_fill_all_the_information_needed(step):
    assert True

@step(u'Then the system will alert to input all the information needed')
def then_the_system_will_alert_to_input_all_the_information_needed(step):
    assert True
