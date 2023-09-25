# from tests.helpers.factories import CollectFactory
from tests.helpers.factories import CollectFactory



#TEST: Should create a integration test for other types of repositories like csv, database etc.
#TEST: Create a testfile for the application layer.
#NOTE: Create base entity (input) and logic of this entity

def test_added_input_should_store_in_list():
    sut = CollectFactory.create()
    sut.input("some random input")
    assert len(sut.getAll() ) == 1

def test_added_input_should_be_unique():
    sut = CollectFactory.create()
    sut.input("some random input")
    sut.input("some random input")
    assert len(sut.getAll() ) == 1

def test_should_return_list_of_str():
    sut = CollectFactory.create()
    sut.input("some random input")
    sut.input("some random input")
    assert type (sut.getAll()) is list

def test_collect_can_hold_many_inputs():
    sut = CollectFactory.create()
    sut.input("some random input")
    sut.input("some random input 2")
    assert len(sut.getAll() ) == 2

def test_input_list_should_be_stored():
    sut = CollectFactory.create()
    sut.input("some random input")
    assert sut.getAll()[0] == "some random input"
