# IMDB-Movies

## Patrones de diseño
* Builder: En ```magicKeyGenerator```, con la función de addCategory.

![MagicKeyGenerator](https://user-images.githubusercontent.com/56079667/174462361-2cf4252d-316f-4d9d-8b2e-3967d03aefc9.png)

* Simple Factory: En ```movie_to_dictionary.py``` con la clase abstracta ```Exporter``` que extiende _csvExporter_ y _jsonExporter_

![Simple Factory](https://user-images.githubusercontent.com/56079667/174462220-111bc8fd-8016-41cd-8121-10a3d2cf948a.png)


## Principios identificados
* Single Responsability: En ```movie_to_dictionary.py``` al separar el módulo que se encarga de convertir los datos a un diccionario.
* Open / Close: La clase de ```MagicKeyGenerator.py``` tiene el atributo 'numberofcategoriesAllowed' el cual permite fijar un número máximo que es modificable, permitiendo aumentar las categorias a usar para generar la llave en caso de que se quiera hacer más complejo al algoritmo o incluir otras categorías.
* Dependency Inversion: En ```movie_fetcher.py``` se tenia la relación _movie_fetcher --> models_, se creó la interfaz **UriInterface.py** para invertir la dependencia, resultando en _models --> movie_fetcher_
* Interface Segregation: En ```UriInterface.py``` se separó el método de get_postgres_uri que originalmente era de models, con lo que quienes usen la interfaz nueva solo podran acceder a esta funcion y no a lo demás de models.

## Diagramas

### Diagramas de casos de uso

![Use Cases](https://user-images.githubusercontent.com/56079667/174462367-dca7ebd6-0bf3-468a-a911-66d903dd3bd0.png)

### Diagramas de secuencia

#### Registro de usuario

![user registration](https://user-images.githubusercontent.com/56079667/174462382-b20606c3-9624-4cc6-8a6b-5f0d781913d3.jpg)

#### Obtener recomendaciones de películas

![retrieval movie recommendation](https://user-images.githubusercontent.com/56079667/174462379-9435683c-5745-41b7-871b-ba2ba27bce02.jpg)
