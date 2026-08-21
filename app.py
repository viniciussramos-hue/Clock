import streamlit as st
import time
from datetime import datetime
from zoneinfo import ZoneInfo
import random

st.set_page_config(page_title="English Word Clock & Phrases", page_icon="⏰", layout="centered")

# Funções de conversão de tempo
def number_to_words(n):
    ones = ["o'clock", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
            "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty"]
    
    if n < 20:
        return ones[n]
    else:
        t = n // 10
        o = n % 10
        if o == 0:
            return tens[t]
        else:
            return f"{tens[t]}-{ones[o]}"

def time_to_words_exact(hour, minute):
    h_12 = hour % 12
    if h_12 == 0:
        h_12 = 12
        
    hours_map = [
        "twelve", "one", "two", "three", "four", "five", 
        "six", "seven", "eight", "nine", "ten", "eleven", "twelve"
    ]
    
    current_hour_word = hours_map[h_12]

    if minute == 0:
        return f"It's {current_hour_word} o'clock"
    elif minute < 10:
        return f"It's {current_hour_word} oh {number_to_words(minute)}"
    else:
        return f"It's {current_hour_word} {number_to_words(minute)}"

# Lista de frases do cotidiano
phrases_list = [
    {"en": "Out of the blue.", "pt": "Do nada / De repente."},
    {"en": "Let's call it a day.", "pt": "Por hoje é só / Vamos encerrar."},
    {"en": "It's up to you.", "pt": "Você que sabe / A escolha é sua."},
    {"en": "Take your time.", "pt": "Não tenha pressa / Vá com calma."},
    {"en": "So far, so good.", "pt": "Até aqui, tudo bem."},
    {"en": "I'll keep you posted.", "pt": "Te mantenho informado."},
    {"en": "Cost an arm and a leg.", "pt": "Custar uma fortuna / O olho da cara."}
]

# Gerenciando a frase atual na sessão
if "current_phrase" not in st.session_state:
    st.session_state.current_phrase = random.choice(phrases_list)

# Botão fora do container para sortear a frase
if st.button("Nova Frase 🔄", use_container_width=True):
    st.session_state.current_phrase = random.choice(phrases_list)

# Placeholder para o card centralizado
card_placeholder = st.empty()

# Loop de atualização do relógio
for _ in range(300):
    brasilia_tz = ZoneInfo("America/Sao_Paulo")
    now = datetime.now(brasilia_tz)
    
    h, m = now.hour, now.minute
    texto_horas = time_to_words_exact(h, m)
    hora_digital = now.strftime("%H:%M:%S")
    
    p = st.session_state.current_phrase

    # Adicionado unsafe_allow_html=True para renderizar o layout corretamente
    card_placeholder.markdown(f"""
        <style>
        .block-container {{
            padding-top: 2rem;
            max-width: 650px;
        }}
        .central-card {{
            background-color: #161616;
            border: 2px solid #FF4B4B;
            padding: 35px;
            border-radius: 20px;
            box-shadow: 0px 8px 30px rgba(0,0,0,0.8);
            text-align: center;
            margin-top: 10px;
        }}
        .word-time {{
            color: #FF4B4B;
            font-size: 2.3rem;
            font-weight: bold;
            margin: 0;
        }}
        .digital-time {{
            color: #999;
            font-size: 1.1rem;
            margin: 10px 0 20px 0;
            letter-spacing: 1px;
        }}
        .divider {{
            border-top: 1px solid #333;
            margin: 20px 0;
        }}
        .phrase-title {{
            font-size: 0.75rem;
            color: #aaa;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            text-align: left;
            margin-bottom: 6px;
        }}
        .phrase-en {{
            font-size: 1.15rem;
            color: #fff;
            font-weight: bold;
            text-align: left;
            margin-bottom: 4px;
        }}
        .phrase-pt {{
            font-size: 0.95rem;
            color: #bbb;
            font-style: italic;
            text-align: left;
        }}
        </style>

        <div class="central-card">
            <div class="word-time">{texto_horas}</div>
            <div class="digital-time">BRT: {hora_digital}</div>
            
            <div class="divider"></div>
            
            <div class="phrase-title">💬 English Daily Phrase</div>
            <div class="phrase-en">"{p['en']}"</div>
            <div class="phrase-pt">{p['pt']}</div>
        </div>
    """, unsafe_allow_html=True)

    time.sleep(1)
    st.rerun()
