from autorg.domain.aggregates.collect import Collect
import datetime
from autorg.domain.entities.input import Input


def test_input_should_be_a_entity():
    sut = Input("some random content")
    assert sut.id() == 0


def test_input_entity_should_store_creation_datetime():
    creation_date = datetime.datetime.now()
    sut = Input("some random content", creation_date=creation_date)
    assert sut.creation_date() == creation_date


def test_input_should_retrieve_creation_date_and_content():
    creation_date = datetime.datetime.now()
    content = "some random content"
    sut = Input("some random content", creation_date=creation_date)
    assert sut.value() == {"creation_date": creation_date, "content": content}
