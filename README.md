# Prueba-PrimeStone-Jr
Prueba primestone
FUNCIONAMIENTO
1. Crear y Activar entorno virtual: crear(python3 -m virtualen entorno) - Activar(source entorno/bin/activate) esto para linux
2. Tener un gestor de bases de datos como mysql(instalar mysqlclient), postgres o sino por defecto en sqlite
3. Tener instalado django y djangorestframework ya que fue el framework en el que se desarrollo la api.
4. Crear base de datos con el nombre de pruebaprimestone esto en mysql y postgres.
5. Migrar el modelo (python3 manage.py makemigrations) despues (python3 manage.py migrate)
6. Para el modelo People que se creo se puede realizar el crud completo.
7. Falto hacer la conversion de la estatura de la persona e implementar la función de números primos.

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
