import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Previsão de Churn", page_icon="📉")
st.title("📉 Previsão de rotatividade de clientes - E-commerce")
st.write("Prevê se o cliente vai abandonar a loja.")

np.random.seed(42)
df = pd.DataFrame({
'meses': np.random.randint(1, 60, 200),
'compras': np.random.randint(1, 30, 200),
'bilhete': np.random.randint(50, 1000, 200),
'reclamações': np.random.randint(0, 5, 200),
})
df['churn'] = ((df['reclamacoes'] > 2) | (df['meses'] < 6)).astype(int)

modelo = RandomForestClassifier()
model.fit(df.drop('churn', axis=1), df['churn'])

st.subheader("Dados do Cliente")
meses = st.slider("Mesas como cliente", 1, 60, 12)
compras = st.number_input("Qtd de compras", 1, 50, 5)
bilhete = st.number_input("Ticket médio R$", 10, 2000, 150)
reclamar = st.slider("Reclamações", 0, 10, 1)

se st.button("PREVER AGORA"):
prob = model.predict_proba([[meses, compras, ticket, reclama]])[0][1]
se prob > 0,5:
st.error(f"⚠️ ALTO RISCO de rotatividade! {prob*100:.1f}%")
outro:
st.success(f"✅ Cliente FIEL! Risco de {prob*10
