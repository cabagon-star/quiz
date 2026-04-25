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
    margin-bottom: 8px;
}

.hero-subtitle {
    font-size: 18px;
    opacity: 0.95;
}

.question-card {
    background-color: white;
    padding: 26px;
    border-radius: 24px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.07);
    border: 1px solid #e5dfd4;
    margin-bottom: 22px;
}

.result-card {
    background-color: #006241;
    color: white;
    padding: 28px;
    border-radius: 26px;
    margin-top: 24px;
    text-align: center;
    box-shadow: 0 10px 28px rgba(0,0,0,0.14);
}

.result-name {
    font-size: 34px;
    font-weight: 900;
}

.match {
    font-size: 18px;
    margin-top: 6px;
    opacity: 0.95;
}

.profile-card {
    background-color: #d4e9e2;
    color: #1e3932;
    padding: 20px;
    border-radius: 22px;
    margin-top: 18px;
}

.alt-card {
    background-color: #ffffff;
    color: #1e3932;
    padding: 18px;
    border-radius: 20px;
    margin-top: 14px;
    border: 1px solid #d8d0c3;
    box-shadow: 0 5px 16px rgba(0,0,0,0.05);
}

.badge {
    display: inline-block;
    background-color: #cba258;
    color: #1e3932;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 10px;
}

.small-note {
    color: #6f6259;
    font-size: 14px;
    text-align: center;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <div class="hero-title">☕ Coffee Match</div>
    <div class="hero-subtitle">Descubre tu café ideal según tu sabor, textura y mood del momento.</div>
</div>
""", unsafe_allow_html=True)

st.progress(0.15)

st.markdown('<div class="question-card">', unsafe_allow_html=True)

dulzor = st.selectbox("1. ¿Qué tan dulce te gusta?", ["Nada", "Poco", "Medio", "Mucho"])
leche = st.selectbox("2. ¿Prefieres café con leche?", ["Sin leche", "A veces", "Sí"])
textura = st.selectbox("3. ¿Qué textura prefieres?", ["Ligera", "Cremosa", "Fuerte"])
temperatura = st.selectbox("4. ¿Cómo lo prefieres?", ["Caliente", "Frío"])
aroma = st.selectbox("5. ¿Qué aroma te atrae más?", ["Chocolate", "Caramelo", "Frutal", "Nuez / Avellana"])
momento = st.selectbox("6. ¿Qué buscas al tomar café?", ["Energía", "Relajarme", "Balance", "Acompañar algo dulce"])

st.markdown("</div>", unsafe_allow_html=True)


def calcular_recomendacion(dulzor, leche, textura, temperatura, aroma, momento):
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


def perfil_usuario(dulzor, leche, textura, temperatura, aroma, momento):
    if leche == "Sí":
        base = "cremoso"
    elif leche == "Sin leche":
        base = "intenso y directo"
    else:
        base = "balanceado"

    return f"Perfil {base}, con preferencia {aroma.lower()}, textura {textura.lower()} y estilo {temperatura.lower()}."


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


if st.button("🔍 Encontrar mi café ideal", use_container_width=True):
    st.progress(1.0)

    resultados = calcular_recomendacion(dulzor, leche, textura, temperatura, aroma, momento)

    bebida_1, score_1 = resultados[0]
    bebida_2, score_2 = resultados[1]
    bebida_3, score_3 = resultados[2]

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
        {perfil_usuario(dulzor, leche, textura, temperatura, aroma, momento)}
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

    st.markdown("""
    <div class="small-note">
        Este demo puede adaptarse al menú real de cualquier cafetería.
    </div>
    """, unsafe_allow_html=True)
