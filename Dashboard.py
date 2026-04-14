import streamlit as st
import pandas as pd
import plotly.express as px

# ----- Configuración rápida -----
st.set_page_config(page_title="Estadísticas Pokémon", page_icon="🔥", layout="wide") #configura el título y el diseño de la página

#coloco dos imagenes
with st.sidebar:
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png", width=100)
    with col2:
        st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/257.png", width=100)

st.sidebar.title("🎮 pokemenu")

# ----- Cargar datos (solo una vez) -----
@st.cache_data
def cargar():
    datos = pd.read_csv("29. Pokemon.csv")
    datos['Is_Legendary'] = datos['Is_Legendary'].astype(bool)
    return datos

datos = cargar()

# ----- Filtros en la barra lateral -----
generaciones = sorted(datos['Generation'].unique())
tipo_elegido = st.sidebar.multiselect("Generación", generaciones, default=generaciones)

tipos = sorted(datos['Type_1'].dropna().unique())
tipo_primario = st.sidebar.multiselect("Tipo primario", tipos, default=tipos)

leyenda_filtro = st.sidebar.radio("Mostrar", ["Todos", "Solo Legendarios", "Solo No Legendarios"])

# ----- Filtro de rango de Total_Stats (slider continuo) -----
min_stats = int(datos['Total_Stats'].min())
max_stats = int(datos['Total_Stats'].max())
rango_total = st.sidebar.slider(
    "Rango de Total_Stats",
    min_value=min_stats,
    max_value=max_stats, value=(min_stats, max_stats), step=10, format="%d pts")
# ----- Aplicar filtros -----
mascara = (datos['Generation'].isin(tipo_elegido)) & (datos['Type_1'].isin(tipo_primario)) & (datos['Total_Stats'].between(rango_total[0], rango_total[1]))
if leyenda_filtro == "Solo Legendarios":
    mascara &= datos['Is_Legendary'] == True
elif leyenda_filtro == "Solo No Legendarios":
    mascara &= datos['Is_Legendary'] == False

filtrados = datos[mascara]


# ----- jamon de el dash -----
st.title("📈 ¿Los Pokémon legendarios son realmente superiores?") 

#----------------Pestañas----------------
tab1, tab2, tab3 = st.tabs(["📊Comparación general", "🏃Análisis de velocidad", "💪Fuerza normal y legendaria"])

#------------------------------------------------------
#-----------------------pestaña 1----------------------
#------------------------------------------------------
with tab1:
    #--------------primer punto----------------
    if len(filtrados) > 0:
        prom_leyenda = filtrados[filtrados['Is_Legendary']]['Total_Stats'].mean()
        prom_normal = filtrados[~filtrados['Is_Legendary']]['Total_Stats'].mean()
        diferencia = prom_leyenda - prom_normal
        porcentaje = (diferencia / prom_normal * 100) if prom_normal != 0 else 0
    else:
        prom_leyenda = prom_normal = diferencia = porcentaje = 0
        
        
    col1, col2, col3 = st.columns(3)
    col1.metric("Promedio Legendarios", f"{prom_leyenda:.1f}" if len(filtrados)>0 else "Sin datos")
    col2.metric("Promedio Normales", f"{prom_normal:.1f}" if len(filtrados)>0 else "Sin datos")
    
    st.markdown("📌 Conclusión: En promedio, los Pokémon legendarios tienen una fuerza total significativamente mayor que los normales. La diferencia porcentual muestra que los legendarios superan a los normales por un margen considerable, lo que refuerza la percepción común de que los legendarios son más poderosos en términos de estadísticas totales.")

# --- Indicador verde/rojo debajo de la diferencia ---
    if len(filtrados) > 0 and diferencia != 0:
        if diferencia > 0:
           delta_texto = f"🟢 +{porcentaje:.1f}% (Legendarios superiores)"
        else:
           delta_texto = f"🔴 {porcentaje:.1f}% (Normales superiores)"
        col3.metric("Diferencia", f"{diferencia:.1f} ({porcentaje:+.1f}%)", delta=delta_texto)
    else:
        col3.metric("Diferencia", "Sin datos")
        
#-----------------distribución del poder total----------------
    
    st.subheader("📦 Distribución del poder total")
    
    if len(filtrados) > 0:
        #creo dos columnas para mostrar los gráficos lado a lado
        col_izq,col_der=st.columns(2)
        
        with col_izq:
            legendarios_df = filtrados[filtrados['Is_Legendary']==True]
            if len(legendarios_df) > 0:
                fig_leg=px.box(legendarios_df,y="Total_Stats",title="Legendarios",points="all",color_discrete_sequence=["darkblue"], hover_data=["Name"])
                st.plotly_chart(fig_leg, use_container_width=True)
            else:
                st.info("No hay legendarios con estos filtros.")    
        with col_der:
             normales_df = filtrados[filtrados['Is_Legendary']==False]
             if len(normales_df) > 0:
                fig_norm=px.box(normales_df,y="Total_Stats",title="Normales",points="all",color_discrete_sequence=["lightgray"], hover_data=["Name"])
                st.plotly_chart(fig_norm, use_container_width=True)
             else:
                st.info("No hay normales con estos filtros.")
    else:
        st.warning("No hay datos disponibles para mostrar.")
        
        
#-----------------grafico:fuerza media por tipo----------------
    st.subheader("🌿 Fuerza media por tipo elemental")
    if len(filtrados) > 0:
        prom_tipo = filtrados.groupby("Type_1")["Total_Stats"].mean().reset_index()
        fig_tipo = px.bar(prom_tipo, x="Total_Stats", y="Type_1", orientation='h',title="Promedio de Total_Stats por tipo",
                         color="Total_Stats", color_continuous_scale="Viridis")
        fig_tipo.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_tipo, use_container_width=True)
        
        st.markdown("📌 Conclusión: El tipo elemental tiene un impacto significativo en la fuerza total de los Pokémon. Los tipos Dragón, Psíquico y Acero destacan por tener promedios de fuerza total más altos, lo que sugiere que estos tipos tienden a incluir Pokémon más poderosos. Por otro lado, tipos como Normal y Hada muestran promedios más bajos, indicando que suelen ser menos fuertes.")

#--------------------------------------------------------------------------
#-----------------------------segunda pestaña-----------------------------
#--------------------------------------------------------------------------
#-----------------------------segundo punto-----------------------------
with tab2:
    st.subheader("🏃 ¿Los normales pueden ser rápidos?")
    
    if len(filtrados) == 0:
        st.write("No hay datos disponibles para mostrar.")
    else:
        mediana_leyenda = filtrados[filtrados['Is_Legendary']]['Speed'].median()
        normales_rapidos = filtrados[~filtrados['Is_Legendary'] & (filtrados['Speed'] >= mediana_leyenda)]
        if len(filtrados[~filtrados['Is_Legendary']]) > 0:
            porc_rapidos = len(normales_rapidos) / len(filtrados[~filtrados['Is_Legendary']]) * 100
        else:
            porc_rapidos = 0
        st.metric("porcentaje de normales con velocidad mayor o igual a la mediana legendaria", f"{porc_rapidos:.1f}%")
        fig_vel = px.scatter(filtrados, x="Speed", y="Total_Stats", color="Is_Legendary",hover_data=["Name"], title="Velocidad vs Poder Total")
        st.plotly_chart(fig_vel, use_container_width=True)
        
        st.markdown("📌 Conclusión: Aunque los Pokémon legendarios tienden a ser más rápidos en promedio, existe un porcentaje significativo de Pokémon normales que igualan o superan la velocidad de la mediana legendaria. Esto indica que no exclusivamente de los legendarios siempre son mas fuertes y que algunos Pokémon normales pueden ser sorprendentemente rápidos.")
        
        st.subheader("📊 Top 10 normales más rápidos")
        top10 = normales_rapidos.nlargest(10, 'Speed')[['Name', 'Type_1', 'Speed', 'Total_Stats']]
        st.dataframe(top10, use_container_width=True)
        st.markdown("📌 Conclusión clave: Entre los Pokémon normales, hay varios que alcanzan velocidades impresionantes, con algunos superando la mediana de los legendarios como \"Ninjask\" que es el más rapido de los no legendario, aunque en general, los legendarios siguen dominando en términos de velocidad media.")
#--------------------------------------------------------------------------
#-----------------------------tercera pestaña-----------------------------
#--------------------------------------------------------------------------
with tab3:
    #------------------------mato el último punto------------------------
    st.subheader("💪 ¿El tipo elemental importa más que ser legendario?")
     # Calcular fuerza media por tipo y condición legendaria
    type_stats = datos.groupby(['Type_1', 'Is_Legendary'])['Total_Stats'].agg(['mean', 'count', 'std']).reset_index() #agrupa por tipo y condición legendaria, calcula la media, cuenta y desviación estándar de Total_Stats
    type_stats.columns = ['Tipo', 'Legendario', 'Fuerza_Media', 'Cantidad', 'Desv_Est'] #renombra las columnas para mayor claridad
    type_stats['Legendario'] = type_stats['Legendario'].map({True: 'Sí', False: 'No'}) #convierte la columna Legendario a texto para mejor visualización en el gráfico

    # Gráfico de barras agrupadas
    fig_bar = px.bar(type_stats, x="Tipo", y="Fuerza_Media", color="Legendario", #crea un gráfico de barras donde el eje x es el tipo, el eje y es la fuerza media, y las barras están coloreadas por condición legendaria
              barmode="group", title="Comparativa de Fuerza total", subtitle="Legendarios vs No Legendarios") #configura el modo de las barras para que estén agrupadas y establece el título del gráfico
    st.plotly_chart(fig_bar, use_container_width=True) # muestra el gráfico en la aplicación de Streamlit, ajustando su ancho al contenedor disponible
    
    st.markdown("📌 Conclusión: En casi todos los tipos elementales, los Pokémon legendarios tienen una fuerza media significativamente mayor que los no legendarios. Esto sugiere que ser legendario es un factor más determinante para la fuerza total que el tipo elemental en sí. Sin embargo, algunos tipos como Dragón y Acero destacan por tener valores altos incluso entre los no legendarios, aunque aún así no alcanzan a sus contrapartes legendarias.")
    
    st.subheader("📊 datos") #subtítulo para la sección de la tabla
    # Mostrar tabla estilo PDF
    st.dataframe(type_stats.sort_values("Fuerza_Media", ascending=False)) #muestra la tabla con la fuerza media por tipo y condición legendaria, ordenada de mayor a menor fuerza media
    
    st.markdown("📌 Conclusión:Los Pokémon legendarios siempre superan en fuerza media a los no legendarios, dentro de cada tipo elemental.El tipo Dragón (635 pts), Acero (613 pts) y Psíquico (562 pts) son los más poderosos entre los legendarios. Aunque algunos no legendarios alcanzan valores altos (como Dragón con 450 pts), ningún tipo común logra igualar a su contraparte legendaria, entonces Ser legendario es más determinante que el tipo elemental para tener una fuerza total alta.")
    
    
    
    
    
    
    
    
    
    
