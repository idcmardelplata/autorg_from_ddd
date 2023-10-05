import os
import pytest
from autorg.application.input import AppInput
from tests.helpers.repository import InMemoryRepository


class TestListInputs:


#TEST: list inpujts should return a dto actually or use optional pattern 
    @pytest.mark.integration
    def test_list_inputs_should_return_a_string_when_there_is_no_inputs_into_inbox(self):
        repo = InMemoryRepository()
        app = AppInput(repo)
        assert type(app.list_inputs()) is str


