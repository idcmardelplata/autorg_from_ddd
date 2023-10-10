from autorg.domain.aggregates.collect import Collect
import os
from autorg.domain.entities.input import Input
from autorg.application.dtos.input_dto import InputDto
import pytest
from autorg.domain.protocols.repository import Repository
from autorg.infrastructure.adapters.csvrepository import CsvRepository
from autorg.application.input import AppInput, EmptyValueError
from tests.helpers.repository import InMemoryRepository

class TestAppInput:
    @classmethod
    def teardown_class(_cls):
        if os.path.exists("data.csv"):
            os.remove("data.csv")

    @pytest.mark.integration
    def test_app_should_has_add_input_case(self):
        repo = CsvRepository()
        app = AppInput(repo)
        app.add_input(InputDto(None,"input content",None))
        result = repo.getAll()

        assert type(result) is list

    def test_add_input_not_accept_empty_strings(self):
        repo = InMemoryRepository()
        app = AppInput(repo)
        with pytest.raises(EmptyValueError):
            app.add_input("")

