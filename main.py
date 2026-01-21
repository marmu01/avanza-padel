import streamlit as st
import pandas as pd
import plotly.express as px

# 1. CONFIGURACIÓN VISUAL Y COLORES CORPORATIVOS
st.set_page_config(page_title="Avanza Pádel - Gestión Pro", layout="wide")
# Estilo CSS para personalizar la interfaz (Colores: Negro, Gris Oscuro, Verde Pádel)
st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    .stMetric { background-color: #1A1C23; padding: 20px; border-radius: 10px; border-left: 5px solid #CCFF00; }
    div[data-baseweb="tab-list"] { gap: 20px; }
    button[data-baseweb="tab"] { font-size: 18px; font-weight: bold; }
    .stProgress > div > div > div > div { background-color: #CCFF00; }
    </style>
    """, unsafe_allow_html=True)

# 2. CARGA DE DATOS
@st.cache_data
def load_data():
    # En producción, esto vendría del CSV o Google Sheets del cliente
    data = {
        'herramienta': ['BSC', 'BSC', 'BSC', 'OKR', 'OKR', 'OKR', 'PIRAMIDE', 'PIRAMIDE', 'PIRAMIDE'],
        'indicador': ['EBITDA Anual', 'Ingresos Totales', 'Ocupación Media', 'Alumnos Escuela', 'Tasa Retención', 'Eventos Q1', 'Limpieza Pistas', 'Mantenimiento', 'Climatización'],
        'valor_actual': [18, 240500, 68, 210, 95, 2, 98, 45, 22],
        'meta': [20, 250000, 70, 250, 90, 3, 100, 60, 21],
        'unidad': ['%', '€', '%', 'alumnos', '%', 'torneos', '%', 'min', 'ºC']
    }
    return pd.DataFrame(data)

df = load_data()

# 3. CABECERA Y SELECCIÓN DE PERIODO
st.title("AVANZA PÁDEL | Management Hub")
periodo_seleccionado = st.select_slider(
    "Seleccione el periodo de análisis para el reporte:",
    options=["Mensual (Operativo)", "Trimestral (Táctico)", "Anual (Estratégico)"],
    value="Anual (Estratégico)"
)

st.divider()

# 4. ÁREAS DEL MODELO DE GESTIÓN
tab_bsc, tab_okr, tab_piramide = st.tabs(["ESTRATEGIA (BSC)", "ESCUELA (OKR)", "OPERACIONES (PIRÁMIDE)"])

# --- TAB 1: ESTRATEGIA (BSC) ---
with tab_bsc:
    st.subheader("Cuadro de Mando Integral - Visión de Negocio")
    st.info("💡 **Ayuda al Gestor:** Esta vista permite al Grupo Recio evaluar la rentabilidad a largo plazo. Si el EBITDA se desvía, revise los costes fijos en la pestaña de Operaciones.")
    
    bsc_data = df[df['herramienta'] == 'BSC']
    m1, m2, m3 = st.columns(3)
    metrics = [m1, m2, m3]
    
    for i, row in bsc_data.reset_index().iterrows():
        delta = row['valor_actual'] - row['meta']
        metrics[i].metric(label=row['indicador'], value=f"{row['valor_actual']}{row['unidad']}", delta=f"{delta}{row['unidad']}")
    
    fig_bsc = px.line(bsc_data, x="indicador", y="valor_actual", markers=True, 
                      title="Tendencia de Rendimiento Estratégico").update_traces(line_color='#CCFF00')
    st.plotly_chart(fig_bsc, use_container_width=True)

# --- TAB 2: ESCUELA (OKR) ---
with tab_okr:
    st.subheader("Objetivos y Resultados Clave - Escuela de Pádel")
    st.info("💡 **Ayuda al Gestor:** Los OKRs miden el crecimiento trimestral. El foco actual es la fidelización de alumnos para asegurar ingresos recurrentes.")
    
    okr_data = df[df['herramienta'] == 'OKR']
    for _, row in okr_data.iterrows():
        progreso = min(row['valor_actual'] / row['meta'], 1.0)
        col_txt, col_bar = st.columns([1, 3])
        col_txt.write(f"**{row['indicador']}**")
        col_bar.progress(progreso, text=f"{int(progreso*100)}% del objetivo")

# --- TAB 3: OPERACIONES (PIRÁMIDE) ---
with tab_piramide:
    st.subheader("Pirámide de Rendimiento - Estándares de Calidad")
    st.info("💡 **Ayuda al Gestor:** Evalúe aquí el 'Día a Día'. La calidad de las pistas es el activo principal de Avanza. Un fallo aquí afecta directamente a la retención de clientes.")
    
    pir_data = df[df['herramienta'] == 'PIRAMIDE']
    
    # Visualización mediante tabla de alta densidad
    st.dataframe(pir_data[['indicador', 'valor_actual', 'meta', 'unidad']], use_container_width=True)
    
    if pir_data.iloc[1]['valor_actual'] > pir_data.iloc[1]['meta']:
        st.warning("⚠️ ALERTA: El tiempo de mantenimiento está excediendo la meta. Riesgo de pérdida de reservas.")

st.markdown("---")
st.caption("Propiedad de Grupo Recio - Sistema de Gestión Avanzada v2.0")
