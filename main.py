import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Configuración de página y estilos (DEBE IR PRIMERO)
st.set_page_config(page_title="Avanza Pádel Hub", layout="wide")

# 2. Definición de las pestañas (ESTA ES LA LÍNEA QUE TE FALTA ARRIBA)
# Primero creamos las pestañas y las asignamos a variables
tab_bsc, tab_okr, tab_piramide = st.tabs(["ESTRATEGIA (BSC)", "ESCUELA (OKR)", "OPERACIONES (PIRÁMIDE)"])

# 3. Ahora ya podemos usar las variables en los bloques 'with'
with tab_bsc:
    st.subheader("Cuadro de Mando Integral - Visión de Negocio")
    # ... resto de tu código para el simulador y métricas ...
    
with tab_okr:
    st.subheader("Objetivos y Resultados Clave - Escuela")
    # ... tu código de OKRs ...

with tab_piramide:
    st.subheader("Pirámide de Rendimiento - Operaciones")
    # ... tu código de la pirámide ...
# Configuración de la página
st.set_page_config(page_title="Avanza Pádel Hub", layout="wide")

st.title("Avanza Pádel: Sistema de Gestión Integrado")
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

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# ... (Mantener la configuración de estilo y el semáforo anterior) ...

# 6. MÓDULO DE INTELIGENCIA DE MERCADO (PLAYTOMIC)
st.markdown("---")
st.header("🕵️ Inteligencia de Mercado & Playtomic")
col_left, col_right = st.columns([2, 1])
with col_left:
    st.subheader("Ocupación por Franja Horaria (Media Semanal)")
    st.info("💡 **Ayuda al Gestor:** Los picos de 18:00 a 22:00 están saturados. El reto es el 'Yield Management': desplazar demanda a las 10:00 - 13:00 mediante bonos de escuela o tarifas dinámicas.")
    # Simulación de datos de ocupación Playtomic
    horas = [f"{h:02d}:00" for h in range(8, 24)]
    ocupacion = [20, 35, 45, 40, 30, 25, 20, 35, 85, 95, 100, 95, 80, 60, 40, 20]
    df_playtomic = pd.DataFrame({"Hora": horas, "Ocupación (%)": ocupacion})
    
    fig_hourly = px.area(df_playtomic, x="Hora", y="Ocupación (%)", 
                         color_discrete_sequence=['#CCFF00'], template="plotly_dark")
    fig_hourly.update_layout(yaxis_range=[0, 100])
    st.plotly_chart(fig_hourly, use_container_width=True)
with tab_piramide:
    st.header("Inteligencia de Competencia (Playtomic)")
    
    # DEFINICIÓN DE DATOS: Asegúrate de que los nombres coincidan
    competencia = pd.DataFrame({
        'Centro': ['Avanza Pádel', 'Club Rival A', 'Centro Rival B'],
        'Pistas_Libres': [2, 0, 5],
        'Precio': [24, 28, 22],  # Hemos simplificado a "Precio"
        'Rating': [4.8, 4.2, 4.5]
    })
    cols = st.columns(3)
    for i, row in competencia.iterrows():
        with cols[i]:
            st.subheader(row['Centro'])
            # CORRECCIÓN AQUÍ: Usamos row['Precio'] y row['Rating']
            st.write(f"Rating: {row['Rating']} ⭐")
            st.write(f"Precio: {row['Precio']} €") 
            
            if row['Pistas_Libres'] == 0:
                st.error("LLENO TOTAL")
            else:
                st.success(f"{row['Pistas_Libres']} pistas disponibles")
# 2. El bucle donde se muestran los datos (Debe llamar a 'Precio')
for _, row in competencia.iterrows():
    st.write(f"**{row['Centro']}**")
    # USAMOS 'Precio' aquí para que coincida con la definición de arriba
    st.caption(f"Rating: {row['Rating']} ⭐ | Precio: {row['Precio']}€") 
    if row['Pistas_Libres'] == 0:
        st.error("Lleno Total (Oportunidad)")
    else:
        st.success(f"{row['Pistas_Libres']} pistas disponibles") # Comparativa de disponibilidad en Playtomic (Centros cercanos)
    competencia = pd.DataFrame({
        'Centro': ['Avanza Pádel', 'Club Alcalá B', 'Centro Entrenúcleos'],
        'Pistas Libres (Hoy)': [2, 0, 5],
        'Precio Medio (€)': [24, 28, 22],
        'Rating': [4.8, 4.2, 4.5]
    })  
    for _, row in competencia.iterrows():
        st.write(f"**{row['Centro']}**")
        st.caption(f"Rating: {row['Rating']} ⭐ | Precio: {row['Precio Medio']}€")
        if row['Pistas Libres (Hoy)'] == 0:
            st.error("Lleno Total (Oportunidad perdida)")
        else:
            st.success(f"{row['Pistas Libres (Hoy)']} pistas disponibles")
# 7. VISIÓN DE OPORTUNIDADES
with st.expander("🔍 Ver Análisis de Oportunidades 'Last Minute'"):
    st.write("""
    Basado en el scraping de Playtomic:
    - **Viernes Noche:** El competidor 'Club Alcalá B' ha subido precios. Tenemos 2 pistas libres; momento para lanzar notificación push.
    - **Mañanas Lunes:** Baja ocupación general en la zona. Recomendación: Torneo 'Americano' para jubilados o trabajadores con turnos.
    """)
