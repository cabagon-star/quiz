import streamlit as st

# ====================================
# CONFIG
# ====================================

st.set_page_config(
    page_title="Coffee Match",
    page_icon="☕",
    layout="centered"
)

# ====================================
# CSS
# ====================================

st.markdown("""
<style>

/* ===== HIDE STREAMLIT ===== */

header {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* ===== GLOBAL ===== */

.block-container {
    padding-top: 2rem !important;
    max-width: 850px;
}

.stApp {
    background: linear-gradient(
        180deg,
        #050505 0%,
        #101010 100%
    );
}

/* ===== HERO ===== */

.hero {
    background: linear-gradient(
        135deg,
        #171717 0%,
        #0f0f0f 100%
    );

    border-radius: 34px;

    padding: 42px;

    margin-bottom: 28px;

    border: 1px solid rgba(212,175,55,0.18);

    box-shadow: 0 10px 45px rgba(0,0,0,0.45);

    text-align: center;
}

/* ===== HERO TITLE ===== */

.hero-title {
    color: #D4AF37;

    font-size: 60px;

    font-weight: 800;

    margin-bottom: 12px;
}

/* ===== HERO SUBTITLE ===== */

.hero-subtitle {
    color: #d9d9d9;

    font-size: 22px;

    font-weight: 400;
}

/* ===== QUESTION BOX ===== */

.question-box {

    background: linear-gradient(
        135deg,
        #1a1a1a 0%,
        #121212 100%
    );

    border-radius: 30px;

    padding: 34px;

    margin-bottom: 22px;

    border: 1px solid rgba(255,255,255,0.05);

    box-shadow: 0 10px 40px rgba(0,0,0,0.35);
}

/* ===== QUESTION TITLE ===== */

.question-title {

    color: #D4AF37;

    font-size: 34px;

    font-weight: 700;

    margin-bottom: 10px;
}

/* ===== QUESTION SUBTITLE ===== */

.question-subtitle {

    color: #cfcfcf;

    font-size: 18px;
}

/* ===== BUTTONS ===== */

.stButton > button {

    width: 100%;

    background-color: #D4AF37;

    color: black;

    border: none;

    border-radius: 18px;

    padding: 16px;

    font-size: 18px;

    font-weight: 700;

    margin-top: 10px;

    transition: 0.3s ease;
}

/* ===== BUTTON HOVER ===== */

.stButton > button:hover {

    background-color: #f2cf69;

    color: black;

    transform: scale(1.02);
}

/* ===== RESULT ===== */

.result-box {

    background: linear-gradient(
        135deg,
        #181818 0%,
        #101010 100%
    );

    border-radius: 30px;

    padding: 34px;

    margin-top: 28px;

    border: 1px solid rgba(212,175,55,0.2);

    text-align: center;

    box-shadow: 0 10px 40px rgba(0,0,0,0.35);
}

.result-title {

    color: #D4AF37;

    font-size: 42px;

    font-weight: 800;

    margin-bottom: 14px;
}

.result-text {

    color: white;

    font-size: 21px;

    line-height: 1.7;
}

/* ===== MOBILE ===== */

@media (max-width: 768px) {

    .hero-title {
        font-size: 42px;
    }

    .hero-subtitle {
        font-size: 18px;
    }

    .question-title {
        font-size: 28px;
    }

    .question-subtitle {
        font-size: 16px;
    }

    .result-title {
        font-size: 34px;
    }

    .result-text {
        font-size: 18px;
    }

    .stButton > button {
        font-size: 16px;
        padding: 14px;
    }
}

</style>
""", unsafe_allow_html=True)

# ====================================
# HERO
# ====================================

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

# ====================================
# QUESTION
# ====================================

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

# ====================================
# BUTTONS
# ====================================

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

# ====================================
# RESULT DEMO
# ====================================

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
