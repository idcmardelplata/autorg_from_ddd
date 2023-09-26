#language: es
Característica: Clarificacion
  La Clarificacion es responder una serie de preguntas sobre el significado de un input para obtener organizables, y se hace desde una lista ordenada descendientemente por importancia de al menos un input

  @happy
  Scenario: el usuario clarifica exitosamente una lista de inputs
    Dado que hay al menos un input en la lista de ordenables
    Cuando el usuario define el significado subjetivo de un input
    Y responde todas las preguntas apropiadas en el flujo
    Entonces el sistema deberia dejar algun tipo de organizable en la lista para organizar

  @break_policy
  Scenario: el usuario no debe avanzar en la clarificacion si no responde apropiadamente alguna pregunta
    Dado que el usuario comenzo a clarificar algun input de la lista de ordenables
    Pero el usuario no responde apropiadamente una pregunta del flujo 
    Entonces el sistema no debe permitirle seguir adelante con la clarificacion
    Y debe notificarle de que debe responder apropiadamente la pregunta para poder avanzar


