import streamlit as st
import random
import time

# Configuration de la page
st.set_page_config(page_title="Entraînement Piano", layout="centered")

st.title("Générateur d'Accords V2")

# --- PARAMÈTRES DU TIMER (Barre latérale) ---
st.sidebar.header("Réglages du Timer")
seconds = st.sidebar.number_input("Secondes entre accords", min_value=1, max_value=30, value=5)

# NOUVELLE OPTION : Aléatoire Mineur/Majeur
opt_alea_timer = st.sidebar.checkbox("Aléatoire Mineur/Majeur (Timer)")

if 'timer_actif' not in st.session_state:
    st.session_state.timer_actif = False

def toggle_timer():
    st.session_state.timer_actif = not st.session_state.timer_actif

label_bouton = "STOP" if st.session_state.timer_actif else "DÉMARRER LE TIMER"
st.sidebar.button(label_bouton, on_click=toggle_timer, use_container_width=True)

# --- OPTIONS À COCHER (Directives strictes) ---
st.subheader("Options de l'accord")
col1, col2 = st.columns(2)

with col1:
    opt_min = st.checkbox("Min (-)")
    opt_altere = st.checkbox("Altéré (#/b)")
    opt_7maj = st.checkbox("7ème Majeure (Δ7)")
    opt_7dom = st.checkbox("7ème Dominante (7)")
with col2:
    opt_renv = st.checkbox("Renversement (1-4)")
    opt_drop2 = st.checkbox("Drop 2")
    opt_ten = st.checkbox("Tensions (9, 11, 13)")

# --- LOGIQUE DE GÉNÉRATION ---
def generer_accord(is_timer=False):
    notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    res = random.choice(notes)
    
    # 1. Altéré
    if opt_altere:
        res += random.choice(['#', 'b'])
    
    # 2. Mineur (Logique adaptée)
    # Si le timer est actif et l'option aléatoire cochée, on tire au sort
    if is_timer and opt_alea_timer:
        if random.choice([True, False]):
            res += "-"
    # Sinon, on suit la case à cocher strictement
    elif opt_min:
        res += "-"
    
    # 3. Logique des 7èmes
    possibilites_7 = []
    if opt_7maj: possibilites_7.append("Δ7")
    if opt_7dom: possibilites_7.append("7")
    
    if possibilites_7:
        res += random.choice(possibilites_7)

    # 4. Tensions
    if opt_ten:
        res += f" ({random.choice(['9', '11', '13'])})"
        
    # 5. Renversement
    if opt_renv:
        res += f" ({random.randint(1, 4)})"
        
    # 6. Drop 2
    if opt_drop2:
        res += " Drop 2"
        
    return res

# --- AFFICHAGE ---
placeholder = st.empty()

if st.session_state.timer_actif:
    while st.session_state.timer_actif:
        # On précise qu'on est en mode timer
        accord = generer_accord(is_timer=True)
        with placeholder.container():
            st.markdown(f"""
                <div style="text-align: center; font-size: 80px; font-weight: bold; 
                color: #FF4B4B; padding: 50px; background: #f0f2f6; border-radius: 20px;">
                    {accord}
                </div>
            """, unsafe_allow_html=True)
        time.sleep(seconds)
        st.rerun()
else:
    if st.button('GÉNÉRER UN ACCORD', use_container_width=True):
        accord = generer_accord(is_timer=False)
        with placeholder.container():
            st.markdown(f"""
                <div style="text-align: center; font-size: 80px; font-weight: bold; 
                color: #FF4B4B; padding: 50px; background: #f0f2f6; border-radius: 20px;">
                    {accord}
                </div>
            """, unsafe_allow_html=True)
