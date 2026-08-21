import streamlit as st
import time
from datetime import datetime
from zoneinfo import ZoneInfo

st.set_page_config(page_title="Word Clock", page_icon="⏰", layout="centered")

# CSS para fixar o relógio na tela (estilo widget flutuante)
st.markdown("""
    <style>
    .floating-clock {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #1e1e1e;
        border: 2px solid #FF4B4B;
        padding: 20px 30px;
        border-radius: 12px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.6);
        z-index: 99999;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🕰️ English Word Clock")
st.markdown("Relógio minuto a minuto no **Horário de Brasília** com widget flutuante fixo.")

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

# Container que ficará flutuando e fixo na tela
floating_placeholder = st.empty()

for _ in range(300):
    brasilia_tz = ZoneInfo("America/Sao_Paulo")
    now = datetime.now(brasilia_tz)
    
    h, m = now.hour, now.minute
    texto_horas = time_to_words_exact(h, m)
    hora_digital = now.strftime("%H:%M:%S")
    
    # Injetando dentro da classe CSS flutuante
    floating_placeholder.markdown(
        f"""
        <div class="floating-clock">
            <h2 style='color: #FF4B4B; margin: 0; font-size: 1.8rem;'>{texto_horas}</h2>
            <p style='color: #888; margin: 5px 0 0 0; font-size: 0.9rem;'>BRT: {hora_digital}</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
        
    time.sleep(1)
    st.rerun()
