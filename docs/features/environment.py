from behave.fixture import fixture, use_fixture_by_tag
from tests.helpers.repository import InMemoryRepository

@fixture(name="repo")
def repo(context):
    repository = InMemoryRepository()
    context.inputs = ["hello1","how2","are3","you4"]
    for input in context.inputs:
        repository.store(input)
    context.repository = repository

fixture_registry = {
    "fixture.repo": repo,
}

    # -- BEHAVE HOOKS:

def before_tag(context, tag):
    if tag.startswith("fixture."):
        # USE-FIXTURE FOR TAGS: @fixture.repo
        return use_fixture_by_tag(tag, context, fixture_registry)
