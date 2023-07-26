# Restful Booker con Python

Ejemplo de cómo utilizar la librería requests de Python utilizando la API [Restfull Booker](https://restful-booker.herokuapp.com/). La API también se puede ejecutar localmente => [API Restful-booker](https://github.com/mwinteringham/restful-booker).


# Estructura del proyecto

 -[api_functions.py](api_functions.py) - Contiene las funciones para ejecutar todos los métodos.
 -[test_booker_api.py](test_booker_api.py) - Contiene sólo un test case que es el smoke. Donde se obtiene el token, se crear el booking, se realiza un update parcial y completo, se elimina y se valida si existe.

## Instalaciones a realizar

- Instalar [Python](https://www.python.org/downloads/).
- Instalar las librerías requests (para utlizar los métodos de la api), pytest (para ejecutar los scripts como test cases) y faker (para generar data random).
- Opcional: instalar la API localmente (lo recomiendo para hacer pruebas de manera tranquila). Se descarga o se clona el proyecto desde [aquí](https://github.com/mwinteringham/restful-booker). Yo utilizo [Visual Studio Code](https://code.visualstudio.com/download). Una vez descargado el proyecto, abrir una terminal y ejecutar los siguientes comandos para levantar la API en la ruta: [http://localhost:3001](http://localhost:3001/)

```
$ npm install
```

```
$ npm start
```
- Instalar Pytest
```
$ pip install pytest
```
- Instalar Requests
```
$ pip install requests
```
- Instalar Faker
```
$ pip install Faker
```
