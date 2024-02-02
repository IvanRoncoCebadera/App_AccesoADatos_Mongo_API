# Decisiones tecnológicas

## Índice
1. [***¿Por que MongoDB?***](##¿Por-que-MongoDB?)

2. [***¿Por que Python?***](##¿Por-que-Python?)
  
## ¿Por que MongoDB?

### Según las inventigaciones que he realizado, he conseguido concluir las siguientes razones de porque usar MongoDB:
 - Ofrece un modelo de datos flexible (generalmente en fromato BSON y con representación en JSON). Esto es muy util para poder escalar la aplicación en un futuro.
 - Por lo que tengo entendido, ofrece un muy buen rendimiento a la hora de realizar multiples consultas rápidas de lectura/escritura.
 - Luego tenemos una de las razones más obvias, y desde luego mí favorita. Al ser muy muy utilizada, existén una cantidad gigantesca de guías y ayudas, ademas de tener una comunidad muy grande sobre la que seguro uno se puede apoyar.
  
### Mientras hacía la investigación sobre MongoDB, me percaté de una cosa. Aun no se de que irá la aplicación que haremos, por eso hice un listado con cosas muy genéricas. 
### Al tratar de informarme más, me dí cuenta de algo. Muchisima gente simepre comentaba cosas como: "...al final, todo depende de para que vayas a usar la BBDD..." o "...dependiendo del caso, es mejor una u otra...", debido a esta incertidumbre, decidí mirar otras opciones de BBDD NoSQL, junto con alguna característica destacable:
 - Cassandra: Destaca por tener una alta disponibilidad, y al igual de MongoDB, una alta escalabilidad y rendimiento.
 - Amazon DynamoDB: Es una base de datos gestionada a través de AWS. Ofrece una alta durabilidad y disponiblidad, al igual que la opción de que escale con el tiempo.
 - Couchbase: que al igual que las anteriores ofrece rendimiento, escalabilidad y para destacar, permite transacciones ACID.

### Al final, llegué a la siguiente conclusión, debido al tamaño más que probablemente reducido que tendrá nuestra app, y que los apartados de distribución, disponibilidad y tal, me son algo irelevantes. Pues la mejor opción se me hace que es MongoDB, y es por nada más y nada menos que, todas las guía y la gran comunidad que tiene.

## ¿Por que Python?

### En el caso de la elección de Python sobre cualquier otro lenguaje, las cosas son algo más simples. Primero estas son las razones por la que me quedaría con Python:
 - Es el lenguaje más usado actualmente!! Eso implicá guías y gran comunidad (¡me gusta!).
 - Ofrece una sintaxis muy clara, lo que apoya a que tenga una curva de aprendizaje muy suave.
 - Es un nuevo lenguaje a utilizar. Esto ya es personal, pero prefiero aprender un lenguaje nuevo si se puede, en vez de usar el mismo una y otra vez.
 - Las bibliotecas. Al ser el lenguaje más usado actualmente, tiene casi cualquier biblioteca imaginable y por lo general, bastante bien adaptadas.

### Sin embargo, no todo es de color de rosa bajo mi punto de vista y es que Python es uno de los lenguajes más pesados. Ademas de que no puedes definir el tipo de las variables, pues lo puedes cambiar en cualquier momento, pero por lo demas no hay más quejas.

### Por último, si tuviera que ofrecer alguna otra opción de lenguaje sería:
 - Java.
 - Kotlin.
 - C/C++/C#.
### Las razones de esto son bastante simples de hecho, son lenguajes que conozco y se que son muy usados, ademas de que tienen detalles que me gustan más que Python.

### Por último, con respecto a los lenguajes de programación y como se usan especificamente para una cosa u otra, no voy a entrar en ese tema, ya que no se sobre que será la aplicación.