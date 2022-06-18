# IMDB-Movies

## Patrones de diseño
* Builder: En magicKeyGenerator, con la función de addCategory.

## Principios identificados
* Single Responsability: En ```movie_to_dictionary.py``` al separar el módulo que se encarga de convertir los datos a un diccionario.
* Open / Close: La clase de ```MagicKeyGenerator.py``` tiene el atributo 'numberofcategoriesAllowed' el cual permite fijar un número máximo que es modificable, permitiendo aumentar las categorias a usar para generar la llave en caso de que se quiera hacer más complejo al algoritmo o incluir otras categorías.
