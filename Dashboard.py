import streamlit as st
import pandas as pd
df = pd.read_csv("29. Pokemon.csv")

def main():
    st.title("análisis estadístico Pokémon")
    st.header("Bienvenido al análisis estadístico de Pokémon")
    st.header("dataframe:")
    st.dataframe(df)
    
  
    
if __name__ == "__main__":
    main()