import streamlit as st

st.set_page_config(page_title="Coffee Match", layout="centered")

st.title("☕ Coffee Match")
st.write("Encuentra tu café ideal en segundos")

# -------------------
# PREGUNTAS
# -------------------

dulzor = st.selectbox("¿Qué tan dulce te gusta?", ["Nada", "Poco", "Medio", "Mucho"])
leche = st.selectbox("¿Leche?", ["Sin leche", "A veces", "Sí"])
textura = st.selectbox("Textura:", ["Ligera", "Cremosa", "Fuerte"])
temperatura = st.selectbox("Temperatura:", ["Caliente", "Frío"])
aroma = st.selectbox("Aroma:", ["Chocolate", "Caramelo", "Frutal"])
momento = st.selectbox("¿Qué buscas?", ["Energía", "Relajarte", "Balance"])

# -------------------
# MOTOR SIMPLIFICADO (inspirado en tu sistema)
# -------------------

def calcular_scores():
    scores = {
        "ESP": 0,
        "V60": 0,
        "PRS": 0,
        "MOK": 0,
        "CLD": 0,
        "MILK": 0,
        "BLACK": 0,
        "BODY": 0,
        "SWEET": 0,
        "CHO": 0,
        "CAR": 0,
        "FRU": 0
    }

    # leche
    if leche == "Sí":
        scores["MILK"] += 10
    elif leche == "A veces":
        scores["MILK"] += 5
    else:
        scores["BLACK"] += 10

    # dulzor
    if dulzor == "Mucho":
        scores["SWEET"] += 8
    elif dulzor == "Medio":
        scores["SWEET"] += 5

    # textura
    if textura == "Fuerte":
        scores["BODY"] += 8
    elif textura == "Cremosa":
        scores["BODY"] += 6

    # aroma
    if aroma == "Chocolate":
        scores["CHO"] += 6
    elif aroma == "Caramelo":
        scores["CAR"] += 6
    elif aroma == "Frutal":
        scores["FRU"] += 6

    # método base
    if scores["MILK"] >= 7:
        scores["ESP"] += 6
    elif scores["BODY"] >= 7:
        scores["MOK"] += 5
    elif scores["FRU"] >= 5:
        scores["V60"] += 6
    else:
        scores["CLD"] += 5

    return scores


# -------------------
# GENERADOR DE BEBIDA
# -------------------

def generar_bebida(scores):
    milk = scores["MILK"]
    body = scores["BODY"]
    sweet = scores["SWEET"]
    choco = scores["CHO"]
    fruity = scores["FRU"]

    if milk >= 7:
        bebida = "Latte"
    elif body >= 7:
        bebida = "Americano"
    elif fruity >= 5:
        bebida = "V60"
    else:
        bebida = "Cold Brew"

    if choco >= 5:
        bebida += " chocolateado"
    elif sweet >= 5:
        bebida += " suave"

    if temperatura == "Frío":
        bebida = "Iced " + bebida

    return bebida


# -------------------
# RESULTADO
# -------------------

if st.button("🔍 Ver recomendación"):

    scores = calcular_scores()

    bebida_principal = generar_bebida(scores)

    # alternativa
    bebida_alt = "Cappuccino" if "Latte" in bebida_principal else "Flat White"

    # exploración
    bebida_extra = "Cold Brew" if temperatura == "Frío" else "Espresso"

    st.success(f"☕ Tu café ideal: **{bebida_principal} (100%)**")

    st.write(f"🔄 Alternativa: **{bebida_alt} (90%)**")
    st.write(f"🎯 Explora: **{bebida_extra} (75%)**")

    st.caption("Basado en tu perfil de sabor y textura")