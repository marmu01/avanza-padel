import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración
st.set_page_config(page_title="Avanza Pádel Hub", layout="wide")

# Carga de datos (Simulando la base de datos del cliente)
@st.cache_data
def load_data():
    return pd.read_csv("data_gestion.csv")

df = load_data()

st.title("🎾 Avanza Pádel: Centro de Control de Gestión")
st.markdown("---")

# --- TABS PARA LAS TRES HERRAMIENTAS ---
tab1, tab2, tab3 = st.tabs(["📊 Estrategia (BSC)", "🎯 Táctica (OKR)", "🔺 Calidad (Pirámide)"])

# 1. BALANCED SCORECARD (Visión Grupo Recio)
with tab1:
    st.header("Balanced Scorecard - Seguimiento Anual")
    bsc_data = df[df['herramienta'] == 'BSC']
    cols = st.columns(len(bsc_data))
    for i, row in bsc_data.iterrows():
        delta = row['valor_actual'] - row['meta']
        cols[i % len(bsc_data)].metric(
            label=row['indicador'],
            value=f"{row['valor_actual']} {row['unidad']}",
            delta=f"{delta} {row['unidad']}"
        )
    
    fig = px.bar(bsc_data, x="indicador", y="valor_actual", color="indicador", title="Cumplimiento de Objetivos Anuales")
    st.plotly_chart(fig, use_container_width=True)

# 2. OKRs (Gestión de la Escuela)
with tab2:
    st.header("OKRs Trimestrales - Foco: Escuela y Comunidad")
    okr_data = df[df['herramienta'] == 'OKR']
    for _, row in okr_data.iterrows():
        progreso = min(row['valor_actual'] / row['meta'], 1.0)
        st.write(f"**{row['indicador']}** ({row['valor_actual']} / {row['meta']} {row['unidad']})")
        st.progress(progreso)

# 3. PIRÁMIDE DE RENDIMIENTO (Operaciones Diarias)
with tab3:
    st.header("Pirámide de Rendimiento - Estándares de Calidad")
    pir_data = df[df['herramienta'] == 'PIRAMIDE']
    st.table(pir_data[['indicador', 'valor_actual', 'meta', 'unidad']])
    st.info("💡 Estos datos deben ser validados semanalmente por el gestor de pista.")
