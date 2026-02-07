import streamlit as st
import random

# Configuration de la page
st.set_page_config(page_title="Générateur d'Accords", layout="centered")

st.title("🎸 Générateur d'Accords")

# Interface sur le côté ou au centre
st.subheader("Options")
col1, col2 = st.columns(2)

with col1:
    opt_min = st.checkbox("Min (-)")
    opt_altere = st.checkbox("Altéré (#/b)")
with col2:
    opt_renv = st.checkbox("Renversement (1-4)")
    opt_drop2 = st.checkbox("Drop 2")

if st.button('GÉNÉRER', use_container_width=True):
    # Logique de génération
    notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    res = random.choice(notes)
    
    if opt_altere:
        res += random.choice(['#', 'b', ''])
    if opt_min and random.choice([True, False]):
        res += "-"
    if opt_renv and random.choice([True, False]):
        res += f" ({random.randint(1, 4)})"
    if opt_drop2 and random.choice([True, False]):
        res += " Drop 2"

    # Affichage stylisé
    st.markdown(f"""
        <div style="text-align: center; font-size: 72px; font-weight: bold; 
        color: #FF4B4B; padding: 40px; border: 2px solid #EEE; border-radius: 15px;">
            {res}
        </div>
    """, unsafe_allow_status=True)
