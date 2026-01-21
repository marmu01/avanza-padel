import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(page_title="Avanza Pádel Hub", layout="wide")

st.title("🎾 Avanza Pádel: Sistema de Gestión Integrado")
st.sidebar.header("Filtros de Control")
periodo = st.sidebar.selectbox("Seleccionar Período", ["Enero 2025", "Q1 2025", "Anual 2025"])

# TABS PRINCIPALES (Las 3 Herramientas)
tab_bsc, tab_okr, tab_piramide = st.tabs([
    "📊 BSC (Visión Anual)", 
    "🎯 OKR (Visión Trimestral)", 
    "🔺 Pirámide (Visión Mensual)"
])

# --- TAB 1: BALANCED SCORECARD (DIRECCIÓN GRUPO RECIO) ---
with tab_bsc:
    st.header("Balanced Scorecard - Dashboard Estratégico")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Ingresos Totales", "240.500 €", "+12%")
    col2.metric("EBITDA", "18%", "-2%")
    col3.metric("Ocupación Media", "68%", "+5%")
    col4.metric("NPS Cliente", "78/100", "+3")

    # Datos para gráfico de cumplimiento por perspectiva
    data_bsc = {
        'Perspectiva': ['Financiera', 'Cliente', 'Procesos', 'Aprendizaje'],
        'Cumplimiento (%)': [95, 88, 92, 75]
    }
    fig_bsc = px.bar(data_bsc, x='Perspectiva', y='Cumplimiento (%)', color='Cumplimiento (%)',
                     range_y=[0, 100], title="Estado de Objetivos Estratégicos")
    st.plotly_chart(fig_bsc, use_container_width=True)

# --- TAB 2: OKRS (ESCUELA DE PÁDEL Y STAFF) ---
with tab_okr:
    st.header("OKRs Q1 - Foco: Escuela de Pádel")
    
    with st.expander("Objetivo: Convertir la escuela en motor de recurrencia", expanded=True):
        st.write("**KR 1: Incrementar alumnos activos a 250**")
        st.progress(0.85, text="85% completado")
        
        st.write("**KR 2: Tasa de Churn (Bajas) inferior al 5%**")
        st.progress(0.95, text="Actual: 4.2% (Objetivo cumplido)")
        
        st.write("**KR 3: Realizar 2 Torneos 'Progresión' en el trimestre**")
        st.progress(0.50, text="1 de 2 realizados")

    st.info("💡 Tip para el Staff: Los alumnos de nivel 2.5 son los que más demandan partidos abiertos.")

# --- TAB 3: PIRÁMIDE DE RENDIMIENTO (CALIDAD OPERATIVA) ---
with tab_piramide:
    st.header("Pirámide de Rendimiento - Control de Calidad")
    
    col_izq, col_der = st.columns(2)
    
    with col_izq:
        st.subheader("Vértice: Calidad y Servicio")
        operativos = pd.DataFrame({
            'KPI Operativo': ['Limpieza de Cristales', 'Tensión de Redes', 'Temp. Nave', 'Atención Recepción'],
            'Estado': ['🟢 Óptimo', '🟢 Óptimo', '🟡 Revisar Clima', '🟢 Excelente']
        })
        st.table(operativos)

    with col_der:
        st.subheader("Eficiencia de Tiempos")
        tiempos = {
            'Categoría': ['Check-in', 'Mantenimiento', 'Resolución Quejas'],
            'Tiempo (min)': [2, 45, 120],
            'Meta (min)': [3, 60, 180]
        }
        fig_radar = px.line_polar(tiempos, r='Tiempo (min)', theta='Categoría', line_close=True)
        st.plotly_chart(fig_radar)

st.sidebar.markdown("---")
st.sidebar.write("✅ Datos actualizados desde Playtomic API")
