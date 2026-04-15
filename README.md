# Análisis Estadístico Pokémon.


# Introducción

En abril de 2013, un usuario del foro Neoseeker planteaba una duda que muchos jugadores novatos comparten al adentrarse en el mundo Pokémon: ¿los Pokémon legendarios son siempre mejores que los normales? Su inquietud reflejaba sus ganas de saber si estas criaturas excepcionales, por su rareza y relevancia en la trama, podrían poseer un rendimiento superior en combate. Más de una década después, la percepción no solo se ha mantenido, sino que se ha establecido: en la escena competitiva actual y en las partidas casuales, los entrenadores tienden de manera excesiva incluir a Pokémon legendarios en sus equipos, marginando a la gran mayoría de las especies regulares. La creencia generalizada sostiene que los legendarios cuentan con un Total de Estadísticas Base (BST) significativamente más alto y distribuciones de puntos más letales, lo que los convierte en la opción óptima para maximizar el rendimiento.

Sin embargo, esta tendencia plantea un riesgo importante para la salud del juego competitivo: si la superioridad estadística de los legendarios es absoluta, el metajuego se volverá cada vez más repetitivo y predecible, y los Pokémon no legendarios quedarían funcionalmente obsoletos. Esto afectaría negativamente la experiencia de quienes buscan creatividad, variedad estratégica y un equilibrio que permita construir equipos diversos. Ante este panorama, surge la necesidad de verificar de manera experimental si dicha superioridad es efectivamente generalizable a todas las variables estadísticas relevantes (Ataque, Defensa, Velocidad, PS, y Total_stats) o si, por el contrario, existen áreas donde los Pokémon comunes pueden competir o incluso superar a los legendarios.

El presente estudio se propone comparar el rendimiento estadístico de Pokémon legendarios y no legendarios utilizando exclusivamente la base de datos oficial de la EECA hasta la Novena Generación. A través de un análisis cuantitativo de las variables Total_stats, Speed, Type_1 e Is_Legendary, se busca determinar si la exclusividad de estas criaturas se traduce en una superioridad absoluta o si el tipo elemental y la especialización permiten que los Pokémon regulares sigan siendo competitivos.

# Estructura del Informe

Este documento técnico se encuentra organizado en cinco capítulos fundamentales que articulan la investigación desde el planteamiento del problema hasta la validación estadística de los datos:

**Capítulo I**, se presenta el origen de la investigación, enfocándose en la creencia común de que los Pokémon legendarios son siempre superiores. Aquí se definen los objetivos del estudio y se delimita el análisis a las nueve generaciones de datos disponibles hasta la actualidad.

**Capítulo II**, se establece el Marco Metodológico y los fundamentos del estudio. Se explican tanto los conceptos del juego como las herramientas estadísticas utilizadas (como el Z-score y la correlación biserial-puntual), que son las que permiten medir con precisión la brecha de poder entre las distintas categorías de Pokémon.

**Capítulo III**, se describe el Marco Metodológico, detallando el proceso técnico de la investigación. Se explica cómo se prepararon los datos en R y por qué se seleccionaron pruebas específicas, como la Prueba t de Welch, para asegurar que la comparación entre grupos de diferentes tamaños sea justa y válida.
 
**Capítulo IV**, se expone el Análisis de Resultados donde se exhiben las tablas y gráficos generados. Se analizan los hallazgos sobre la velocidad y el poder total, identificando a los Pokémon comunes que logran romper la regla de superioridad y competir directamente con 

**Capítulo V**, se presentan las Conclusiones y Recomendaciones. En este apartado se  sintetizan los descubrimientos más importantes y se propone una estrategia de selección de equipos basada en la eficiencia de las estadísticas, ayudando a los jugadores a tomar decisiones informadas.

Este reporte no solo busca ofrecer un diagnóstico estadístico sobre el equilibrio de poder en la franquicia, sino también consolidar una metodología técnica que pueda ser replicada para evaluar el balance y la eficiencia en diversos sistemas de personajes dentro de la industria del entretenimiento digital

# Planteamiento de Problema

En abril de 2013, el usuario **Darias (2013)** planteaba una interrogante fundamental sobre si los Pokémon legendarios eran naturalmente superiores a los normales, motivado por su reciente inicio en el juego. En la actualidad, se observa que los jugadores de Pokémon se inclinan abrumadoramente por utilizar Pokémon "Legendarios" en sus alineaciones, dejando de lado a la mayoría de los Pokémon regulares. Existe la certeza generalizada de que los Pokémon legendarios poseen un Total de Estadísticas Base significativamente superior y una distribución de puntos más letal frente a los Pokémon comunes; por lo tanto, como los jugadores buscan maximizar su rendimiento, eligen invariablemente estas criaturas por su aparente ventaja numérica.
Según esta tendencia de superioridad estadística, el juego competitivo se volverá cada vez más repetitivo y predecible, siendo posible que los Pokémon no legendarios queden completamente obsoletos, afectando negativamente la experiencia de los usuarios que buscan creatividad y variedad estratégica. Para demostrar este pronóstico, es necesario verificar estadísticamente si esta superioridad de los legendarios es absoluta en las variables (Ataque, Defensa, Velocidad, vida máxima y actual, generación, Total_stats) o si es solo un mito en ciertas áreas, para así brindar información verificada. El volumen de datos a estudiar se limitará exclusivamente a la base de datos de los Pokémon proporcionada por la EECA hasta la Novena Generación, analizando únicamente las variables mencionadas.
Con el fin de orientar a los nuevos usuarios en la toma de decisiones estratégicas basadas en datos y no solo en la popularidad de las criaturas, el presente estudio se guía por las siguientes preguntas de investigación:

 **1.** ¿Existen diferencias estadísticamente significativas en el Total de Estadísticas Base (Total_stats) entre los Pokémon legendarios y regulares a lo largo de las nueve generaciones?
 
 **2.** ¿Cuál es la proporción de Pokémon regulares cuya estadística de Velocidad (Speed) iguala o supera la media (o mediana) de los Pokémon legendarios?
 
 **3.** ¿Ha aumentado la brecha del Total de Estadísticas Base (Total_stats) entre Pokémon legendarios y regulares a medida que avanzan las generaciones (Generation)?

## Justificación

La presente investigación surge de la necesidad de evaluar críticamente el estado actual del balance competitivo entre los pokemones normales y los pokemones legendarios en el universo Pokémon según nuestra data ("29. Pokemon.csv"). Ante la percepción de que el juego se encamina hacia una homogeneidad donde solo las criaturas "Legendarias" tienen cabida, este estudio se justifica por la siguiente razón:
Utilidad Práctica para el Jugador Principiante: A menudo, los nuevos jugadores se ven limitados por la creencia de que la única vía hacia el éxito es la obtención de Pokémon legendarios. Esta investigación busca democratizar el acceso a la estrategia basada en datos, proporcionando una base sólida para que el principiante pueda elegir a sus compañeros de equipo no por su estatus de "mito", sino por su eficiencia estadística real. Identificar Pokémon comunes con estadísticas de Velocidad o Ataque superiores permite que el usuario optimice sus recursos desde las primeras etapas del juego.

## Objetivos
### Objetivo General
Determinar mediante un análisis estadístico comparativo si la supuesta superioridad competitiva de los Pokémon legendarios sobre los no legendarios es absoluta, evaluando sus estadísticas base y variables de rendimiento hasta la Novena Generación.
### Objetivos Específicos
**1.** Contrastar el promedio de las estadísticas base (Ataque, Defensa, Velocidad, Vida y Total_stats) de los Pokémon legendarios frente a los no legendarios para identificar brechas significativas de poder.

**2.** Identificar los ejemplares no legendarios que superan los umbrales de velocidad promedio de la categoría legendaria, con el fin de catalogar excepciones a la regla de superioridad estadística.

**3.** Evaluar la correlación entre la potencia de un Pokémon y sus variables determinantes (tipo elemental vs. condición de legendario) para establecer cuál factor tiene mayor incidencia en su desempeño letal.



 
  


