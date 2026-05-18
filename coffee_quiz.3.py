import streamlit as st

st.set_page_config(
    page_title="Coffee Match",
    page_icon="☕",
    layout="centered"
)

st.markdown("""
<style>

/* ===== OCULTAR STREAMLIT ===== */

header {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* ===== ESPACIADO GENERAL ===== */

.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem;
    max-width: 800px;
}

/* ===== FONDO GENERAL ===== */

.stApp {
    background: linear-gradient(
        180deg,
        #0f0f0f 0%,
        #171717 100%
    );
    color: white;
}

/* ===== HERO ===== */

.hero {
    background: linear-gradient(
        135deg,
        #1b1b1b 0%,
        #111111 100%
    );
    
    border: 1px solid rgba(212,175,55,0.15);

    padding: 28px;

    border-radius: 28px;

    text-align: center;

    margin-top: 10px;
    margin-bottom: 25px;

    box-shadow: 0 10px 40px rgba(0,0,0,0.35);
}

/* ===== TITULO ===== */

.hero-title {
    font-size: 42px;
    font-weight: 800;
    color: #D4AF37;
    margin-bottom: 10px;
    letter-spacing: 1px;
}

/* ===== SUBTITULO ===== */

.hero-subtitle {
    font-size: 18px;
    color: #d7d7d7;
    margin-bottom: 10px;
}

/* ===== PREGUNTA ===== */

.question-box {
    background-color: #1a1a1a;

    border-radius: 22px;

    padding: 24px;

    margin-bottom: 22px;

    border: 1px solid rgba(255,255,255,0.06);
}

/* ===== TITULO PREGUNTA ===== */

.question-title {
    color: #D4AF37;

    font-size: 30px;

    font-weight: 700;

    margin-bottom: 10px;
}

/* ===== TEXTO PREGUNTA ===== */

.question-subtitle {
    color: #d0d0d0;

    font-size: 17px;

    margin-bottom: 12px;
}

/* ===== BOTONES ===== */

.stButton>button {

    width: 100%;

    background-color: #D4AF37;

    color: black;

    border: none;

    border-radius: 18px;

    padding: 14px;

    font-size: 18px;

    font-weight: 700;

    transition: 0.3s;

    margin-top: 8px;
}

/* ===== HOVER ===== */

.stButton>button:hover {

    background-color: #f0cd63;

    transform: scale(1.02);

    color: black;
}

/* ===== RESULTADO ===== */

.result-box {

    background: linear-gradient(
        135deg,
        #1b1b1b 0%,
        #121212 100%
    );

    border-radius: 28px;

    padding: 30px;

    margin-top: 20px;

    border: 1px solid rgba(212,175,55,0.2);

    text-align: center;

    box-shadow: 0 10px 40px rgba(0,0,0,0.4);
}

/* ===== TITULO RESULTADO ===== */

.result-title {

    color: #D4AF37;

    font-size: 38px;

    font-weight: 800;

    margin-bottom: 16px;
}

/* ===== TEXTO RESULTADO ===== */

.result-text {

    color: white;

    font-size: 20px;

    line-height: 1.6;
}

/* ===== MOBILE ===== */

@media (max-width: 768px) {

    .hero-title {
        font-size: 34px;
    }

    .question-title {
        font-size: 25px;
    }

    .result-title {
        font-size: 30px;
    }

    .stButton>button {
        font-size: 17px;
        padding: 13px;
    }
}

</style>
""", unsafe_allow_html=True)

# ===== HERO =====

st.markdown("""
<div class="hero">
    <div class="hero-title">
        Coffee Match ☕
    </div>

    <div class="hero-subtitle">
        Descubre el café que realmente va contigo
    </div>
</div>
""", unsafe_allow_html=True)

# ===== PREGUNTA =====

st.markdown("""
<div class="question-box">

    <div class="question-title">
        ¿Qué tan dulce te gusta?
    </div>

    <div class="question-subtitle">
        Elige rápido. No hay respuesta correcta.
    </div>

</div>
""", unsafe_allow_html=True)

# ===== BOTONES =====

col1, col2 = st.columns(2)

with col1:
    st.button("Muy dulce")

with col2:
    st.button("Balanceado")

col3, col4 = st.columns(2)

with col3:
    st.button("Poco dulce")

with col4:
    st.button("Nada dulce")

# ===== RESULTADO DEMO =====

st.markdown("""
<div class="result-box">

    <div class="result-title">
        Tu perfil ☕
    </div>

    <div class="result-text">
        Te gustan los cafés suaves, cremosos y balanceados.
        <br><br>
        Tu mejor opción probablemente sería un Latte o Cappuccino.
    </div>

</div>
""", unsafe_allow_html=True)
