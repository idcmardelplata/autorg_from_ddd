from autorg.flow.flow import Flow
from autorg.pregunta.pregunta import Pregunta
import pytest

# Kind of flow should be an enum 
# flow should use strategy for load questions
def test_given_a_name_flow_should_exists():
    assert Flow("Clarification") != None

def test_flow_questions_should_differ_between_a_clarification_and_another_flow():
    clarifi_questions = Flow("Clarification").get_questions()
    another_questions = Flow("Another").get_questions()
    assert clarifi_questions[0].get_question() != another_questions [0].get_question()

def test_aa_clarification_flow_should_contain_clarification_questions():
    str_clarification_questions = ["Que significa esto para mi","Es accionable?","Que creo que debo hacer","Cuantas acciones atomicas","Depende de mi?","Es accion siguiente o esta bloqueada?","El no accionable tiene valor potencial?"]
    clarification_questions = [Pregunta(x) for x in str_clarification_questions]
    flow_questions = Flow("Clarification").get_questions()
    assert all([clarification_questions.get_question() == flow_questions.get_question() for clarification_questions, flow_questions in zip(clarification_questions, flow_questions)])

def test_flow_position_show_move_foward_when_a_question_is_answered():
    flow = Flow("Clarification")
    index_at_start = flow.start().get_index()
    flow.answer_current_question("Significa tal cosa")
    index_after_response = flow.get_index()
    assert index_at_start < index_after_response
    

