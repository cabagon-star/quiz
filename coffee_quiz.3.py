import streamlit as st

st.set_page_config(
    page_title="Coffee Match",
    page_icon="☕",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #f4f1e8 0%, #ffffff 100%);
}

.hero {
    background-color: #006241;
    padding: 32px;
    border-radius: 28px;
    color: white;
    text-align: center;
    margin-bottom: 24px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.14);
}

.hero-title {
    font-size: 42px;
    font-weight: 900;
}

.hero-subtitle {
    font-size: 17px;
    opacity: 0.95;
}

.question-card {
    background-color: white;
    padding: 30px;
    border-radius: 26px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    border: 1px solid #e5dfd4;
    margin-top: 18px;
}

.question-title {
    color: #1e3932;
    font-size: 25px;
    font-weight: 850;
    margin-bottom: 18px;
    text-align: center;
}

.helper {
    color: #6f6259;
    text-align: center;
    font-size: 15px;
    margin-bottom: 20px;
}

div[role="radiogroup"] label {
    background-color: #f7f3ea;
    padding: 14px 16px;
    border-radius: 16px;
    margin-bottom: 10px;
    border: 1px solid #d8d0c3;
}

div[role="radiogroup"] label:hover {
    border-color: #006241;
    background-color: #eef7f3;
}

button[kind="primary"] {
    background-color: #006241 !important;
    border-radius: 999px !important;
    border: none !important;
    font-weight: 800 !important;
}

.result-card {
    background-color: #006241;
    color: white;
    padding: 30px;
    border-radius: 28px;
    margin-top: 24px;
    text-align: center;
    box-shadow: 0 10px 28px rgba(0,0,0,0.16);
}

.badge {
    background-color: #cba258;
    color: #1e3932;
    padding: 6px 14px;
    border-radius: 999px;
    font-weight: 800;
    display: inline-block;
    margin-bottom: 12px;
}

.result-name {
    font-size: 36px;
    font-weight: 900;
}

.match {
    font-size: 18px;
    opacity: 0.95;
    margin-top: 8px;
}

.profile-card {
    background-color: #d4e9e2;
    color: #1e3932;
    padding: 20px;
    border-radius: 22px;
    margin-top: 18px;
}

.alt-card {
    background-color: white;
    color: #1e3932;
    padding: 18px;
    border-radius: 20px;
    margin-top: 14px;
    border: 1px solid #d8d0c3;
    box-shadow: 0 5px 16px rgba(0,0,0,0.05);
}

.small-note {
    color: #6f6259;
    font-size: 14px;
    text-align: center;
    margin-top: 20px;
}

@media (max-width: 600px) {
    .hero {
        padding: 24px;
        border-radius: 22px;
    }

    .hero-title {
        font-size: 31px;
    }

    .hero-subtitle {
        font-size: 15px;
    }

    .question-card {
        padding: 22px;
        border-radius: 22px;
    }

    .question-title {
        font-size: 22px;
    }

    .result-name {
        font-size: 28px;
    }
}
</style>
""", unsafe_allow_html=True)


questions = [
    {
        "key": "dulzor",
        "title": "¿Qué tan dulce te gusta?",
        "helper": "Esto nos ayuda a definir si prefieres algo natural, suave o más indulgente.",
        "options": ["Nada", "Poco", "Medio", "Mucho"]
    },
    {
        "key": "leche",
        "title": "¿Prefieres café con leche?",
        "helper": "La leche cambia cuerpo, textura y suavidad.",
        "options": ["Sin leche", "A veces", "Sí"]
    },
    {
        "key": "textura",
        "title": "¿Qué textura prefieres?",
        "helper": "Elige cómo quieres sentir el café en boca.",
        "options": ["Ligera", "Cremosa", "Fuerte"]
    },
    {
        "key": "temperatura",
        "title": "¿Cómo lo prefieres?",
        "helper": "Caliente para una experiencia clásica, frío para algo más refrescante.",
        "options": ["Caliente", "Frío"]
    },
    {
        "key": "aroma",
        "title": "¿Qué aroma te atrae más?",
        "helper": "Esto define el perfil sensorial de tu recomendación.",
        "options": ["Chocolate", "Caramelo", "Frutal", "Nuez / Avellana"]
    },
    {
        "key": "momento",
        "title": "¿Qué buscas al tomar café?",
        "helper": "Queremos recomendarte algo según tu mood del momento.",
        "options": ["Energía", "Relajarme", "Balance", "Acompañar algo dulce"]
    }
]


if "step" not in st.session_state:
    st.session_state.step = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}


def calcular_recomendacion(answers):
    dulzor = answers["dulzor"]
    leche = answers["leche"]
    textura = answers["textura"]
    temperatura = answers["temperatura"]
    aroma = answers["aroma"]
    momento = answers["momento"]

    scores = {
        "Latte": 0,
        "Cappuccino": 0,
        "Americano": 0,
        "Espresso": 0,
        "Cold Brew": 0,
        "V60": 0,
        "Mocha": 0,
        "Flat White": 0
    }

    if leche == "Sí":
        scores["Latte"] += 5
        scores["Cappuccino"] += 4
        scores["Flat White"] += 4
        scores["Mocha"] += 5
    elif leche == "A veces":
        scores["Cappuccino"] += 3
        scores["Flat White"] += 3
        scores["Latte"] += 2
        scores["Americano"] += 1
    else:
        scores["Americano"] += 5
        scores["Espresso"] += 4
        scores["V60"] += 4
        scores["Cold Brew"] += 4

    if dulzor == "Mucho":
        scores["Mocha"] += 5
        scores["Latte"] += 4
    elif dulzor == "Medio":
        scores["Latte"] += 3
        scores["Cappuccino"] += 3
        scores["Mocha"] += 3
    elif dulzor == "Poco":
        scores["Flat White"] += 3
        scores["Cappuccino"] += 2
        scores["Americano"] += 2
    else:
        scores["Espresso"] += 4
        scores["Americano"] += 4
        scores["V60"] += 3

    if textura == "Cremosa":
        scores["Latte"] += 5
        scores["Cappuccino"] += 4
        scores["Flat White"] += 4
        scores["Mocha"] += 4
    elif textura == "Fuerte":
        scores["Espresso"] += 5
        scores["Americano"] += 4
        scores["Flat White"] += 3
    else:
        scores["V60"] += 5
        scores["Cold Brew"] += 3
        scores["Americano"] += 2

    if temperatura == "Frío":
        scores["Cold Brew"] += 6
        scores["Americano"] += 2
        scores["Latte"] += 2
        scores["Mocha"] += 2
    else:
        scores["Latte"] += 2
        scores["Cappuccino"] += 2
        scores["Espresso"] += 2
        scores["V60"] += 2

    if aroma == "Chocolate":
        scores["Mocha"] += 6
        scores["Flat White"] += 2
        scores["Cappuccino"] += 2
    elif aroma == "Caramelo":
        scores["Latte"] += 4
        scores["Cappuccino"] += 3
        scores["Cold Brew"] += 2
    elif aroma == "Frutal":
        scores["V60"] += 5
        scores["Cold Brew"] += 4
        scores["Americano"] += 2
    else:
        scores["Cappuccino"] += 3
        scores["Flat White"] += 3
        scores["Latte"] += 2

    if momento == "Energía":
        scores["Espresso"] += 5
        scores["Americano"] += 4
        scores["Cold Brew"] += 3
    elif momento == "Relajarme":
        scores["Latte"] += 4
        scores["Cappuccino"] += 3
        scores["V60"] += 2
    elif momento == "Balance":
        scores["Flat White"] += 4
        scores["Cappuccino"] += 3
        scores["Americano"] += 2
    else:
        scores["Latte"] += 4
        scores["Mocha"] += 4
        scores["Cappuccino"] += 3

    ordenados = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    mejor_score = ordenados[0][1]

    return [(bebida, round((score / mejor_score) * 100, 1)) for bebida, score in ordenados[:3]]


def nombre_final(bebida, temperatura):
    if temperatura == "Frío" and bebida in ["Latte", "Americano", "Mocha", "Cappuccino"]:
        return f"Iced {bebida}"
    return bebida


def descripcion(bebida):
    textos = {
        "Latte": "Suave, cremoso y fácil de tomar. Ideal para una experiencia cómoda.",
        "Cappuccino": "Espumoso, aromático y balanceado. Buena mezcla entre café y textura.",
        "Americano": "Directo, limpio y con sabor marcado a café.",
        "Espresso": "Corto, intenso y con mucha presencia.",
        "Cold Brew": "Frío, suave y refrescante. Perfecto para algo ligero con carácter.",
        "V60": "Ligero, aromático y limpio. Ideal para descubrir notas más delicadas.",
        "Mocha": "Cremoso, dulce y chocolatoso. Una opción más indulgente.",
        "Flat White": "Cremoso pero más intenso que un latte. Muy buen balance."
    }
    return textos.get(bebida, "Una opción alineada con tus respuestas.")


def perfil_usuario(answers):
    leche = answers["leche"]
    textura = answers["textura"]
    temperatura = answers["temperatura"]
    aroma = answers["aroma"]

    if leche == "Sí":
        base = "cremoso"
    elif leche == "Sin leche":
        base = "intenso y directo"
    else:
        base = "balanceado"

    return f"Perfil {base}, con preferencia {aroma.lower()}, textura {textura.lower()} y estilo {temperatura.lower()}."


st.markdown("""
<div class="hero">
    <div class="hero-title">☕ Coffee Match</div>
    <div class="hero-subtitle">Tu recomendación personalizada, pregunta por pregunta.</div>
</div>
""", unsafe_allow_html=True)


total_steps = len(questions)
current_step = st.session_state.step

progress = current_step / total_steps
st.progress(progress)

if current_step < total_steps:
    q = questions[current_step]

    st.markdown(f"""
    <div class="question-card">
        <div class="question-title">{q["title"]}</div>
        <div class="helper">{q["helper"]}</div>
    </div>
    """, unsafe_allow_html=True)

    selected = st.radio(
        "Selecciona una opción:",
        q["options"],
        key=f"radio_{q['key']}",
        label_visibility="collapsed"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅️ Atrás", use_container_width=True, disabled=current_step == 0):
            st.session_state.step -= 1
            st.rerun()

    with col2:
        if st.button("Siguiente ➜", use_container_width=True, type="primary"):
            st.session_state.answers[q["key"]] = selected
            st.session_state.step += 1
            st.rerun()

else:
    st.progress(1.0)

    resultados = calcular_recomendacion(st.session_state.answers)

    bebida_1, score_1 = resultados[0]
    bebida_2, score_2 = resultados[1]
    bebida_3, score_3 = resultados[2]

    temperatura = st.session_state.answers["temperatura"]

    final_1 = nombre_final(bebida_1, temperatura)
    final_2 = nombre_final(bebida_2, temperatura)
    final_3 = nombre_final(bebida_3, temperatura)

    st.markdown(f"""
    <div class="result-card">
        <div class="badge">MEJOR MATCH</div>
        <div class="result-name">{final_1}</div>
        <div class="match">{score_1}% de compatibilidad contigo</div>
        <br>
        <div>{descripcion(bebida_1)}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="profile-card">
        <b>Tu perfil de sabor:</b><br>
        {perfil_usuario(st.session_state.answers)}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="alt-card">
        <b>🔄 Alternativa cercana:</b> {final_2} — {score_2}% match<br>
        Una opción parecida, pero con una sensación diferente en taza.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="alt-card">
        <b>🎯 Para explorar:</b> {final_3} — {score_3}% match<br>
        Ideal si quieres probar algo fuera de tu elección habitual.
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔁 Reiniciar quiz", use_container_width=True):
        st.session_state.step = 0
        st.session_state.answers = {}
        st.rerun()

    st.markdown("""
    <div class="small-note">
        Este demo puede adaptarse al menú real de cualquier cafetería.
    </div>
    """, unsafe_allow_html=True)
