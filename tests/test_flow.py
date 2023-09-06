from autorg.flow.flow import Flow
import pytest

# Kind of flow should be an enum 
def test_given_a_name_flow_should_exists():
    assert Flow("Clarification") != None

def test_flow_questions_should_differ_between_a_clarification_and_another_flow():
    clarifi_questions = Flow("Clarification").get_questions()
    another_questions = Flow("Another").get_questions()
    assert clarifi_questions[0].get_question() != another_questions [0].get_question()
