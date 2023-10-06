from tests.helpers.factories import CollectFactory
from autorg.domain.entities.input import Input
from autorg.domain.aggregates.collect import Collect
from tests.helpers.repository import InMemoryRepository

# TEST: El agregado debe permitir almacenar los inputs a un repositorio.
# TEST: El agregado debe permitir cargar los inputs desde un repositorio.


def test_aggregate_should_create_a_unique_id_for_each_input():
    # HACK: Hacer que CollectFactory me retorne los inputs creados
    sut = Collect()
    sut.add_input("random input 1")
    sut.add_input("random input 2")
    inputs = sut.getAll()
    assert inputs[0].id() != inputs[1].id()


def test_aggregate_should_contain_a_method_to_construct_a_input():
    sut = CollectFactory.createWithInput()
    assert type(sut.getAll().pop()) is Input


def test_aggregate_should_ensure_that_not_exists_duplicate_inputs():
    sut = CollectFactory.createDuplicateInputs()
    assert len(sut.getAll()) == 1


def test_added_input_should_store_in_list():
    sut = CollectFactory.createWithInput()
    assert len(sut.getAll()) == 1


def test_collect_can_hold_many_inputs():
    sut = CollectFactory.createManyInputs(count=2)
    assert len(sut.getAll()) == 2


def test_input_list_should_be_stored():
    sut = CollectFactory.createWithInput()
    assert sut.getAll()[0].value().get("content") == "some random input"
