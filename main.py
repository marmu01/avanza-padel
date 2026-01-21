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
