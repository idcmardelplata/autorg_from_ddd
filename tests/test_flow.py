from autorg.flow.flow import Flow
from .helpers.fake_pregunta import Fake_Pregunta as Pregunta
import pytest

# Kind of flow should be an enum 
# flow should use strategy for load questions
@pytest.mark.parametrize(
    ("flow"),
    [
        (Flow("Clarification"))
    ]
)
class Test_Flow_Clarification:
        
    @pytest.fixture
    def clarification_questions(self,flow):
        str_clarification_questions = ["Que significa esto para mi","Es accionable?","Que creo que debo hacer","Cuantas acciones atomicas","Depende de mi?","Es accion siguiente o esta bloqueada?","El no accionable tiene valor potencial?"]
        clarification_questions = [Pregunta(x) for x in str_clarification_questions]
        return clarification_questions

    @pytest.fixture
    def questions(self,flow):
        return flow.get_questions()

    def test_given_a_name_flow_should_exists(self,flow):
        assert flow!= None

    def test_flow_questions_should_differ_between_a_clarification_and_another_flow(self,flow,questions):
        another_questions = Flow("Another").get_questions()
        assert questions[0].get_question() != another_questions [0].get_question()

    def test_aa_clarification_flow_should_contain_clarification_questions(self,flow,questions,clarification_questions):
        assert all([clarification_questions.get_question() == questions.get_question() for clarification_questions, questions in zip(clarification_questions, questions)])
    
    def test_flow_position_show_move_foward_when_a_question_is_answered(self,flow):
        flow = Flow("Clarification")
        index_at_start = flow.start().get_index()
        flow.answer_current_question("Significa tal cosa")
        index_after_response = flow.get_index()
        assert index_at_start < index_after_response
        
    

    def test_flow_should_has_a_unanswered_questions_list(self,flow):
        assert hasattr(flow,"unanswered_questions") and isinstance(flow.unanswered_questions,list)
    
    
    def test_flow_should_locate_all_unanswered_questions_in_unanswered_questions_list(self,flow,clarification_questions):
        unanswered_questions = flow.get_unanswered_questions()
        assert len(unanswered_questions)!= 0 and all([clarification_questions.get_question() == unanswered_questions.get_question() for clarification_questions, unanswered_questions in zip(clarification_questions, unanswered_questions)])
    
    def test_when_current_question_is_answered_then_unanswered_questions_list_should_remove_it(self,flow):
        current_question = flow.get_current_question()
        flow.answer_current_question("Something")
        after_response_question = flow.get_current_question()
        assert not current_question.get_question().__eq__(after_response_question.get_question())
    
    
# when i answer a question then flow should give me another one different
# clarification flow has subflows, procesar accionable, procesar no accionable, planificar proyecto... definir los subflujos y hacer que sgeun una respuesta se cambie de flujo 
