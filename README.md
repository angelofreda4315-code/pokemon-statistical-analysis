# análisis estadístico Pokémon.

## Planteamiento de problema.
Darias en abril del 2013 se preguntaba si los pokemones legendarios siempre eran mejor que los normales porque el y su amigo estaban empezando el juego(https://www.neoseeker.com/forums/21237/t1852213-need-some-clarification/). En la actualidad podemos observar es que los jugadores de pokémon se inclinan abrumadoramente por utilizar Pokémon "Legendarios" en sus alineaciones, dejando de lado a la mayoría de los Pokémon regulares. Existe la certeza generalizada de que los Pokémon legendarios poseen un Total de Estadísticas Base significativamente superior y una distribución de puntos más letal frente a los Pokémon comunes entoces como los jugadores estan buscando maximizar su rendimiento, eligen invariablemente estas criaturas por su aparente ventaja numérica. Según esta tendencia de superioridad estadística el juego competitivo se volverá cada vez más repetitivo y predecible y es posible que los Pokémon no legendarios queden completamente obsoletos, afectando negativamente la experiencia de los jugadores que buscan creatividad y variedad estratégica. para demostrar este pronostico, es necesario verificar estadísticamente si esta superioridad de los legendarios es absoluta en las variables (Ataque, Defensa, Velocidad, vida máxima y actual, generación, Total_stats) o si es solo un mito en ciertas áreas, Para asi dar información verificada. El volumen de datos a estudiar se limitará exclusivamente a la base de datos de los pokemon dadas por la EECA hasta la Novena Generación, analizando únicamente las variables mensionadas.

La investigación ayuda a principiantes, a elegir mejor sus pokémon con base estadistica. Debido a esto, se plantea las siguientes preguntas de investigación:

### 1) ¿Los pokémon legendarios son superiores estadisticamente segun el total de estadísticas base (BST)? en las generaciones de la data, usando las variables "Total_stats" y "Is_Legendary".

### 2) ¿Qué tan común es encontrar Pokémon normales que sean igual de rápidos o incluso más veloces que los legendarios? en las generaciones de la data, usando las variables "Speed" y "Is_Legendary".

### 3) ¿Influye más el "elemento" del Pokémon (Fuego, Agua, etc.) en su fuerza total que el hecho de ser o no un legendario? en las generaciones de la data, usando las variables "Type_1", "Is_Legendary" y "Total_Stats".

## **objetivo General**
- Comparar el rendimiendo estadistico de los Pokémones legendarios y los que no legendarios en las generaciones pokémon.

## **objetivos especificos**
- Comparar a los legendarios y no legendarios con el promedio de las estadísticas más importantes.
- Encontrar cuales son esos pokémones que logran ser más rapidos que los legendarios.
- Analizar si lo que hace fuerte al pokémon normalmente es su tipo o porque es legendario.

## **Justificación**
La presente investigación surge de la necesidad de evaluar críticamente el estado actual del balance competitivo entre los pokemones normales y los pokemones legendarios en el universo Pokémon según nuestra data("X29_pokemon"). Ante la percepción de que el juego se encamina hacia una homogeneidad donde solo las criaturas "Legendarias" tienen cabida, este estudio se justifica por la siguiente razón:

Utilidad Práctica para el Jugador Principiante: A menudo, los nuevos jugadores se ven limitados por la creencia de que la única vía hacia el éxito es la obtención de Pokémon legendarios. Esta investigación busca democratizar el acceso a la estrategia basada en datos, proporcionando una base sólida para que el principiante pueda elegir a sus compañeros de equipo no por su estatus de "mito", sino por su eficiencia estadística real. Identificar Pokémon comunes con estadísticas de Velocidad o Ataque superiores permite que el usuario optimice sus recursos desde las primeras etapas del juego.

