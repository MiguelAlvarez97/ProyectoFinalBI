# ProyectoFinalBI
Analisis de Sentimientos Mundial GRUPO 1 

• Participantes:
    -Álvarez Miguel
    -Salazar Javier
• Método:
    Para el desarrollo de este proyecto se utilizó la api de twitter para recolectar los twitters y guardarlos en una base de datos noSql (CouchDB), para el analisis de sentimientos se necesito filtrar los datos para obtener solo twitters que esten relacionados al mundial y eliminar los enlaces, tags, hashtags, emojis, etc y traducir los twitters al inglés para luego etiquetarlos en positivos, negativos o neutros, con esto pudimos implementar naiveBayes para clasificar los datos utilizando para ello un json de entrenamiento y testeo. 
    Despues se procedio a analizar los datos:
      -Tweets por hora del día (barras)
      -Tweets por fecha
      -Tweets por idioma (barras)
      -Porcentaje de sentimientos (pastel)
      -Tweets por país
      -Tweets (relacionados al mundial) por país
• Resultados
  -El analisis de sentimientos tanto en los paises que ganaron el partido como los que no, tienen mas tweets positivos que negativos (con excepcion de portugal).
  -La mayor cantidad de tweets se realizaban durante el partido en los respectivos paises.
  -La fecha con la mayor cantidad de tweets realizados fue el domingo 15 de julio, es decir la final del mundial de rusia 2018.
  -Pese a la gran cantidad de tweets recolectados una vez filtrados solo los tweets del mundial eran pocos en comparacion con el total.
• Conclusiones y trabajo futuro
  -NaiveBayes no nos dio un buen resultado (quizá por la cantidad de los datos utilizados en el entrenamiento), por lo que recomendamos utilizar otra tecnica de clasificacion, como red neuronal o arboles de decisión.
  -El analisis de sentimientos es muy util si una empresa quiere averiguar el grado de aceptacion que tiene entre sus clientes, incluso plantear estragegias para identificar y conseguir fieles usuarios.
  -Como trabajo futuro seria una mejor implementacion para clasificar los sentimientos, analizar que paises son los mas sentimentales en cuanto al futbol y planear estrategias de marketing y publicidad en los mismos.
• Apéndice: instrucciones de instalación y funcionamiento
  herramientas:
    -instalar python y couchdb
    -recolectar los tweets utilizando las librerias tweepy de python
    -Utilizar las vistas apra filtrar los datos del mundial y etiquetarlos con el programa EtiquetadoAS.py
    -clasificar con naiveBayes (clasificadorTwitters.py)
    -ejecutar los demas programas para obtener los datos y graficos.
