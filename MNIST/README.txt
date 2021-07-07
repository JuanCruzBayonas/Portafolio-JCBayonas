MNIST es una base de datos con 70 mil capturas de dígitos escritos a mano, del 0 al 9.  La misma fue creada en su momento por empleados del *US Census Bureau* de Estados Unidos y por estudiantes con el objetivo de crear un sistema capaz de reconocer los números de los códigos postales.   

Se debe identificar correctamente nuevos dígitos escritos a mano. Los datos son:

- 60 mil imágenes previamente clasificados con su correspondiente etiqueta (0-9)
- 10 mil imágenes sin etiquetar

Todas las imágenes tienen una resolución de 28x28 pixels y están en escala de grises

**Primera Parte:** 

1- Visualizar las imágenes: debe instrumentar alguna manera que nos permita ver las imágenes. Se debe mostrar la imagen y la correspondiente etiqueta

2- Generar el modelo de **produccion_1**. Para ello deberá efectuar selección de modelo entre los de **Machine Learning Clásico y Redes Neuronales eligiendo el que considere que funcionará mejor**.     

3- Con el modelo de Producción_1 deberá efectuar etiquetar las 10 mil imágenes provistas. Guarde las 10 mil etiquetas generadas como un array de numpy. 

4- La métrica será Accuracy.   

**Segunda Parte**:  

Luego de observar las imágenes, Ud supone que algunos pixels de la misma tienen poca relevancia para determinar qué número está escrito en ellas. 

1- Se deberá generar un conjunto de **a lo sumo 200 pixels aproximados** con los cuales deberá repetir la primera parte.  
2- Al modelo de producción de esta segunda parte deberá llamarlo **produccion_2**  
3- Deberá comparar los resultados obtenidos con los anteriores y anotar cómo funciona mejor.   
4- Finalmente con produccion_2 deberá etiquetar las 10 mil imágenes y guardar las etiquetas.