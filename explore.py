import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 


name_dataset = pd.read_csv('titlerating.csv')
# Chargement des datasets disponibles