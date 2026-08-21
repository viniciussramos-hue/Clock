import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Word Clock", page_icon="⏰", layout="centered")

st.title("🕰️ English Word Clock")
st.markdown("Relógio dinâmico que escreve as horas por extenso em inglês.")

# Função para converter horas e minutos em texto formal em inglês
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

    if minute == 0:
        return f"It's {units[h_12]} o'clock"
    elif minute == 15:
        return f"It's a quarter past {units[h_12]}"
    elif minute == 30:
        return f"It's half past {units[h_12]}"
    elif minute == 45:
        return f"It's a quarter to {units[next_h_12]}"
    elif minute < 30:
        return f"It's {units[minute]} past {units[h_12]}"
    else:
        mins_to = 60 - minute
        return f"It's {units[mins_to]} to {units[next_h_12]}"

# Espaço na tela para o relógio atualizar
clock_placeholder = st.empty()
digital_placeholder = st.empty()

# Loop para atualizar o relógio em tempo real
for _ in range(300): # Roda por um tempo antes de pedir refresh
    now = datetime.now()
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
            f"<p style='text-align: center; color: gray;'>Digital: {hora_digital}</p>", 
            unsafe_allow_html=True
        )
        
    time.sleep(1)
    st.rerun()
