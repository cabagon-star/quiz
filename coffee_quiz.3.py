import streamlit as st

st.set_page_config(
    page_title="Coffee Match",
    page_icon="☕",
    layout="centered"
)

st.markdown("""
<style>
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

.stApp {
    background: linear-gradient(180deg, #050505 0%, #101010 100%);
}

.block-container {
    padding-top: 2rem !important;
    max-width: 850px;
}

.hero {
    background: linear-gradient(135deg, #171717 0%, #0f0f0f 100%);
    border-radius: 34px;
    padding: 42px;
    margin-bottom: 28px;
    border: 1px solid rgba(212,175,55,0.18);
    box-shadow: 0 10px 45px rgba(0,0,0,0.45);
    text-align: center;
}

.hero-title {
    color: #D4AF37;
    font-size: 60px;
    font-weight: 800;
    margin-bottom: 12px;
}

.hero-subtitle {
    color: #d9d9d9;
    font-size: 22px;
}

.question-box {
    background: linear-gradient(135deg, #1a1a1a 0%, #121212 100%);
    border-radius: 30px;
    padding: 34px;
    margin-bottom: 22px;
    border: 1px solid rgba(255,255,255,0.05);
    box-shadow: 0 10px 40px rgba(0,0,0,0.35);
}

.question-title {
    color: #D4AF37;
    font-size: 34px;
    font-weight: 700;
    margin-bottom: 10px;
}

.question-subtitle {
    color: #cfcfcf;
    font-size: 18px;
}

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
}

.stButton > button:hover {
    background-color: #f2cf69;
    color: black;
    transform: scale(1.02);
}

@media (max-width: 768px) {
    .hero-title {font-size: 42px;}
    .hero-subtitle {font-size: 18px;}
    .question-title {font-size: 28px;}
    .question-subtitle {font-size: 16px;}
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><div class="hero-title">Coffee Match ☕</div><div class="hero-subtitle">Descubre el café que realmente va contigo</div></div>', unsafe_allow_html=True)

st.markdown('<div class="question-box"><div class="question-title">¿Qué tan dulce te gusta?</div><div class="question-subtitle">Elige rápido. No hay respuesta correcta.</div></div>', unsafe_allow_html=True)

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
