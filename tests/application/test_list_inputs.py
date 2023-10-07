import os
import pytest
from autorg.application.input import AppInput
from tests.helpers.repository import InMemoryRepository


class TestListInputs:


#FIX: App should return a empty list if there is no inputs to list
    @pytest.mark.integration
    def test_list_inputs_should_return_a_string_when_there_is_no_inputs_into_inbox(self):
        repo = InMemoryRepository()
        app = AppInput(repo)
        assert type(app.list_inputs()) is list


