import streamlit as st

st.set_page_config(
    page_title="Coffee Match",
    page_icon="☕",
    layout="centered"
)

# -------------------
# ESTILOS (COLORES + UI)
# -------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #f4f1e8 0%, #ffffff 100%);
}

/* HERO */
.hero {
    background-color: #006241;
    padding: 34px;
    border-radius: 26px;
    color: white;
    text-align: center;
    margin-bottom: 26px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.12);
}

.hero-title {
    font-size: 42px;
    font-weight: 900;
}

.hero-subtitle {
    font-size: 18px;
    opacity: 0.95;
}

/* BLOQUE PREGUNTAS */
.question-card {
    background-color: white;
    padding: 26px;
    border-radius: 24px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.07);
    border: 1px solid #e5dfd4;
}

/* TEXTO DE PREGUNTAS */
label {
    color: #1e3932 !important;
    font-weight: 700 !important;
}

/* SELECTBOX */
div[data-baseweb="select"] > div {
    background-color: #f7f3ea !important;
    border: 1px solid #d8d0c3 !important;
    border-radius: 14px !important;
}

div[data-baseweb="select"] > div:hover {
    border-color: #006241 !important;
}

div[data-baseweb="select"] span {
    color: #1e3932 !important;
}

/* RESULTADO */
.result-card {
    background-color: #006241;
    color: white;
    padding: 28px;
    border-radius: 26px;
    margin-top: 24px;
    text-align: center;
}

.result-name {
    font-size: 34px;
    font-weight: 900;
}

.match {
    font-size: 18px;
    margin-top: 6px;
}

/* PERFIL */
.profile-card {
    background-color: #d4e9e2;
    color: #1e3932;
    padding: 20px;
    border-radius: 22px;
    margin-top: 18px;
}

/* ALTERNATIVAS */
.alt-card {
    background-color: #ffffff;
    color: #1e3932;
    padding: 18px;
    border-radius: 20px;
    margin-top: 14px;
    border: 1px solid #d8d0c3;
}

/* BADGE */
.badge {
    background-color: #cba258;
    padding: 6px 12px;
    border-radius: 999px;
    font-weight: 700;
    margin-bottom: 10px;
    display: inline-block;
}

/* TEXTO FINAL */
.small-note {
    color: #6f6259;
    font-size: 14px;
    text-align: center;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# -------------------
# HEADER
# -------------------
st.markdown("""
<div class="hero">
    <div class="hero-title">☕ Coffee Match</div>
    <div class="hero-subtitle">Descubre tu café ideal en segundos</div>
</div>
""", unsafe_allow_html=True)

# -------------------
# PREGUNTAS
# -------------------
st.markdown('<div class="question-card">', unsafe_allow_html=True)

dulzor = st.selectbox("¿Qué tan dulce te gusta?", ["Nada", "Poco", "Medio", "Mucho"])
leche = st.selectbox("¿Prefieres café con leche?", ["Sin leche", "A veces", "Sí"])
textura = st.selectbox("¿Qué textura prefieres?", ["Ligera", "Cremosa", "Fuerte"])
temperatura = st.selectbox("¿Cómo lo prefieres?", ["Caliente", "Frío"])
aroma = st.selectbox("¿Qué aroma te gusta?", ["Chocolate", "Caramelo", "Frutal"])
momento = st.selectbox("¿Qué buscas?", ["Energía", "Relajarme", "Balance"])

st.markdown('</div>', unsafe_allow_html=True)

# -------------------
# MOTOR SIMPLE
# -------------------
def recomendar():
    if leche == "Sí":
        bebida = "Latte"
    elif dulzor == "Nada":
        bebida = "Americano"
    elif aroma == "Frutal":
        bebida = "V60"
    else:
        bebida = "Cappuccino"

    if temperatura == "Frío":
        bebida = "Iced " + bebida

    return bebida

# -------------------
# RESULTADO
# -------------------
if st.button("🔍 Ver recomendación", use_container_width=True):

    bebida = recomendar()

    st.markdown(f"""
    <div class="result-card">
        <div class="badge">MEJOR MATCH</div>
        <div class="result-name">{bebida}</div>
        <div class="match">100% compatible contigo</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="profile-card">
        Perfil: te gustan sabores {aroma.lower()}, textura {textura.lower()} y estilo {temperatura.lower()}.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="alt-card">
        🔄 Alternativa: prueba un Cappuccino
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="alt-card">
        🎯 Explora: prueba un Cold Brew
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="small-note">
        Basado en tus preferencias de sabor.
    </div>
    """, unsafe_allow_html=True)
