import streamlit as st

# ======================================
# CONFIG
# ======================================

st.set_page_config(
    page_title="Coffee Match",
    page_icon="☕",
    layout="centered"
)

# ======================================
# CSS
# ======================================

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

/* ===== APP ===== */

.stApp {
    background: linear-gradient(
        180deg,
        #050505 0%,
        #111111 100%
    );
}

/* ===== CONTAINER ===== */

.block-container {
    padding-top: 2rem !important;
    max-width: 850px;
}

/* ===== HERO ===== */

.hero {
    background: linear-gradient(
        135deg,
        #171717 0%,
        #101010 100%
    );

    border-radius: 32px;

    padding: 40px;

    margin-bottom: 30px;

    border: 1px solid rgba(212,175,55,0.18);

    box-shadow: 0 10px 40px rgba(0,0,0,0.45);

    text-align: center;
}

/* ===== TITULO ===== */

.hero-title {
    color: #D4AF37;

    font-size: 58px;

    font-weight: 800;

    margin-bottom: 12px;
}

/* ===== SUBTITULO ===== */

.hero-subtitle {
    color: #d7d7d7;

    font-size: 21px;
}

/* ===== QUESTION BOX ===== */

.question-box {

    background: linear-gradient(
        135deg,
        #1b1b1b 0%,
        #131313 100%
    );

    border-radius: 28px;

    padding: 30px;

    margin-bottom: 22px;

    border: 1px solid rgba(255,255,255,0.05);

    box-shadow: 0 10px 35px rgba(0,0,0,0.35);
}

/* ===== QUESTION TITLE ===== */

.question-title {

    color: #D4AF37;

    font-size: 32px;

    font-weight: 700;

    margin-bottom: 10px;
}

/* ===== QUESTION SUBTITLE ===== */

.question-subtitle {

    color: #cfcfcf;

    font-size: 17px;
}

/* ===== BUTTONS ===== */

.stButton > button {

    width: 100%;

    background-color: #D4AF37 !important;

    color: black !important;

    border: none;

    border-radius: 18px;

    padding: 15px;

    font-size: 17px;

    font-weight: 700;

    margin-top: 10px;
}

/* ===== BUTTON HOVER ===== */

.stButton > button:hover {

    background-color: #f0cd63 !important;

    color: black !important;
}

/* ===== RADIO TEXT FIX ===== */

.stRadio label {
    color: white !important;
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
        font-size: 26px;
    }

    .question-subtitle {
        font-size: 15px;
    }
}

</style>
""", unsafe_allow_html=True)

# ======================================
# HERO
# ======================================

st.markdown("""
<div class="hero">
<h1 class="hero-title">Coffee Match ☕</h1>
<p class="hero-subtitle">
Descubre el café que realmente va contigo
</p>
</div>
""", unsafe_allow_html=True)

# ======================================
# QUESTION
# ======================================

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

# ======================================
# BUTTONS
# ======================================

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
