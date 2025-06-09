import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 


name_dataset = pd.read_csv('titlerating.csv')
# Chargement des datasets disponibles
st.title("Exploration des données")
st.write("Sélectionnez un dataset pour l'explorer :")   

df = st.selectbox("Quel dataset veux-tu utiliser ?",name_dataset)

set = sns.load_dataset(df)

dfchoisi= set.columns.to_list()

st.dataframe(set)
st.write("Voici les colonnes disponibles dans le dataset :")
st.write(dfchoisi)