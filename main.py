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
import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN Y ESTILO AVANZA PÁDEL
st.set_page_config(page_title="Avanza Pádel Hub", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    [data-testid="stMetricValue"] { color: #CCFF00; font-size: 32px; }
    .status-box { padding: 25px; border-radius: 15px; text-align: center; margin-bottom: 25px; font-weight: bold; font-size: 20px; }
    .stProgress > div > div > div > div { background-color: #CCFF00; }
    </style>
    """, unsafe_allow_html=True)

# 2. LOGICA DEL SEMÁFORO DE SALUD (ALGORITMO)
def calcular_salud_global():
    # Simulamos pesos de negocio (Cifras reales vendrían del cliente)
    cumplimiento_bsc = 0.85   # 85% metas financieras
    cumplimiento_okr = 0.70   # 70% metas de escuela
    cumplimiento_pir = 0.95   # 95% calidad operativa
    
    # Media ponderada
    score = (cumplimiento_bsc * 0.50) + (cumplimiento_okr * 0.30) + (cumplimiento_pir * 0.20)
    
    if score >= 0.85: return "🟢 EXCELENTE", "#1B5E20", "El negocio está en zona de crecimiento. Operaciones y finanzas alineadas."
    elif score >= 0.70: return "🟡 PRECAUCIÓN", "#FBC02D", "Desviación detectada en Escuela. Riesgo de estancamiento en ingresos recurrentes."
    else: return "🔴 ALERTA CRÍTICA", "#B71C1C", "Intervención inmediata requerida. Los márgenes operativos están en riesgo."

status_label, status_color, status_msg = calcular_salud_global()

# 3. INTERFAZ SUPERIOR
st.title("AVANZA PÁDEL | Centro de Control")
st.markdown(f'<div class="status-box" style="background-color: {status_color}; color: white;">ESTADO GLOBAL: {status_label}<br><span style="font-size: 14px; font-weight: normal;">{status_msg}</span></div>', unsafe_allow_html=True)

periodo = st.select_slider("Línea de tiempo de análisis:", options=["Semanal", "Mensual", "Trimestral", "Anual"], value="Mensual")

# 4. DISTRIBUCIÓN DE MÉTRICAS CLAVE
st.markdown("### Indicadores Maestros")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Ocupación", "72%", "+4%")
c2.metric("NPS Cliente", "8.2", "0.5")
c3.metric("Margen Escuela", "34%", "-2%")
c4.metric("Consumo Energ.", "1.2k€", "-150€")

st.divider()

# 5. PESTAÑAS DEL MODELO HÍBRIDO
tab_bsc, tab_okr, tab_pir = st.tabs(["ESTRATEGIA (BSC)", "CRECIMIENTO (OKR)", "CALIDAD (PIRÁMIDE)"])

with tab_bsc:
    st.info("**Objetivo:** Supervisión del ROI para Grupo Recio.")
    # (Aquí irían los gráficos de ingresos/gastos anuales)
    st.write("Visualización de Flujo de Caja y EBITDA consolidado.")

with tab_okr:
    st.info("**Objetivo:** Rendimiento de monitores y fidelización de alumnos.")
    st.write("**Progreso KR: Alumnos Nivel 3.0+**")
    st.progress(0.65)
    st.write("**Progreso KR: Retención Mensual**")
    st.progress(0.92)

with tab_pir:
    st.info("**Objetivo:** Mantenimiento de los activos físicos y experiencia en pista.")
    st.write("Checklist de Calidad: Pistas 1-10")
    st.success("✅ Cristales e Iluminación: Estado Óptimo")
    st.warning("⚠️ Climatización Nave B: Revisión programada en 48h")
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

with col_right:
    st.subheader("Radar de Competencia")
    st.info("Oportunidades vs. Clubes vecinos")
    
   # 1. Definición de los datos (Asegúrate de que los nombres no tengan espacios extra)
competencia = pd.DataFrame({
    'Centro': ['Avanza Pádel', 'Club Alcalá B', 'Centro Entrenúcleos'],
    'Pistas_Libres': [2, 0, 5],
    'Precio': [24, 28, 22],  # Cambiamos "Precio Medio" por "Precio"
    'Rating': [4.8, 4.2, 4.5]
})
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
import streamlit as st
import pandas as pd
import plotly.express as px

# ... (Mantener el resto de la configuración anterior) ...

with tab_bsc:
    st.subheader("Simulador de Ingresos Dinámicos (Yield Management)")
    st.info("💡 **Ayuda:** Utilice este simulador para ver el impacto de subir el precio en horas punta (18:00 - 22:00) donde la ocupación es del 95% o superior.")

    col_sim1, col_sim2 = st.columns([1, 2])

    with col_sim1:
        incremento = st.number_input("Incremento de tarifa por hora (€)", min_value=0.0, max_value=10.0, value=2.0, step=0.5)
        horas_punta_dia = st.slider("Horas punta al día con >95% ocupación", 1, 6, 4)
        pistas_afectadas = 10 # Número total de pistas en Avanza Pádel
        
        # Cálculo: Incremento * Horas * Pistas * 30 días
        ingreso_extra_mensual = incremento * horas_punta_dia * pistas_afectadas * 30
        
        st.metric("Ingreso Extra Estimado", f"{ingreso_extra_mensual:,.0f} € / mes", delta="Impacto en EBITDA")
        st.write(f"Estimación basada en {pistas_afectadas} pistas operativas.")

    with col_sim2:
        # Gráfico comparativo
        data_sim = pd.DataFrame({
            'Escenario': ['Ingreso Actual', 'Con Tarifa Dinámica'],
            'Euros (€)': [48500, 48500 + ingreso_extra_mensual]
        })
        fig_sim = px.bar(data_sim, x='Escenario', y='Euros (€)', 
                         color='Escenario', color_discrete_map={'Ingreso Actual': '#333', 'Con Tarifa Dinámica': '#CCFF00'})
        st.plotly_chart(fig_sim, use_container_width=True)

    st.success(f"Proyección: Si aplicas este cambio, el margen operativo subiría aproximadamente un {round((ingreso_extra_mensual/48500)*100, 1)}% mensual.")
