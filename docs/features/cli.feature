#language: es
@fixture.repo
Característica: Command line interface
  El usuario accedera a las funcionalidades del sistema mediante una interfaz de linea de comandos

  Escenario: el usuario lista los inputs recopilados en la bandeja de entrada
    Dado que la bandeja de entrada contiene inputs
    Cuando el usuario indique al sistema que desea ver una lista de inputs en la bandeja de entrada
    Entonces el sistma deberia mostrarle una lista de inputs actuales que contiene la bandeja de entrada

  Escenario: el usuario lista los inputs recopilados en la bandeja pero no hay inputs
    Dado que la bandeja de entrada no contiene inputs
    Cuando el usuario indique al sistema que desea ver una lista de inputs en la bandeja de entrada
    Entonces el sistema no deberia mostrarle una lista
    Y deberia notificarle que "La bandeja de entrada esta vacia"
