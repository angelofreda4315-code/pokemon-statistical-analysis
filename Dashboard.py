import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv("29. Pokemon.csv")
st.set_page_config(page_title="mi APP análisis estadístico Pokémon", page_icon=":guardsman:", layout="wide", initial_sidebar_state="collapsed")
def main():
    st.title("análisis estadístico Pokémon")
    st.header("Bienvenido al análisis estadístico de Pokémon")
    st.header("dataframe:")
    st.dataframe(df)
    st.sidebar.header("Analisis")
    st.subheader("Información General de los Pokémon")
    df_count = df.groupby("Type_1").count().reset_index()
    fig = px.pie(df_count, values="Total_Stats", names="Type_1", title="Tipos de Pokémon con sus estadísticas importantes totales")
    st.plotly_chart(fig)

    st.subheader("Información de los Pokémon Legendarios")
    df_count2 = df.groupby("Is_Legendary").count().reset_index()
    fig2 = px.pie(df_count2, values="Total_Stats", names="Is_Legendary", title="Distribución de Pokémon legendarios")
    st.plotly_chart(fig2)
    
    df_prom = df.groupby("Type_1")["Total_Stats"].mean().reset_index()
    fig3 = px.bar(df_prom, x="Type_1", y="Total_Stats", title="Promedio de Estadísticas importantes por Tipo de Pokémon", color="Total_Stats", color_continuous_scale="Viridis")
    st.plotly_chart(fig3)
if __name__ == "__main__":
    main()