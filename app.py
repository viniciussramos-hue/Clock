import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="English Word Clock & Phrases", page_icon="⏰", layout="centered")

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
            width: 520px;
        }

        .word-time {
            color: #FF4B4B;
            font-size: 2.7rem;
            font-weight: 800;
            margin: 0;
            line-height: 1.2;
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
            min-height: 110px;
            margin-bottom: 15px;
        }

        .phrase-title {
            font-size: 0.7rem;
            color: #aaa;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 4px;
        }

        .phrase-en {
            font-size: 1.1rem;
            color: #fff;
            font-weight: bold;
            margin-bottom: 4px;
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
        }

        .btn-group {
            display: flex;
            gap: 12px;
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

        .btn-audio:hover {
            background: #3b3b3b;
        }
    </style>
</head>
<body>

    <div class="central-card">
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

    <script>
        // Banco de dados interno robusto com dezenas de expressões do cotidiano e negócios
        const phraseDatabase = [
            { en: "Practice makes perfect.", phonetic: "prác-tis méiks pər-fekt", pt: "A prática leva à perfeição." },
            { en: "Let's call it a day.", phonetic: "lets kól it ə dei", pt: "Por hoje é só / Vamos encerrar por aqui." },
            { en: "It's up to you.", phonetic: "its áp tu iu", pt: "Você que sabe / A escolha é sua." },
            { en: "Take your time.", phonetic: "teik ior taim", pt: "Não tenha pressa / Vá com calma." },
            { en: "So far, so good.", phonetic: "sou far, sou gud", pt: "Até aqui, tudo bem." },
            { en: "I'll keep you posted.", phonetic: "ail kiip iu poust-ed", pt: "Te mantenho informado." },
            { en: "Out of the blue.", phonetic: "aut ov dhi blu", pt: "Do nada / De repente." },
            { en: "Cost an arm and a leg.", phonetic: "kost an arm ənd ə leg", pt: "Custar uma fortuna / O olho da cara." },
            { en: "Keep me in the loop.", phonetic: "kiip mi in dhi lup", pt: "Me mantenha informado / atualizado." },
            { en: "Back to the drawing board.", phonetic: "bak tu dhi dró-ing bord", pt: "Voltar à estaca zero / Refazer o plano." },
            { en: "Action is the foundational key to all success.", phonetic: "ák-shun iz dhi foun-déi-shun-al kii tu ol sak-sés", pt: "A ação é a chave fundamental para todo o sucesso." },
            { en: "Don't watch the clock; keep going.", phonetic: "dont uótch dhi klok; kiip gó-ing", pt: "Não olhe para o relógio; continue indo." },
            { en: "Better late than never.", phonetic: "bé-ter leit dhan né-ver", pt: "Antes tarde do que nunca." },
            { en: "Actions speak louder than words.", phonetic: "ák-shunz spiik láu-der dhan uordz", pt: "Ações falam mais alto que palavras." },
            { en: "Every cloud has a silver lining.", phonetic: "év-ri klaud héz ə síl-ver lái-ning", pt: "Há males que vêm para o bem." }
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
""", height=560, scrolling=False)
