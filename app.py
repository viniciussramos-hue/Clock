import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="English Word Clock & Dynamic Phrases", page_icon="⏰", layout="centered")

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
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0px 8px 30px rgba(0,0,0,0.8);
            text-align: center;
            width: 480px;
        }

        .word-time {
            color: #FF4B4B;
            font-size: 2.2rem;
            font-weight: bold;
            margin: 0;
        }

        .digital-time {
            color: #999;
            font-size: 1rem;
            margin: 8px 0 15px 0;
            letter-spacing: 1px;
        }

        .divider {
            border-top: 1px solid #333;
            margin: 15px 0;
        }

        .phrase-box {
            text-align: left;
            min-height: 80px;
        }

        .phrase-title {
            font-size: 0.75rem;
            color: #aaa;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 4px;
        }

        .phrase-en {
            font-size: 1.05rem;
            color: #fff;
            font-weight: bold;
            margin-bottom: 4px;
        }

        .phrase-author {
            font-size: 0.85rem;
            color: #bbb;
            font-style: italic;
            margin-bottom: 15px;
        }

        .btn-group {
            display: flex;
            gap: 10px;
        }

        .btn {
            background: #FF4B4B;
            border: none;
            color: white;
            padding: 9px 12px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: bold;
            cursor: pointer;
            flex: 1;
            transition: background 0.2s;
        }

        .btn:hover {
            background: #ff2a2a;
        }

        .btn-audio {
            background: #333;
        }

        .btn-audio:hover {
            background: #444;
        }
    </style>
</head>
<body>

    <div class="central-card">
        <div class="word-time" id="wordClock">Loading...</div>
        <div class="digital-time" id="digitalClock">BRT: --:--:--</div>
        
        <div class="divider"></div>

        <div class="phrase-box">
            <div class="phrase-title">🌐 Live Internet Quote (English)</div>
            <div class="phrase-en" id="phraseEn">"Buscando frase na internet..."</div>
            <div class="phrase-author" id="phraseAuthor">---</div>
        </div>

        <div class="btn-group">
            <button class="btn btn-audio" onclick="speakPhrase()">🔊 Ouvir</button>
            <button class="btn" onclick="fetchRandomQuote()">Nova Frase 🌐</button>
        </div>
    </div>

    <script>
        let currentPhraseText = "";

        // Função para buscar frases reais de uma API pública da internet
        async function fetchRandomQuote() {
            document.getElementById("phraseEn").innerText = '"Carregando nova frase..."';
            document.getElementById("phraseAuthor").innerText = "Aguarde...";
            
            try {
                // API pública gratuita de citações em inglês
                const response = await fetch('https://api.quotable.io/random');
                const data = await response.json();
                
                currentPhraseText = data.content;
                document.getElementById("phraseEn").innerText = `"${data.content}"`;
                document.getElementById("phraseAuthor").innerText = `— ${data.author}`;
            } catch (error) {
                // Fallback caso caia a internet
                currentPhraseText = "Practice makes perfect.";
                document.getElementById("phraseEn").innerText = `"${currentPhraseText}"`;
                document.getElementById("phraseAuthor").innerText = "— Proverb (Offline mode)";
            }
        }

        function speakPhrase() {
            if ('speechSynthesis' in window && currentPhraseText) {
                const utterance = new SpeechSynthesisUtterance(currentPhraseText);
                utterance.lang = 'en-US';
                window.speechSynthesis.speak(utterance);
            }
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

        // Carrega a primeira frase ao abrir e inicia o relógio
        fetchRandomQuote();
        setInterval(updateClock, 1000);
        updateClock();
    </script>
</body>
</html>
""", height=520, scrolling=False)
