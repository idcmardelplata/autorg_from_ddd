#language: es
Característica: Clarificacion
  La Clarificacion es responder una serie de preguntas sobre el significado de un input para obtener organizables, y se hace desde una lista ordenada descendientemente por importancia de al menos un input

  @happy
  Escenario: el usuario clarifica exitosamente una lista de inputs
    Dado que hay al menos un input en la lista de ordenables
    Cuando el usuario define el significado subjetivo de un input
    Y responde todas las preguntas apropiadas en el flujo
    Entonces el sistema deberia dejar por cada input algun tipo de organizable en la lista para organizar

  @happy
  Escenario: el usuario relaciona un input consultable con uno o mas proyectos
    Dado que el usuario determino que el significado de un input es no accionable y consultable
    Cuando quiera relacionarlo con un proyecto o mas existente/s
    Entonces el sistema deberia mostrarle una lista de proyectos existentes
    Y el usuario deberia poder seleccionar mas de uno para ser relacionado

  @happy
  Escenario: el usuario termina de clarificar un input consultable
    Dado que el usuario determino que un input era consultable y lo relaciono con proyecto/s
    Entonces el sistema deberia enlistar el significado dentro de consultables

  @break_policy
  Escenario: el usuario no relaciona un consultable con ningun proyecto
    Dado que el usuario determino que un input era consultable
    Pero no lo relaciono con proyecto alguno
    Entonces el sistema no deberia enlistar el significado dentro de consultables
    Y deberia notificar al usuario de que debe relacionar un consultable con un proyecto o mas

  @happy
  Escenario: el usuario relaciona un input incubable con uno o mas objetivos existentes
    Dado que el usuario determino que el significado de un input es no accionable e incubable
    Cuando quiera relacionarlo con un objetivo o mas existentes
    Entonces el sistema deberia mostrarle una lista de objetivos existentes junto a su valor de impacto
    Y el usuario deberia poder seleccionar uno o mas para ser relacionado

  @happy
  Escenario: el usuario termina de clarificar un input incubable
    Dado que el usuario determino que un input era incubable y lo relaciono con al menos un objetivo existente
    Entonces el sistema deberia enlistar el incubable dentro de algun dia tal vez

  @break_policy
  Escenario: el usuario no relaciona un incubable con ningun objetivo
    Dado que el usuario determino que un input era incubable
    Pero no lo relaciono con objetivo alguno
    Entonces el sistema no deberia enlistar el significado dentro de algun dia tal vez 
    Y deberia notificar al usuario de que debe relacionar un incubable con un objetivo o mas

  @break_policy
  Escenario: el usuario no debe avanzar en la clarificacion si no responde apropiadamente alguna pregunta
    Dado que el usuario comenzo a clarificar algun input de la lista de ordenables
    Pero el usuario no responde apropiadamente una pregunta del flujo 
    Entonces el sistema no debe permitirle seguir adelante con la clarificacion
    Y debe notificarle de que debe responder apropiadamente la pregunta para poder avanzar

  @break_policy
  Escenario: no existen inputs a clarificar en la lista de ordenables
    Dado que no existen inputs a clarificar en la lista de ordenables
    Entonces el sistema debe notificar que no hay nada para clarificar

  
