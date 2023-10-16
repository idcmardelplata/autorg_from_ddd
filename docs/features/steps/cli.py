from autorg.application.input import AppInput
"""
Step implementation for cli
NOTE: Here is only expected behavior from user's pov, hence there is no real use of Cli, intended to avoid coupling with that

"""


@given(u'que la bandeja de entrada contiene inputs')
def step_impl(context):
    context.ut = AppInput(context.repository)


@when(u'el usuario indique al sistema que desea ver una lista de inputs en la bandeja de entrada')
def step_impl(context):
    context.response = context.ut.list_inputs()

@then(u'el sistma deberia mostrarle una lista de inputs actuales que contiene la bandeja de entrada')
def step_impl(context):
    actual =  [+1 for input in context.inputs if input in context.response ]
    assert len(actual) == 4


@given(u'que la bandeja de entrada no contiene inputs')
def step_impl(context):
    context.repository.items.clear()
    context.ut = AppInput(context.repository)


@then(u'el sistema no deberia mostrarle una lista')
def step_impl(context):
    assert type(context.response) is not list


@then(u'deberia notificarle que "La bandeja de entrada esta vacia"')
def step_impl(context):
    assert context.response == "La bandeja de entrada esta vacia"
