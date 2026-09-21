import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Previsão de Churn", page_icon="📊")
st.title("📊 Previsão de rotatividade de clientes - E-commerce")
st.write("Prevê se o cliente vai abandonar a loja.")

np.random.seed(42)
df = pd.DataFrame({
    'meses': np.random.randint(1, 60, 200),
    'compras': np.random.randint(1, 30, 200),
    'bilhete': np.random.randint(50, 1000, 200),
    'reclamacoes': np.random.randint(0, 5, 200),
})
df['churn'] = ((df['reclamacoes'] > 2) | (df['meses'] < 6)).astype(int)

modelo = RandomForestClassifier()
modelo.fit(df.drop('churn', axis=1), df['churn'])

st.subheader("Dados do Cliente")
compras = st.slider("Qtd de compras", 1, 30, 5)
meses = st.slider("Meses como cliente", 1, 60, 12)
bilhete = st.number_input("Ticket médio (R$)", 50, 1000, 200)
reclama = st.slider("Reclamações", 0, 5, 0)

if st.button("PREVER AGORA"):
    prob = modelo.predict_proba([[meses, compras, bilhete, reclama]])[0][1]
    st.metric("Risco de Churn", f"{prob*100:.1f}%")
    if prob > 0.5:
        st.error("⚠️ ALTO RISCO de rotatividade!")
    else:
        st.success("✅ Cliente FIEL! Baixo risco.")



