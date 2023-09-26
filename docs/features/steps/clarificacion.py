
@given(u'que hay al menos un input en la lista de ordenables')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given que hay al menos un input en la lista de ordenables')


@when(u'el usuario define el significado subjetivo de un input')
def step_impl(context):
    raise NotImplementedError(u'STEP: When el usuario define el significado subjetivo de un input')


@when(u'responde todas las preguntas apropiadas en el flujo')
def step_impl(context):
    raise NotImplementedError(u'STEP: When responde todas las preguntas apropiadas en el flujo')


@then(u'el sistema deberia dejar algun tipo de organizable en la lista para organizar')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then el sistema deberia dejar algun tipo de organizable en la lista para organizar')


@given(u'que el usuario comenzo a clarificar algun input de la lista de ordenables')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given que el usuario comenzo a clarificar algun input de la lista de ordenables')


@given(u'el usuario no responde apropiadamente una pregunta del flujo')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given el usuario no responde apropiadamente una pregunta del flujo')


@then(u'el sistema no debe permitirle seguir adelante con la clarificacion')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then el sistema no debe permitirle seguir adelante con la clarificacion')


@then(u'debe notificarle de que debe responder apropiadamente la pregunta para poder avanzar')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then debe notificarle de que debe responder apropiadamente la pregunta para poder avanzar')
