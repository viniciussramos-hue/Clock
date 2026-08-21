import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="English Word Clock & Phrases", page_icon="⏰", layout="centered")

# Usando o componente nativo de HTML do Streamlit para renderizar o design perfeitamente
components.html("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>English Word Clock</title>
    <style>
        body { 
            background-color: #0e1117; 
            color: #fff; 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            overflow: hidden;
        }
        
        .central-card {
            background-color: #161616;
            border: 2px solid #FF4B4B;
            padding: 35px;
            border-radius: 20px;
            box-shadow: 0px 8px 30px rgba(0,0,0,0.8);
            text-align: center;
            width: 450px;
        }

        .word-time {
            color: #FF4B4B;
            font-size: 2.3rem;
            font-weight: bold;
            margin: 0;
        }

        .digital-time {
            color: #999;
            font-size: 1.1rem;
            margin: 10px 0 20px 0;
            letter-spacing: 1px;
        }

        .divider {
            border-top: 1px solid #333;
            margin: 20px 0;
        }

        .phrase-title {
            font-size: 0.75rem;
            color: #aaa;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            text-align: left;
            margin-bottom: 6px;
        }

        .phrase-en {
            font-size: 1.15rem;
            color: #fff;
            font-weight: bold;
            text-align: left;
            margin-bottom: 4px;
        }

        .phrase-pt {
            font-size: 0.95rem;
            color: #bbb;
            font-style: italic;
            text-align: left;
            margin-bottom: 20px;
        }

        .btn {
            background: #FF4B4B;
            border: none;
            color: white;
            padding: 10px 15px;
            border-radius: 8px;
            font-size: 0.9rem;
            font-weight: bold;
            cursor: pointer;
            width: 100%;
            transition: background 0.2s;
        }

        .btn:hover {
            background: #ff2a2a;
        }
    </style>
</head>
<body>

    <div class="central-card">
        <div class="word-time" id="wordClock">Loading...</div>
        <div class="digital-time" id="digitalClock">BRT: --:--:--</div>
        
        <div class="divider"></div>
        
        <div class="phrase-title">💬 English Daily Phrase</div>
        <div class="phrase-en" id="phraseEn">"Loading..."</div>
        <div class="phrase-pt" id="phrasePt">Carregando...</div>
        
        <button class="btn" onclick="changePhrase()">Nova Frase 🔄</button>
    </div>

    <script>
        const dailyPhrases = [
            { en: "Out of the blue.", pt: "Do nada / De repente." },
            { en: "Let's call it a day.", pt: "Por hoje é só / Vamos encerrar." },
            { en: "It's up to you.", pt: "Você que sabe / A escolha é sua." },
            { en: "Take your time.", pt: "Não tenha pressa / Vá com calma." },
            { en: "So far, so good.", pt: "Até aqui, tudo bem." },
            { en: "I'll keep you posted.", pt: "Te mantenho informado." },
            { en: "Cost an arm and a leg.", pt: "Custar uma fortuna / O olho da cara." }
        ];

        function changePhrase() {
            const randomIndex = Math.floor(Math.random() * dailyPhrases.length);
            document.getElementById("phraseEn").innerText = `"${dailyPhrases[randomIndex].en}"`;
            document.getElementById("phrasePt").innerText = dailyPhrases[randomIndex].pt;
        }

        function numberToWords(n) {
            const ones = ["o'clock", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
                          "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
                          "seventeen", "eighteen", "nineteen"];
            const tens = ["", "", "twenty", "thirty", "forty", "fifty"];
            
            if (n < 20) {
                return ones[n];
            } else {
                let t = Math.floor(n / 10);
                let o = n % 10;
                if (o === 0) {
                    return tens[t];
                } else {
                    return `${tens[t]}-${ones[o]}`;
                }
            }
        }

        function updateClock() {
            const now = new Date();
            const optionsTime = { timeZone: 'America/Sao_Paulo', hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' };
            const timeString = new Intl.DateTimeFormat('en-GB', optionsTime).format(now);
            
            const [hStr, mStr, sStr] = timeString.split(':');
            let h = parseInt(hStr, 10);
            let m = parseInt(mStr, 10);

            let h12 = h % 12;
            if (h12 === 0) h12 = 12;

            const hoursMap = [
                "twelve", "one", "two", "three", "four", "five", 
                "six", "seven", "eight", "nine", "ten", "eleven", "twelve"
            ];
            
            let currentHourWord = hoursMap[h12];
            let text = "";

            if (m === 0) {
                text = `It's ${currentHourWord} o'clock`;
            } else if (m < 10) {
                text = `It's ${currentHourWord} oh ${numberToWords(m)}`;
            } else {
                text = `It's ${currentHourWord} ${numberToWords(m)}`;
            }

            document.getElementById("wordClock").innerText = text;
            document.getElementById("digitalClock").innerText = `BRT: ${timeString}`;
        }

        changePhrase();
        setInterval(updateClock, 1000);
        updateClock();
    </script>
</body>
</html>
""", height=500, scrolling=False)
