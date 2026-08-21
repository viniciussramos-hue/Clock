import streamlit as st
import time
from datetime import datetime
from zoneinfo import ZoneInfo

st.set_page_config(page_title="Word Clock", page_icon="⏰", layout="centered")

st.title("🕰️ English Word Clock")
st.markdown("Relógio dinâmico (minuto a minuto) ajustado para o **Horário de Brasília** (GMT-3).")

# Função para converter números de 0 a 59 em palavras em inglês
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

# Função para formatar a hora exata minuto a minuto
def time_to_words_exact(hour, minute):
    h_12 = hour % 12
    if h_12 == 0:
        h_12 = 12
        
    # Nomes das horas
    hours_map = [
        "twelve", "one", "two", "three", "four", "five", 
        "six", "seven", "eight", "nine", "ten", "eleven", "twelve"
    ]
    
    current_hour_word = hours_map[h_12]

    if minute == 0:
        return f"It's {current_hour_word} o'clock"
    elif minute < 10:
        # Ex: 06:04 -> "It's six oh four"
        return f"It's {current_hour_word} oh {number_to_words(minute)}"
    else:
        # Ex: 06:54 -> "It's six fifty-four"
        return f"It's {current_hour_word} {number_to_words(minute)}"

# Espaços na tela
clock_placeholder = st.empty()
digital_placeholder = st.empty()

# Loop de atualização em tempo real
for _ in range(300):
    brasilia_tz = ZoneInfo("America/Sao_Paulo")
    now = datetime.now(brasilia_tz)
    
    h, m = now.hour, now.minute
    
    texto_horas = time_to_words_exact(h, m)
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
