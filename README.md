#SCAV
#P1
#Daniel Mateos Manjón
#U150004   NIA:205514

#Ej 1

En el archivo run_lenght.py se puede observar dos funciones de conversión de rgb a yuv y viceversa y imprimimos por pantalla una demostración de como aplicando ambas simultáneamente obtenemos el input original.
Las funciones son copias ligeramente modificadas del siguiente link: https://gist.github.com/Quasimondo/c3590226c924a06b276d606f4f189639


#Ej 2

En la captura P1_ej2.png se muestra como realizamos la reducción de pixeles de la imagen Lenna.png a Lenna100x100.png. Se puede observar la cantidad de pixeles de ambas en las propiedades de la captura P1_ej2.2.png

#Ej 3

En la captura P1_ej3.png se puede observar la línea de comando para transfomar la Imagen de Lenna.png a su versión en blanco y negro LennaBW.png


#Ej 4

El código run_lenght.py para codificar secuencias binarias fue cambiado de uno encontrado en internet (https://www.geeksforgeeks.org/run-length-encoding-python/), pero modificado para que solo pueda codificar valores binarios y en caso opuesto avisar con un print.
También fue modificado para que el output codificado indique los 0 como 'A' y los 1 como 'B', ya que podría darse casos al decodificar strings con diversas posibilidades como por ejemplo "1011", no sabríamos si es un uno y un cero o 101 unos, de esta manera al decodificar no habrá confusión posible.

#Ej 5

En el archivo dct.py se toma un input y se le aplica la función de dct de la libreria scipy.
