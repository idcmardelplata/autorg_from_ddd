from autorg.domain.aggregates.collect import Collect
import os
import pytest
from autorg.domain.protocols.repository import Repository
from autorg.infrastructure.adapters.csvrepository import CsvRepository
from autorg.application.input import AppInput, EmptyValueError
from tests.helpers.repository import InMemoryRepository


@pytest.fixture
def setup():
    if os.path.exists("data.csv"):
        os.remove("data.csv")

@pytest.mark.integration
def test_app_should_has_add_input_case(setup):
    repo = CsvRepository()
    app = AppInput(repo)
    app.add_input("input content")
    assert repo.getAll()[0] == "input content"

def test_add_input_not_accept_empty_strings():
    repo = InMemoryRepository()
    app = AppInput(repo)
    with pytest.raises(EmptyValueError):
        app.add_input("")
