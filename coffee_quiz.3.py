import streamlit as st

st.set_page_config(
    page_title="Coffee Match",
    page_icon="☕",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #f3f0e8 0%, #ffffff 100%);
}

.main-card {
    background-color: #ffffff;
    padding: 28px;
    border-radius: 22px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    border: 1px solid #e6e0d4;
}

.title {
    color: #006241;
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 0px;
}

.subtitle {
    color: #1e3932;
    text-align: center;
    font-size: 18px;
    margin-bottom: 28px;
}

.result-card {
    background-color: #006241;
    color: white;
    padding: 24px;
    border-radius: 22px;
    margin-top: 20px;
    text-align: center;
}

.result-title {
    font-size: 28px;
    font-weight: 800;
}

.result-subtitle {
    font-size: 16px;
    opacity: 0.95;
}

.alt-card {
    background-color: #d4e9e2;
    color: #1e3932;
    padding: 18px;
    border-radius: 18px;
    margin-top: 14px;
}

.small-note {
    color: #6f6259;
    font-size: 14px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


st.markdown('<div class="title">☕ Coffee Match</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Descubre el café que mejor va contigo en menos de 30 segundos.</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="main-card">', unsafe_allow_html=True)

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

    resultados = []
    for bebida, score in ordenados[:3]:
        porcentaje = round((score / mejor_score) * 100, 1)
        resultados.append((bebida, porcentaje))

    return resultados


def nombre_final(bebida, temperatura):
    if temperatura == "Frío" and bebida in ["Latte", "Americano", "Mocha", "Cappuccino"]:
        return f"Iced {bebida}"
    return bebida


def descripcion(bebida, aroma, textura):
    textos = {
        "Latte": "Cremoso, suave y fácil de tomar. Ideal si buscas una experiencia cómoda y balanceada.",
        "Cappuccino": "Espumoso, aromático y con buen cuerpo. Perfecto si quieres balance sin perder intensidad.",
        "Americano": "Directo, limpio y con sabor claro a café. Buena opción si prefieres algo menos dulce.",
        "Espresso": "Corto, fuerte e intenso. Para quienes quieren energía y sabor concentrado.",
        "Cold Brew": "Frío, suave y refrescante. Ideal si quieres algo ligero pero con carácter.",
        "V60": "Ligero, aromático y limpio. Perfecto para notar sabores más delicados.",
        "Mocha": "Cremoso, dulce y con notas de chocolate. Buena opción si quieres algo indulgente.",
        "Flat White": "Cremoso pero más intenso que un latte. Excelente balance entre leche y café."
    }

    return textos.get(bebida, "Una opción balanceada según tus respuestas.")


if st.button("🔍 Encontrar mi café ideal", use_container_width=True):
    resultados = calcular_recomendacion(dulzor, leche, textura, temperatura, aroma, momento)

    bebida_1, score_1 = resultados[0]
    bebida_2, score_2 = resultados[1]
    bebida_3, score_3 = resultados[2]

    final_1 = nombre_final(bebida_1, temperatura)
    final_2 = nombre_final(bebida_2, temperatura)
    final_3 = nombre_final(bebida_3, temperatura)

    st.markdown(f"""
    <div class="result-card">
        <div class="result-title">☕ {final_1}</div>
        <div class="result-subtitle">{score_1}% match contigo</div>
        <br>
        <div>{descripcion(bebida_1, aroma, textura)}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="alt-card">
        <b>🔄 Alternativa cercana:</b> {final_2} — {score_2}% match<br>
        Si quieres algo parecido, pero con otra sensación en taza.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="alt-card">
        <b>🎯 Opción para explorar:</b> {final_3} — {score_3}% match<br>
        Una recomendación diferente para salir un poco de tu zona de confort.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <br>
    <div class="small-note">
        Recomendación basada en tus preferencias de sabor, textura, dulzor y temperatura.
    </div>
    """, unsafe_allow_html=True)
