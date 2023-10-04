from autorg.application.input import AppInput
"""Step implementation for cli"""


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
    raise NotImplementedError()


@then(u'el sistema no deberia mostrarle una lista')
def step_impl(context):
    raise NotImplementedError()


@then(u'deberia notificarle que "La bandeja de entrada esta vacia"')
def step_impl(context):
    raise NotImplementedError()
