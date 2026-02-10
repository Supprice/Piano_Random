iimport streamlit as st
import random
import time

# --- CONFIGURATION ---
st.set_page_config(page_title="Piano Training Pro", layout="centered")

# Style CSS pour le clavier et l'interface
st.markdown("""
    <style>
    .piano-keys { display: flex; justify-content: center; margin-top: 20px; }
    .white-key { width: 40px; height: 120px; border: 1px solid #000; background: white; border-radius: 0 0 5px 5px; }
    .black-key { width: 24px; height: 70px; background: black; margin-left: -12px; margin-right: -12px; z-index: 1; border-radius: 0 0 3px 3px; }
    .main-chord { text-align: center; font-size: 80px; font-weight: bold; color: #FF4B4B; padding: 20px; background: #f0f2f6; border-radius: 20px; }
    </style>
""", unsafe_allow_html=True)

st.title("🎹 Entraînement Piano Pro")

# --- BARRE LATÉRALE (Filtres et Timer) ---
st.sidebar.header("Paramètres d'entraînement")

# Idée 1 : Chronomètre
auto_mode = st.sidebar.toggle("Mode Automatique (Loop)")
seconds = st.sidebar.slider("Secondes entre accords", 2, 10, 5)

# Idée 2 : Filtre de Tonalités
st.sidebar.subheader("Filtrer les notes")
show_nat = st.sidebar.checkbox("Naturelles (A, B...)", value=True)
show_sharp = st.sidebar.checkbox("Dièses (#)", value=True)
show_flat = st.sidebar.checkbox("Bémols (b)", value=True)

# --- OPTIONS D'ACCORDS ---
col1, col2 = st.columns(2)
with col1:
    opt_min = st.checkbox("Inclure Mineur (-)")
    opt_7 = st.checkbox("Inclure 7ème (Δ7 / 7)")
with col2:
    opt_ten = st.checkbox("Ajouter Tensions (9, 11, 13)") # Idée 4
    opt_renv = st.checkbox("Renversements (1-4)")

# --- LOGIQUE DE GÉNÉRATION ---
def generer_accord():
    # Base de notes selon les filtres (Idée 2)
    pool = []
    if show_nat: pool += ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    if not pool: return "Sélectionnez une note !"
    
    res = random.choice(pool)
    
    # Altérations
    alt = ""
    if show_sharp and show_flat: alt = random.choice(['#', 'b', ''])
    elif show_sharp: alt = random.choice(['#', ''])
    elif show_flat: alt = random.choice(['b', ''])
    res += alt

    if opt_min and random.choice([True, False]): res += "-"
    if opt_7 and random.choice([True, False]): res += random.choice(["Δ7", "7"])
    
    # Idée 4 : Tensions
    if opt_ten and random.choice([True, False]):
        res += f" ({random.choice(['9', '11', '13', 'b9', '#11'])})"
        
    if opt_renv and random.choice([True, False]):
        res += f" ({random.randint(1, 4)})"
        
    if random.choice([True, False]): # Option Drop 2 toujours présente
        res += " Drop 2"
        
    return res

# Gestion du rafraîchissement automatique (Idée 1)
if auto_mode:
    placeholder = st.empty()
    while True:
        accord = generer_accord()
        with placeholder.container():
            st.markdown(f'<div class="main-chord">{accord}</div>', unsafe_allow_html=True)
            # Idée 3 : Schéma de clavier visuel
            st.markdown("""
                <div class="piano-keys">
                    <div class="white-key"></div><div class="black-key"></div><div class="white-key"></div><div class="black-key"></div><div class="white-key"></div>
                    <div class="white-key"></div><div class="black-key"></div><div class="white-key"></div><div class="black-key"></div><div class="white-key"></div><div class="black-key"></div><div class="white-key"></div>
                </div>
            """, unsafe_allow_html=True)
        time.sleep(seconds)
        st.rerun()
else:
    if st.button("GÉNÉRER UN ACCORD", use_container_width=True):
        accord = generer_accord()
        st.markdown(f'<div class="main-chord">{accord}</div>', unsafe_allow_html=True)
        # Idée 3 : Clavier visuel
        st.markdown("""
            <div class="piano-keys">
                <div class="white-key"></div><div class="black-key"></div><div class="white-key"></div><div class="black-key"></div><div class="white-key"></div>
                <div class="white-key"></div><div class="black-key"></div><div class="white-key"></div><div class="black-key"></div><div class="white-key"></div><div class="black-key"></div><div class="white-key"></div>
            </div>
        """, unsafe_allow_html=True)
