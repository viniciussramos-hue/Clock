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
            padding: 25px;
            border-radius: 20px;
            box-shadow: 0px 8px 30px rgba(0,0,0,0.8);
            text-align: center;
            width: 500px;
        }

        .word-time {
            color: #FF4B4B;
            font-size: 2rem;
            font-weight: bold;
            margin: 0;
        }

        .digital-time {
            color: #999;
            font-size: 0.95rem;
            margin: 6px 0 12px 0;
            letter-spacing: 1px;
        }

        .divider {
            border-top: 1px solid #333;
            margin: 12px 0;
        }

        .phrase-box {
            text-align: left;
            min-height: 100px;
        }

        .phrase-title {
            font-size: 0.7rem;
            color: #aaa;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 3px;
        }

        .phrase-en {
            font-size: 1rem;
            color: #fff;
            font-weight: bold;
            margin-bottom: 2px;
        }

        .phrase-phonetic {
            font-size: 0.85rem;
            color: #4da6ff;
            font-style: italic;
            margin-bottom: 4px;
        }

        .phrase-pt {
            font-size: 0.85rem;
            color: #bbb;
            margin-bottom: 10px;
        }

        .btn-group {
            display: flex;
            gap: 10px;
            margin-top: 10px;
        }

        .btn {
            background: #FF4B4B;
            border: none;
            color: white;
            padding: 8px 12px;
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
            <div class="phrase-title">🌐 Live Internet Quote + Guide</div>
            <div class="phrase-en" id="phraseEn">"Buscando frase..."</div>
            <div class="phrase-phonetic" id="phrasePhonetic">Pronúncia: ---</div>
            <div class="phrase-pt" id="phrasePt">Tradução: ---</div>
        </div>

        <div class="btn-group">
            <button class="btn btn-audio" onclick="speakPhrase()">🔊 Ouvir</button>
            <button class="btn" onclick="fetchAndTranslateQuote()">Nova Frase 🌐</button>
        </div>
    </div>

    <script>
        let currentPhraseText = "";

        // Função para gerar uma guia de pronúncia aproximada (quebra fonética estilo "prat-ice")
        function generatePhonetic(text) {
            return text
                .toLowerCase()
                .replace(/ing\b/g, "in'")
                .replace(/tion\b/g, "shun")
                .replace(/the/g, "dha")
                .replace(/you/g, "iu")
                .replace(/to/g, "tu")
                .replace(/are/g, "ar")
                .replace(/is/g, "iz")
                .replace(/([aeiou])\1/g, "$1") // suaviza vogais dobradas
                .split('')
                .join(' ')
                .replace(/\s+s\s+/g, ' s ')
                .replace(/  +/g, ' ');
        }

        // Tradutor simulado/integrado para dar suporte às frases da API
        async function fetchAndTranslateQuote() {
            document.getElementById("phraseEn").innerText = '"Carregando nova frase..."';
            document.getElementById("phrasePhonetic").innerText = "Pronúncia: ...";
            document.getElementById("phrasePt").innerText = "Tradução: ...";
            
            try {
                const response = await fetch('https://api.quotable.io/random');
                const data = await response.json();
                
                currentPhraseText = data.content;
                document.getElementById("phraseEn").innerText = `"${data.content}" (${data.author})`;
                
                // Gerando a fonética simulada baseada nas letras
                let phoneticGuide = generatePhonetic(data.content);
                document.getElementById("phrasePhonetic").innerText = `🗣️ Pronúncia guiada: [ ${phoneticGuide} ]`;

                // Traduzindo via API gratuita do MyMemory para português
                const transResponse = await fetch(`https://api.mymemory.translated.net/get?q=${encodeURIComponent(data.content)}&langpair=en|pt`);
                const transData = await transResponse.json();
                
                if(transData && transData.responseData) {
                    document.getElementById("phrasePt").innerText = `🇧🇷 Tradução: "${transData.responseData.translatedText}"`;
                } else {
                    document.getElementById("phrasePt").innerText = "🇧🇷 Tradução indisponível no momento.";
                }

            } catch (error) {
                currentPhraseText = "Practice makes perfect.";
                document.getElementById("phraseEn").innerText = `"${currentPhraseText}"`;
                document.getElementById("phrasePhonetic").innerText = "🗣️ Pronúncia guiada: [ prác-tis méiks pər-fekt ]";
                document.getElementById("phrasePt").innerText = '🇧🇷 Tradução: "A prática leva à perfeição."';
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

        fetchAndTranslateQuote();
        setInterval(updateClock, 1000);
        updateClock();
    </script>
</body>
</html>
""", height=550, scrolling=False)
