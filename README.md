# Prueba-PrimeStone-Jr
Prueba primestone
FUNCIONAMIENTO
1. Crear y Activar entorno virtual
2. Tener un gestor de bases de datos como mysql(instalar mysqlclient), postgres o sino por defecto en sqlite
3. Crear base de datos con el nombre de pruebaprimestone esto en mysql y postgres.
4. Migrar el modelo (python3 manage.py makemigrations) despues (python3 manage.py migrate)
5. Para el modelo People que se creo se puede realizar el crud completo.
6. Falto hacer la conversion de la estatura de la persona e implementar la función de números primos.

MODELO People

METODO GET (ejemplo de consultas)
Consulta todos people http://127.0.0.1:8000/api/people

METODO POST (ejemplo agregar un client) 
Consulta todos people http://127.0.0.1:8000/api/people
{
  "name": "Pedro",
  "height": 70
}

METODO PUT (ejemplo actualizar un people)

http://127.0.0.1:8000/api/people/1

METODO DELETE (ejemplo eliminar un people)

http://127.0.0.1:8000/api/clients/1




MUCHAS GRACIAS...
