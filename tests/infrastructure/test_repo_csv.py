from autorg.domain.aggregates.collect import Collect
from autorg.infrastructure.adapters.csvrepository import CsvRepository
import pytest
import os


#TEST: ¿Debo manejar alguna logica para borrar los elementos segun algun criterio?
#TEST: Hay un bug sorpresa que deberias buscar josu.... :) #TaskForHome. #Tip (centrate en la funcionalidad basica del componente)


@pytest.fixture
def setup():
    """
    Create subjects for tests
    """
    if os.path.exists("data.csv"):
        os.remove("data.csv")

    repo = CsvRepository()
    collect = Collect(repo)
    return [repo, collect]

@pytest.mark.integration
def test_repo_should_store_data_in_csv_file(setup):
    [_sut, collect] = setup
    collect.input("First input")
    collect.input("Second input")
    assert collect.getAll()[1] == "Second input"

@pytest.mark.integration
def test_given_input_the_find_should_return_the_id_of_input(setup):
    [repo, collect] = setup
    for n in range(1,11):
        collect.input(f"Item {n}")
    assert repo.find("Item 3") == 2

@pytest.mark.integration
def test_should_return_all_inputs(setup):
    items = ["First element", "second input", "third input", "more content"]
    [_repo, collect] = setup 
    for item in items:
        collect.input(item)

    assert collect.getAll() == items
