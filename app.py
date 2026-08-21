import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="English Word Clock & Grammar Hub", page_icon="📚", layout="centered")

components.html("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>English Clock & Grammar</title>
    <style>
        body { 
            background-color: #0e1117; 
            color: #fff; 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 10px;
            box-sizing: border-box;
        }
        
        .main-container {
            background-color: #161616;
            border: 2px solid #FF4B4B;
            padding: 20px;
            border-radius: 20px;
            box-shadow: 0px 8px 30px rgba(0,0,0,0.8);
            width: 100%;
            max-width: 500px;
            text-align: center;
            box-sizing: border-box;
        }

        /* Sistema de Abas */
        .tabs {
            display: flex;
            gap: 8px;
            margin-bottom: 15px;
            border-bottom: 2px solid #333;
            padding-bottom: 10px;
        }

        .tab-btn {
            background: #222;
            border: none;
            color: #aaa;
            padding: 8px 10px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: bold;
            cursor: pointer;
            flex: 1;
            transition: all 0.2s;
        }

        .tab-btn.active {
            background: #FF4B4B;
            color: white;
        }

        .tab-content {
            display: none;
            text-align: left;
            max-height: 350px;
            overflow-y: auto;
            padding-right: 5px;
        }

        .tab-content.active {
            display: block;
        }

        /* Estilho da aba do Relógio */
        .word-time {
            color: #FF4B4B;
            font-size: 2.2rem;
            font-weight: 800;
            margin: 0;
            line-height: 1.2;
            text-align: center;
        }

        .digital-time {
            color: #999;
            font-size: 0.9rem;
            margin: 6px 0 10px 0;
            letter-spacing: 1px;
            text-align: center;
        }

        .divider {
            border-top: 1px solid #333;
            margin: 12px 0;
        }

        .phrase-box {
            min-height: 85px;
            margin-bottom: 12px;
        }

        .phrase-title {
            font-size: 0.7rem;
            color: #aaa;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 3px;
        }

        .phrase-en {
            font-size: 0.95rem;
            color: #fff;
            font-weight: bold;
            margin-bottom: 2px;
        }

        .phrase-phonetic {
            font-size: 0.8rem;
            color: #4da6ff;
            font-style: italic;
            margin-bottom: 3px;
        }

        .phrase-pt {
            font-size: 0.8rem;
            color: #bbb;
        }

        .btn-group {
            display: flex;
            gap: 10px;
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
            background: #2b2b2b;
            border: 1px solid #444;
        }

        /* Estilho da aba de Gramática */
        .grammar-card {
            background: #1f1f1f;
            border-left: 4px solid #FF4B4B;
            padding: 10px 12px;
            margin-bottom: 10px;
            border-radius: 4px;
        }

        .grammar-title {
            color: #FF4B4B;
            font-size: 0.85rem;
            font-weight: bold;
            margin-bottom: 3px;
        }

        .grammar-desc {
            color: #ccc;
            font-size: 0.75rem;
            margin-bottom: 4px;
        }

        .grammar-example {
            color: #4da6ff;
            font-size: 0.75rem;
            font-style: italic;
        }

        /* Barra de rolagem customizada */
        ::-webkit-scrollbar {
            width: 5px;
        }
        ::-webkit-scrollbar-thumb {
            background: #444;
            border-radius: 10px;
        }
    </style>
</head>
<body>

    <div class="main-container">
        <!-- Navegação por Abas -->
        <div class="tabs">
            <button class="tab-btn active" onclick="switchTab('clockTab', event)">⏰ Clock & Phrases</button>
            <button class="tab-btn" onclick="switchTab('grammarTab', event)">📖 Grammar Guide</button>
        </div>

        <!-- ABA 1: Relógio e Frases -->
        <div id="clockTab" class="tab-content active">
            <div class="word-time" id="wordClock">Loading...</div>
            <div class="digital-time" id="digitalClock">BRT: --:--:--</div>
            
            <div class="divider"></div>

            <div class="phrase-box">
                <div class="phrase-title">💬 Everyday English & Business Expressions</div>
                <div class="phrase-en" id="phraseEn">"Buscando frase..."</div>
                <div class="phrase-phonetic" id="phrasePhonetic">Pronúncia: ---</div>
                <div class="phrase-pt" id="phrasePt">Tradução: ---</div>
            </div>

            <div class="btn-group">
                <button class="btn btn-audio" onclick="speakPhrase()">🔊 Ouvir</button>
                <button class="btn" onclick="getRandomPhrase()">Nova Frase 🔄</button>
            </div>
        </div>

        <!-- ABA 2: Regras Gramaticais -->
        <div id="grammarTab" class="tab-content">
            <div class="grammar-card">
                <div class="grammar-title">1. Present Simple vs. Continuous</div>
                <div class="grammar-desc">Usado para rotinas/verdades (Simple) versus ações acontecendo agora (Continuous).</div>
                <div class="grammar-example">Ex: I work every day vs. I am working now.</div>
            </div>

            <div class="grammar-card">
                <div class="grammar-title">2. Past Simple (Verbos Regulares e Irregulares)</div>
                <div class="grammar-desc">Ações concluídas no passado. Regulares adicionam '-ed', irregulares mudam a forma.</div>
                <div class="grammar-example">Ex: Worked (trabalhou) / Went (foi - de go).</div>
            </div>

            <div class="grammar-card">
                <div class="grammar-title">3. Future: 'Will' vs. 'Going to'</div>
                <div class="grammar-desc">'Will' para decisões espontâneas; 'Going to' para planos futuros planejados.</div>
                <div class="grammar-example">Ex: I will help you / I am going to travel tomorrow.</div>
            </div>

            <div class="grammar-card">
                <div class="grammar-title">4. Present Perfect (Have + Participio)</div>
                <div class="grammar-desc">Ações que aconteceram no passado mas têm ligação com o presente.</div>
                <div class="grammar-example">Ex: I have finished my report. (Terminei o relatório).</div>
            </div>

            <div class="grammar-card">
                <div class="grammar-title">5. Preposições de Tempo (In, On, At)</div>
                <div class="grammar-desc">AT para horários exatos, ON para dias da semana/datas, IN para meses e anos.</div>
                <div class="grammar-example">Ex: At 8 PM / On Monday / In July.</div>
            </div>
        </div>
    </div>

    <script>
        function switchTab(tabId, evt) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
            
            document.getElementById(tabId).classList.add('active');
            evt.currentTarget.classList.add('active');
        }

        const phraseDatabase = [
            { en: "Practice makes perfect.", phonetic: "prác-tis méiks pər-fekt", pt: "A prática leva à perfeição." },
            { en: "Let's call it a day.", phonetic: "lets kól it ə dei", pt: "Por hoje é só / Vamos encerrar por aqui." },
            { en: "It's up to you.", phonetic: "its áp tu iu", pt: "Você que sabe / A escolha é sua." },
            { en: "Take your time.", phonetic: "teik ior taim", pt: "Não tenha pressa / Vá com calma." },
            { en: "So far, so good.", phonetic: "sou far, sou gud", pt: "Até aqui, tudo bem." },
            { en: "I'll keep you posted.", phonetic: "ail kiip iu poust-ed", pt: "Te mantenho informado." },
            { en: "Out of the blue.", phonetic: "aut ov dhi blu", pt: "Do nada / De repente." },
            { en: "Keep me in the loop.", phonetic: "kiip mi in dhi lup", pt: "Me mantenha informado / atualizado." },
            { en: "Back to the drawing board.", phonetic: "bak tu dhi dró-ing bord", pt: "Voltar à estaca zero / Refazer o plano." }
        ];

        let currentPhraseText = "";

        function getRandomPhrase() {
            const randomIndex = Math.floor(Math.random() * phraseDatabase.length);
            const item = phraseDatabase[randomIndex];
            
            currentPhraseText = item.en;
            document.getElementById("phraseEn").innerText = `"${item.en}"`;
            document.getElementById("phrasePhonetic").innerText = `🗣️ Pronúncia guiada: [ ${item.phonetic} ]`;
            document.getElementById("phrasePt").innerText = `🇧🇷 Tradução: "${item.pt}"`;
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

        getRandomPhrase();
        setInterval(updateClock, 1000);
        updateClock();
    </script>
</body>
</html>
""", height=500, scrolling=True)
