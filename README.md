# ProyectoFinalBI

Análisis de Sentimientos Mundial GRUPO 1 
• Participantes: 
-Álvarez Miguel 
-Salazar Javier 
Objetivo General Implementar e investigar el funcionamiento de un clasificador de sentimientos utilizando los algoritmos de aprendizaje vistos en clase y los datos recolectados de Twitter para identificar tendencias de opinión en los 20 países que participaron en el mundial a partir del 28 de junio del 2018. 

*Herramientas 
-CouchDb
-Pycharm
-Phyton
-Ubuntu
-16.04 • Método: 
Para el desarrollo de este proyecto se utilizó la api de twitter para recolectar los twitters y guardarlos en una base de datos noSql
(CouchDB), para el análisis de sentimientos se filtro los datos para obtener solo twitters que esten relacionados al mundial y eliminar los enlaces, tags, hashtags, emojis, etc y traducir los twitters al inglés para luego etiquetarlos en positivos, negativos o neutros, con esto pudimos implementar naiveBayes para clasificar los datos utilizando para ello un json de entrenamiento y testeo. 
Información recopilada de los tweets de los partidos de los equipos que clasificaron al mundial 2018. Los partidos que se van a analizar son: Francia vs Argentina,Uruguay vs Portugal, Bélgica vs Inglaterra, Francia vs Croacia. 
Después se procedió a analizar los datos: 
-Tweets por hora del día (barras) 
-Tweets por fecha 
-Tweets por idioma (barras) 
-Porcentaje de sentimientos (pastel) 
-Tweets por país 
-Tweets (relacionados al mundial) por país 
• Resultados 
-El análisis de sentimientos tanto en los países que ganaron el partido como los que no, tienen más tweets positivos que negativos, con excepción de Portugal. 
-La mayor cantidad de tweets se realizaban durante el partido en los respectivos países. 
-La fecha con la mayor cantidad de tweets realizados fue el domingo 15 de julio, es decir la final del mundial de rusia 2018. 
-Aún con la gran cantidad de tweets recolectados una vez filtrados solo los tweets del mundial eran pocos en comparación con el total.
• Conclusiones y trabajo futuro 
-NaiveBayes, no nos brindo un buen resultado (quizá por la cantidad de los datos utilizados en el entrenamiento), por lo que recomendamos utilizar otra técnica de clasificación, como red neuronal o arboles de decisión. El análisis de sentimientos es muy útil si una empresa quiere indagar el grado de aceptación que tiene entre sus clientes, incluso plantear estrategias para identificar y conseguir fieles usuarios. Cómo trabajo futuro seria una mejor implementación para clasificar los sentimientos, analizar que países son los más sentimentales en cuanto al fútbol y planear estrategias de marketing y publicidad en los mismos. • Apéndice: instrucciones de instalación y funcionamiento 
herramientas: 
Instalar python y couchdb para windows 10 recolectar los tweets utilizando las librerias tweepy de python.
- Utilizar las vistas para filtrar los datos del mundial y etiquetarlos con el programa EtiquetadoAS.py
- Clasificar con naiveBayes (clasificadorTwitters.py) 
- Ejecutar los demás programas para obtener los datos y gráficos.
