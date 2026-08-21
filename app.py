import streamlit as st
import time
from datetime import datetime
from zoneinfo import ZoneInfo # Nativo do Python 3.9+ para fusos horários

st.set_page_config(page_title="Word Clock", page_icon="⏰", layout="centered")

st.title("🕰️ English Word Clock")
st.markdown("Relógio dinâmico ajustado para o **Horário de Brasília** (GMT-3).")

# Função para converter horas e minutos em texto em inglês
def time_to_words(hour, minute):
    units = [
        "twelve", "one", "two", "three", "four", "five", 
        "six", "seven", "eight", "nine", "ten", "eleven", 
        "twelve", "thirteen", "fourteen", "quarter", "sixteen", 
        "seventeen", "eighteen", "nineteen", "twenty", "twenty-one", 
        "twenty-two", "twenty-three", "twenty-four", "twenty-five", 
        "twenty-six", "twenty-seven", "twenty-eight", "twenty-nine"
    ]
    
    # Ajuste para formato de 12 horas
    h_12 = hour % 12
    if h_12 == 0:
        h_12 = 12
    next_h_12 = (hour % 12) + 1
    if next_h_12 == 13:
        next_h_12 = 1

    # Arredondando para os blocos mais comuns de conversa em inglês (de 5 em 5 minutos)
    m_rounded = round(minute / 5) * 5
    
    if m_rounded == 0:
        return f"It's {units[h_12]} o'clock"
    elif m_rounded == 15:
        return f"It's a quarter past {units[h_12]}"
    elif m_rounded == 30:
        return f"It's half past {units[h_12]}"
    elif m_rounded == 45:
        return f"It's a quarter to {units[next_h_12]}"
    elif m_rounded < 30:
        return f"It's {units[m_rounded]} past {units[h_12]}"
    else:
        mins_to = 60 - m_rounded
        return f"It's {units[mins_to]} to {units[next_h_12]}"

# Espaços na tela
clock_placeholder = st.empty()
digital_placeholder = st.empty()

# Loop de atualização em tempo real
for _ in range(300):
    # Força a captura da hora usando o fuso de Brasília
    brasilia_tz = ZoneInfo("America/Sao_Paulo")
    now = datetime.now(brasilia_tz)
    
    h, m = now.hour, now.minute
    
    texto_horas = time_to_words(h, m)
    hora_digital = now.strftime("%H:%M:%S")
    
    with clock_placeholder.container():
        st.markdown(
            f"<h1 style='text-align: center; color: #FF4B4B;'>{texto_horas}</h1>", 
            unsafe_allow_html=True
        )
    
    with digital_placeholder.container():
        st.markdown(
            f"<p style='text-align: center; color: gray;'>Brasília Time (BRT): {hora_digital}</p>", 
            unsafe_allow_html=True
        )
        
    time.sleep(1)
    st.rerun()
