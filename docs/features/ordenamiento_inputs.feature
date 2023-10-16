#language: es
Característica: Ordenamiento de inputs
El usuario debe indicar de alguna forma cual es la importancia de cada input que haya recopilado, esto a la hora de clarificar, para obtener un orden a la hora de clarificar que corresponda a comenzar con lo mas importante de todo y terminar con lo menos.
Para esto hay dos maneras, o el usuario ingresa el valor manualmente en un rango de 1 a 10, o lo relaciona con objetivos existentes que contengan un valor de priroidad.
Esta feature depende de la existencia de objetivos en el sistema

  Escenario: el usuario ordena los inputs a clarificar indicando importancia manualmente
    Dado que el usuario habia recopilado inputs
    Cuando indique que desea ordenarlos manualmente
    E ingrese un valor para cada input del 1 al 10
    Entonces la lista de inputs deberia quedar ordenada

  Escenario: El usuario ingresa un valor manualmente fuera de rango
    Dado que el usuario esta ordenando manualmente
    Pero ingresa un valor que no esta entre el 1 y el 10
    Entonces el sistema no deberia ordenar la lista
    Y deberia indicarle al usuario que el rango de importancia es de 1 a 10 inclusive
