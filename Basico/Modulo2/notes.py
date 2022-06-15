print("La funcion 'print'")
#La palabra "print" es el nombre de una funcion. Eso no significa que dondequiera que aparezca esta palabra, 
#sera siempre el nombre de una funcion. El dignificado de la palabra proviene del contexto en el cual se 
#haya utilizado la palabra. La funciones de Python son mas flexibles y pueden contener mas que sus 
#parientes matematicos. Una funcion es una parte separada del codigo de computadora el cual es capaz de: 
# ---Causar algun efecto (crear un archivo), esto es algo inaudito en el mundo de las matematicas.
# ---Evaluar un valor (la raiz cuadrada de un valor x) y devolverlo como el resultado de una funcion, esto
#    lo que hace que las funciones de Python sean parientes de conceptos matematicos.
#Ademas muchas funciones de Python pueden hacer las dos cosas anteriores juntas.

print("De donde proviene las funciones?")
# ---Pueden venir de Python mismo. La funcion print es una de este tipo, dicha funcion es un valo agregado 
#   de Python junto con su entorno (esta integrada), no se tiene que hacer nada en especial para usarla.
# ---Puende provenir de uno o varios modulos de Python llamados complementos, alguno modulos vienen de Python, 
#    otros pueden requerir una instalacion con el codigo.
# ---Puedes escribirlas tu mismo, colocando tantas funciones como desees y necesites de su programa para hacerlo
#    mas simple, claro y elegante.
#El nombre de una funcion debe ser significativo, si vas a utilizar alguna funcion ya existente, no podras 
#modificar su nonbre, pero cuando comiences a escribir tus propias funciones, debes considerar cuidadosamente 
#la eleccion de nombres.

print("La funcion 'print' propiedades")
#Como se dijo anteriormente un funcion puede tener:
# Un efecto
# Un resultado 
#Tambien existe un tercer componente de la funcion, muy importante, el o los argumentos.
#Las funciones matematicas usualmente toman un argumento, por ejemplo sen(x) toma a x como argumento.
#Las funciones de Python por otro lado, son mas versatiles. Dependiendo de las necesodades individuales, pueden 
#aceptar cualquier numero de argumentos, tantos como sea necesario para realizar sus tareas.
#Las funciones en Python demandan forzosamente la presencia de un par de parentesis (el de apertura y de cierre).
#El unico argumento que tiene print en el ejemplo es una cedena ("Hola mundo!"), la cadena esta delimitada por 
#comillas forman la cadena, recortan una parte del codigo y le asignan un significado diferente.
#Casi cualquier cosa que ponga dentro de las comillas se tomaran de manera literal, no como codigo, sino como datos. 
#Existe mas de una forma de como especificar una cadena dentro del codigo de Python.

print("Semantica de las funciones")
#El nombre de la funcion junto con los parentesis y los argumentos, forman la invocacion de la funcion. 
#Que se cude cuando Python encuentra una invacacion como la que esta a continuacion? 
# nombre_funcion(argumento)
# ---Primero, Python comprueba si el nombre especificado es legal (explora sus datos internos para encontrar una 
#    funcion existente del nombre, si esta busqueda falla Python cancela el codigo).
# ---En segundo lugar, Python comprueba si los requisitos de la funcion para el numero de argumentos le permiten 
#    invocar la funcion de esta manera (ejemplo si una funcion exige dos argumentos y solo se le entrega uno se 
#    considerara erronea y abortara la ejecucion del codigo)
# ---Tercero, Python Python deja el codigo por un momento y salta dentro de la funcion que se desea invocar, 
#    por lo tanto, tambien toma los argumentos y los pasa a la funcion.
# ---Cuarto, la funcion ejecuta el codigo, provoca el efecto deseado, evalua el resultado deseado y termina la tarea.
# ---Finalmente, Python regresa al codigo (inmediatamente despues de la invocacion) y reanuda su ejecucion.

print("La cual es el efecto que causa la funcion?")
#El efecto es muy util.
# ---Toma los argumentos
# ---Los convierte en un formato legible para el ser humano si es necesario.
# ---Envia los datos resultante al dispositivo de salidam en otras palabras, cualquier cosa que se ponga en la funcion
#    print() se aparecera en la pantalla.

print("Que argumentos espera print()")
# Cualquiera. Puede operar con practicamente todos los tipos de datos ofrecidos por Python. Cadenas, numeros, caracteres, 
# valores logicos, objetos: cualquiera de estos se puede pasar con exito a print().

print("Que valor evalua la funcion print()")
#Ninguno. Su efecto es suficiente print() no evalua nada.

#La sintaxis de Python es bastante especifica en esta rea. A diferencia de la mayoria de los lenguajes de programacion,
#Python requiere que no haya mas de una instruccion por linea. Una linea puede estar vacia pero no debe contener dos, 
#tres o mas instrucciones. Esto esta estrictamente prohibido.

print("La Witsi Witsi Araña\nsubió a su telaraña.\n saltos de linea")
# La \n sirve para hacer un salto de linea, es decir que se crea un nueva linea. La palabra \n colocada despues de la barra 
# invertida proviene de la palabra newline (nueva linea). Tanto la barra \ como la n forman un simbolo especial denomindao 
# (caracter de nuiva liena) que incita a la consola a iniciar una nueva linea de salida.
# Si deseas colocar solo una barra invertida dentro de una cadena, no olvides su naturaleza de escape: tiene que ser duplicada.
# Lo siguiente cuasara un error print("\")
# Mientras que esta no lo hara print("\\")
# No todos los pares de escape significan algo. 

print("La funcion de print() usando multiples argumentos")
# print("La Witsi Witsi Araña" , "subió" , "a su telaraña.") hay una invocacion de la funcion print() pero contiene tres argumentos. 
# Todos ellos son cadenas. Los argumentos estan separados por comas. Se han rodeado de espacion para hacerlo mas visibbles, pero no 
# es realmente necsario. Las comas que separan los argumentos desempenan un papel completamente diferente a la coma dentro de la cadena.
# el primero es una parte de la sintaxis de Python, el segundo esta destinado a mostrarse en la consola.
# ---Una funcion print() invocada con mas de un argumento genera la salida en una sola linea.
# ---La funcion print() coloca un espacio entre los argumentos emitidos por iniciativa propia.


print("La funcion print() la manera de posicional de pasar argumentos")
#La forma en que pasemos los argumentos a la funcion print() es la mas comun en Python, y se denomina manera posicional (este nombre
# proviene del hecho de que el dignificado del argumento esta dictado por su posicion, por ejemplo, el segundo argumento se emitira 
# despues del primero, y no al reves).
 