import streamlit as st
import time
from datetime import datetime
from zoneinfo import ZoneInfo
import random

st.set_page_config(page_title="Word Clock & English Study", page_icon="⏰", layout="centered")

# Criando abas na interface
tab_clock, tab_phrases = st.tabs(["🕰️ English Clock", "💬 Frases do Cotidiano"])

with tab_clock:
    st.title("🕰️ English Word Clock")
    st.markdown("Relógio minuto a minuto no **Horário de Brasília**.")
    
    # (Aqui entraria a lógica do relógio exata que fizemos antes)
    brasilia_tz = ZoneInfo("America/Sao_Paulo")
    now = datetime.now(brasilia_tz)
    st.info(f"Hora atual em Brasília: {now.strftime('%H:%M:%S')}")

with tab_phrases:
    st.title("💬 Daily English Phrases")
    st.markdown("Expressões e frases naturais usadas no dia a dia em inglês.")

    phrases_list = [
        {"en": "Let's call it a day.", "pt": "Por hoje é só / Vamos encerrar."},
        {"en": "It's up to you.", "pt": "Você que sabe / A escolha é sua."},
        {"en": "Take your time.", "pt": "Não tenha pressa."},
        {"en": "So far, so good.", "pt": "Até aqui, tudo bem."},
        {"en": "I'll keep you posted.", "pt": "Te mantenho informado."},
        {"en": "Out of the blue.", "pt": "Do nada / De repente."}
    ]

    # Botão para sortear uma frase aleatória
    if st.button("Sortear Nova Frase 🎲"):
        st.session_state.selected_phrase = random.choice(phrases_list)

    # Mantém a frase na sessão
    if "selected_phrase" not in st.session_state:
        st.session_state.selected_phrase = phrases_list[0]

    current = st.session_state.selected_phrase
    
    st.success(f"🇬🇧 **{current['en']}**")
    st.write(f"🇧🇷 *Tradução:* {current['pt']}")
