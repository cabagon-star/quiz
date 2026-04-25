import streamlit as st

st.set_page_config(
    page_title="Coffee Match",
    page_icon="☕",
    layout="centered"
)

# -------------------
# ESTILOS
# -------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #f4f1e8 0%, #ffffff 100%);
}

/* HERO */
.hero {
    background-color: #006241;
    padding: 32px;
    border-radius: 28px;
    color: white;
    text-align: center;
    margin-bottom: 24px;
}

.hero-title {
    font-size: 40px;
    font-weight: 900;
}

.hero-subtitle {
    font-size: 16px;
}

/* CARD */
.question-card {
    background-color: white;
    padding: 26px;
    border-radius: 22px;
    border: 1px solid #e5dfd4;
    margin-top: 20px;
}

.question-title {
    color: #1e3932;
    font-size: 24px;
    font-weight: 800;
    text-align: center;
}

.helper {
    color: #6f6259;
    text-align: center;
    margin-bottom: 18px;
}

/* RADIO OPCIONES (CORREGIDO) */
div[role="radiogroup"] label {
    background-color: #ffffff !important;
    padding: 12px 14px !important;
    border-radius: 14px !important;
    margin-bottom: 8px !important;
    border: 1px solid #d8d0c3 !important;
}

div[role="radiogroup"] label,
div[role="radiogroup"] label span,
div[role="radiogroup"] label p {
    color: #1e3932 !important;
    font-weight: 600 !important;
}

div[role="radiogroup"] label:hover {
    border-color: #006241 !important;
    background-color: #f4f1e8 !important;
}

/* BOTÓN */
button[kind="primary"] {
    background-color: #006241 !important;
    border-radius: 999px !important;
    font-weight: 700 !important;
}

/* RESULTADO */
.result-card {
    background-color: #006241;
    color: white;
    padding: 26px;
    border-radius: 24px;
    text-align: center;
    margin-top: 20px;
}

.result-name {
    font-size: 32px;
    font-weight: 900;
}

.match {
    font-size: 16px;
}

/* PERFIL */
.profile-card {
    background-color: #d4e9e2;
    color: #1e3932;
    padding: 18px;
    border-radius: 18px;
    margin-top: 14px;
}

/* ALTERNATIVAS */
.alt-card {
    background-color: white;
    color: #1e3932;
    padding: 16px;
    border-radius: 16px;
    margin-top: 12px;
    border: 1px solid #d8d0c3;
}

/* MOBILE */
@media (max-width: 600px) {
    .hero-title { font-size: 30px; }
    .question-title { font-size: 20px; }
    .result-name { font-size: 24px; }
}
</style>
""", unsafe_allow_html=True)

# -------------------
# HEADER
# -------------------
st.markdown("""
<div class="hero">
    <div class="hero-title">☕ Coffee Match</div>
    <div class="hero-subtitle">Tu café ideal en segundos</div>
</div>
""", unsafe_allow_html=True)

# -------------------
# PREGUNTAS
# -------------------
questions = [
    {"key":"dulzor","title":"¿Qué tan dulce te gusta?","options":["Nada","Poco","Medio","Mucho"]},
    {"key":"leche","title":"¿Prefieres café con leche?","options":["Sin leche","A veces","Sí"]},
    {"key":"textura","title":"¿Qué textura prefieres?","options":["Ligera","Cremosa","Fuerte"]},
    {"key":"temperatura","title":"¿Cómo lo prefieres?","options":["Caliente","Frío"]},
    {"key":"aroma","title":"¿Qué aroma te gusta?","options":["Chocolate","Caramelo","Frutal"]},
    {"key":"momento","title":"¿Qué buscas?","options":["Energía","Relajarme","Balance"]}
]

if "step" not in st.session_state:
    st.session_state.step = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

# -------------------
# MOTOR
# -------------------
def recomendar(a):
    if a["leche"] == "Sí":
        bebida = "Latte"
    elif a["dulzor"] == "Nada":
        bebida = "Americano"
    elif a["aroma"] == "Frutal":
        bebida = "V60"
    else:
        bebida = "Cappuccino"

    if a["temperatura"] == "Frío":
        bebida = "Iced " + bebida

    return bebida

# -------------------
# FLUJO APP
# -------------------
total = len(questions)
step = st.session_state.step

st.progress(step/total)

if step < total:

    q = questions[step]

    st.markdown(f"""
    <div class="question-card">
        <div class="question-title">{q["title"]}</div>
    </div>
    """, unsafe_allow_html=True)

    selected = st.radio(
        "Selecciona:",
        q["options"],
        label_visibility="collapsed"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅️"):
            if step > 0:
                st.session_state.step -= 1
                st.rerun()

    with col2:
        if st.button("➡️", type="primary"):
            st.session_state.answers[q["key"]] = selected
            st.session_state.step += 1
            st.rerun()

else:

    bebida = recomendar(st.session_state.answers)

    st.markdown(f"""
    <div class="result-card">
        <div class="result-name">{bebida}</div>
        <div class="match">Tu mejor match</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="profile-card">
        Perfil: te gustan sabores {st.session_state.answers["aroma"].lower()}
        con textura {st.session_state.answers["textura"].lower()}.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="alt-card">🔄 Alternativa: Cappuccino</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="alt-card">🎯 Explora: Cold Brew</div>
    """, unsafe_allow_html=True)

    if st.button("Reiniciar"):
        st.session_state.step = 0
        st.session_state.answers = {}
        st.rerun()
