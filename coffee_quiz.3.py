import streamlit as st

st.set_page_config(
    page_title="Coffee Match",
    page_icon="☕",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #f6f1e8 0%, #ffffff 100%);
}

.block-container {
    padding-top: 4.5rem;
    padding-bottom: 1.2rem;
    max-width: 760px;
}

.hero {
    background: linear-gradient(135deg, #006241 0%, #1e3932 100%);
    padding: 20px 18px;
    border-radius: 24px;
    color: white;
    text-align: center;
    margin-bottom: 12px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.14);
}

.hero-title {
    font-size: 34px;
    font-weight: 900;
    line-height: 1.05;
}

.hero-subtitle {
    font-size: 15px;
    opacity: 0.96;
    margin-top: 6px;
}

.question-card {
    background-color: white;
    padding: 14px 16px;
    border-radius: 20px;
    border: 1px solid #e5dfd4;
    box-shadow: 0 6px 18px rgba(0,0,0,0.07);
    margin-bottom: 10px;
}

.question-title {
    color: #1e3932;
    font-size: 22px;
    font-weight: 900;
    text-align: center;
    line-height: 1.15;
}

.helper {
    color: #6f6259;
    text-align: center;
    font-size: 13px;
    margin-top: 4px;
}

.option-card {
    background-color: white;
    border: 1px solid #ded6c8;
    border-radius: 18px;
    padding: 7px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    margin-bottom: 8px;
}

.option-title {
    color: #1e3932;
    font-size: 14px;
    font-weight: 850;
    margin-top: 4px;
    margin-bottom: 5px;
    min-height: 20px;
}

.stButton > button[kind="primary"] {
    background-color: #006241;
    color: white;
    border-radius: 999px;
    border: none;
    padding: 7px 10px;
    font-weight: 850;
    width: 100%;
    min-height: 36px;
}

.stButton > button[kind="primary"]:hover {
    background-color: #1e3932;
    color: white;
}

.stButton > button[kind="secondary"] {
    background-color: #f3eadb;
    color: #1e3932;
    border: 1px solid #cba258;
    border-radius: 999px;
    padding: 7px 10px;
    font-weight: 850;
    width: 100%;
    min-height: 36px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.05);
}

.stButton > button[kind="secondary"]:hover {
    background-color: #cba258;
    color: #1e3932;
    border: 1px solid #cba258;
}

.result-card {
    background: linear-gradient(135deg, #006241 0%, #1e3932 100%);
    color: white;
    padding: 24px 18px;
    border-radius: 28px;
    text-align: center;
    margin-top: 14px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.16);
}

.badge {
    background-color: #cba258;
    color: #1e3932;
    padding: 6px 13px;
    border-radius: 999px;
    font-weight: 900;
    display: inline-block;
    margin-bottom: 10px;
    font-size: 13px;
}

.result-name {
    font-size: 34px;
    font-weight: 950;
    line-height: 1.05;
}

.match {
    font-size: 16px;
    opacity: 0.95;
    margin-top: 6px;
}

.result-description {
    font-size: 15px;
    line-height: 1.35;
    margin-top: 10px;
}

.profile-card {
    background-color: #d4e9e2;
    color: #1e3932;
    padding: 16px;
    border-radius: 20px;
    margin-top: 12px;
    font-size: 15px;
    line-height: 1.35;
}

.alt-card {
    background-color: white;
    color: #1e3932;
    padding: 14px;
    border-radius: 18px;
    margin-top: 10px;
    border: 1px solid #d8d0c3;
    box-shadow: 0 4px 14px rgba(0,0,0,0.04);
    font-size: 14px;
    line-height: 1.3;
}

.small-note {
    color: #6f6259;
    font-size: 13px;
    text-align: center;
    margin-top: 14px;
}

div[data-testid="stImage"] {
    display: flex;
    justify-content: center;
}

div[data-testid="stImage"] img {
    border-radius: 14px;
    width: 100%;
    height: 92px;
    object-fit: cover;
    object-position: center center;
    display: block;
}

@media (max-width: 600px) {
    .block-container {
        padding-left: 0.8rem;
        padding-right: 0.8rem;
        padding-top: 4.5rem;
    }

    .hero {
        padding: 17px 14px;
        border-radius: 20px;
        margin-bottom: 10px;
    }

    .hero-title {
        font-size: 29px;
    }

    .hero-subtitle {
        font-size: 13px;
    }

    .question-card {
        padding: 12px;
        border-radius: 18px;
    }

    .question-title {
        font-size: 19px;
    }

    .helper {
        font-size: 12px;
    }

    .option-card {
        padding: 5px;
        border-radius: 16px;
        margin-bottom: 6px;
    }

    .option-title {
        font-size: 12px;
        margin-top: 3px;
        margin-bottom: 4px;
    }

    .stButton > button {
        min-height: 32px;
        padding: 5px 8px;
        font-size: 13px;
    }

    div[data-testid="stImage"] img {
        height: 72px;
        object-position: center center;
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
        "helper": "Elige rápido. No hay respuesta correcta.",
        "options": [
            {"value": "Nada", "label": "Nada dulce", "image": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=500"},
            {"value": "Poco", "label": "Poco dulce", "image": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=500"},
            {"value": "Medio", "label": "Dulzor medio", "image": "https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=500"},
            {"value": "Mucho", "label": "Muy dulce", "image": "https://images.unsplash.com/photo-1541167760496-1628856ab772?w=500"},
        ]
    },
    {
        "key": "leche",
        "title": "¿Lo prefieres con leche?",
        "helper": "Esto define suavidad, cuerpo y cremosidad.",
        "options": [
            {"value": "Sin leche", "label": "Sin leche", "image": "https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?w=500"},
            {"value": "A veces", "label": "A veces", "image": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=500"},
            {"value": "Sí", "label": "Con leche", "image": "https://images.unsplash.com/photo-1570968915860-54d5c301fa9f?w=500"},
        ]
    },
    {
        "key": "textura",
        "title": "¿Qué textura se te antoja?",
        "helper": "Ligero, cremoso o con más presencia.",
        "options": [
            {"value": "Ligera", "label": "Ligera", "image": "https://images.unsplash.com/photo-1502462041640-b3d7e50d0662?w=500"},
            {"value": "Cremosa", "label": "Cremosa", "image": "https://images.unsplash.com/photo-1534778101976-62847782c213?w=500"},
            {"value": "Fuerte", "label": "Fuerte", "image": "https://images.unsplash.com/photo-1510707577719-ae7c14805e3a?w=500"},
        ]
    },
    {
        "key": "temperatura",
        "title": "¿Caliente o frío?",
        "helper": "Caliente para clásico, frío para algo fresco.",
        "options": [
            {"value": "Caliente", "label": "Caliente", "image": "https://images.unsplash.com/photo-1498804103079-a6351b050096?w=500"},
            {"value": "Frío", "label": "Frío", "image": "https://images.unsplash.com/photo-1517701604599-bb29b565090c?w=500"},
        ]
    },
    {
        "key": "aroma",
        "title": "¿Qué aroma te llama más?",
        "helper": "Esto define tu perfil de sabor.",
        "options": [
            {"value": "Chocolate", "label": "Chocolate", "image": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=500"},
            {"value": "Caramelo", "label": "Caramelo", "image": "https://images.unsplash.com/photo-1551024506-0bccd828d307?w=500"},
            {"value": "Frutal", "label": "Cítrico/frutal", "image": "https://images.unsplash.com/photo-1582979512210-99b6a53386f9?w=500"},
            {"value": "Nuez / Avellana", "label": "Nuez/avellana", "image": "https://images.unsplash.com/photo-1508061253366-f7da158b6d46?w=500"},
        ]
    },
    {
        "key": "momento",
        "title": "¿Qué buscas hoy?",
        "helper": "Tu café también depende del momento.",
        "options": [
            {"value": "Energía", "label": "Energía", "image": "https://images.unsplash.com/photo-1497636577773-f1231844b336?w=500"},
            {"value": "Relajarme", "label": "Disfrutar", "image": "https://images.unsplash.com/photo-1511081692775-05d0f180a065?w=500"},
            {"value": "Balance", "label": "Balance", "image": "https://images.unsplash.com/photo-1523942839745-7848c839b661?w=500"},
            {"value": "Acompañar algo dulce", "label": "Postre", "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=500"},
        ]
    },
]


BEVERAGE_INFO = {
    "Latte": {
        "description": "Suave, cremoso y fácil de tomar. Ideal si buscas una experiencia cómoda.",
        "method": "Espresso",
        "milk": "Alta",
        "intensity": "Baja-media",
    },
    "Cappuccino": {
        "description": "Espumoso, aromático y balanceado. Buena mezcla entre café y textura.",
        "method": "Espresso",
        "milk": "Media",
        "intensity": "Media",
    },
    "Americano": {
        "description": "Directo, limpio y con sabor marcado a café, sin sentirse tan corto como un espresso.",
        "method": "Espresso + agua",
        "milk": "Sin leche",
        "intensity": "Media",
    },
    "Espresso": {
        "description": "Corto, intenso y con mucha presencia. Para quien quiere café sin rodeos.",
        "method": "Espresso",
        "milk": "Sin leche",
        "intensity": "Alta",
    },
    "Cold Brew": {
        "description": "Frío, suave y refrescante. Perfecto para algo ligero con carácter.",
        "method": "Extracción fría",
        "milk": "Opcional",
        "intensity": "Media",
    },
    "V60": {
        "description": "Ligero, aromático y limpio. Ideal para descubrir notas delicadas y frutales.",
        "method": "Filtrado",
        "milk": "Sin leche",
        "intensity": "Baja-media",
    },
    "Mocha": {
        "description": "Cremoso, dulce y chocolatoso. Una opción más indulgente.",
        "method": "Espresso",
        "milk": "Alta",
        "intensity": "Media",
    },
    "Flat White": {
        "description": "Cremoso pero más intenso que un latte. Muy buen balance entre leche y café.",
        "method": "Espresso",
        "milk": "Media",
        "intensity": "Media-alta",
    },
    "Cortado": {
        "description": "Pequeño, intenso y suavizado con poca leche. Buen punto medio.",
        "method": "Espresso",
        "milk": "Baja",
        "intensity": "Alta",
    },
    "Iced Latte": {
        "description": "Frío, suave y cremoso. Fácil de tomar y muy agradable.",
        "method": "Espresso",
        "milk": "Alta",
        "intensity": "Baja-media",
    },
    "Iced Americano": {
        "description": "Frío, limpio y directo. Refrescante sin perder carácter de café.",
        "method": "Espresso + agua fría",
        "milk": "Sin leche",
        "intensity": "Media",
    },
    "Iced Mocha": {
        "description": "Frío, cremoso y chocolatoso. Ideal si quieres algo dulce y refrescante.",
        "method": "Espresso",
        "milk": "Alta",
        "intensity": "Media",
    },
    "Iced Cappuccino": {
        "description": "Frío, espumoso y balanceado. Menos suave que un iced latte.",
        "method": "Espresso",
        "milk": "Media",
        "intensity": "Media",
    },
}


if "step" not in st.session_state:
    st.session_state.step = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}


def add_score(scores, beverage, points, reason=None):
    scores[beverage] = scores.get(beverage, 0) + points


def calcular_recomendacion(answers):
    scores = {
        "Latte": 0,
        "Cappuccino": 0,
        "Americano": 0,
        "Espresso": 0,
        "Cold Brew": 0,
        "V60": 0,
        "Mocha": 0,
        "Flat White": 0,
        "Cortado": 0,
    }

    dulzor = answers["dulzor"]
    leche = answers["leche"]
    textura = answers["textura"]
    temperatura = answers["temperatura"]
    aroma = answers["aroma"]
    momento = answers["momento"]

    # Leche: una de las señales más importantes.
    if leche == "Sí":
        add_score(scores, "Latte", 7)
        add_score(scores, "Mocha", 6)
        add_score(scores, "Cappuccino", 5)
        add_score(scores, "Flat White", 5)
        add_score(scores, "Cortado", 2)
        add_score(scores, "Americano", -3)
        add_score(scores, "Espresso", -3)
        add_score(scores, "V60", -4)
    elif leche == "A veces":
        add_score(scores, "Cappuccino", 5)
        add_score(scores, "Flat White", 5)
        add_score(scores, "Cortado", 4)
        add_score(scores, "Latte", 3)
        add_score(scores, "Americano", 2)
        add_score(scores, "Cold Brew", 2)
    else:
        add_score(scores, "Americano", 7)
        add_score(scores, "Espresso", 6)
        add_score(scores, "V60", 6)
        add_score(scores, "Cold Brew", 5)
        add_score(scores, "Cortado", -2)
        add_score(scores, "Latte", -5)
        add_score(scores, "Mocha", -5)

    # Dulzor: diferencia entre café puro, suave e indulgente.
    if dulzor == "Mucho":
        add_score(scores, "Mocha", 8)
        add_score(scores, "Latte", 6)
        add_score(scores, "Iced Mocha", 0) if False else None
        add_score(scores, "Cappuccino", 3)
        add_score(scores, "Espresso", -3)
        add_score(scores, "Americano", -2)
    elif dulzor == "Medio":
        add_score(scores, "Latte", 5)
        add_score(scores, "Cappuccino", 4)
        add_score(scores, "Mocha", 4)
        add_score(scores, "Flat White", 3)
    elif dulzor == "Poco":
        add_score(scores, "Flat White", 5)
        add_score(scores, "Cappuccino", 4)
        add_score(scores, "Americano", 3)
        add_score(scores, "Cold Brew", 2)
    else:
        add_score(scores, "Espresso", 6)
        add_score(scores, "Americano", 6)
        add_score(scores, "V60", 5)
        add_score(scores, "Cold Brew", 4)
        add_score(scores, "Mocha", -4)
        add_score(scores, "Latte", -2)

    # Textura: cuerpo y sensación en boca.
    if textura == "Cremosa":
        add_score(scores, "Latte", 7)
        add_score(scores, "Flat White", 6)
        add_score(scores, "Cappuccino", 6)
        add_score(scores, "Mocha", 6)
        add_score(scores, "Cortado", 3)
        add_score(scores, "V60", -3)
        add_score(scores, "Americano", -2)
    elif textura == "Fuerte":
        add_score(scores, "Espresso", 7)
        add_score(scores, "Americano", 5)
        add_score(scores, "Flat White", 4)
        add_score(scores, "Cortado", 5)
        add_score(scores, "Cold Brew", 3)
        add_score(scores, "Latte", -1)
    else:
        add_score(scores, "V60", 7)
        add_score(scores, "Cold Brew", 5)
        add_score(scores, "Americano", 4)
        add_score(scores, "Cappuccino", 1)
        add_score(scores, "Mocha", -2)

    # Temperatura: ajusta bebidas finales y método.
    if temperatura == "Frío":
        add_score(scores, "Cold Brew", 8)
        add_score(scores, "Americano", 4)
        add_score(scores, "Latte", 4)
        add_score(scores, "Mocha", 4)
        add_score(scores, "Cappuccino", 2)
        add_score(scores, "Espresso", -2)
        add_score(scores, "V60", 1)
    else:
        add_score(scores, "Latte", 3)
        add_score(scores, "Cappuccino", 3)
        add_score(scores, "Flat White", 3)
        add_score(scores, "Espresso", 3)
        add_score(scores, "Americano", 2)
        add_score(scores, "V60", 3)
        add_score(scores, "Cold Brew", -4)

    # Aroma: sabor dominante.
    if aroma == "Chocolate":
        add_score(scores, "Mocha", 8)
        add_score(scores, "Flat White", 4)
        add_score(scores, "Cappuccino", 4)
        add_score(scores, "Espresso", 3)
        add_score(scores, "Latte", 3)
        add_score(scores, "V60", -2)
    elif aroma == "Caramelo":
        add_score(scores, "Latte", 6)
        add_score(scores, "Cappuccino", 5)
        add_score(scores, "Flat White", 3)
        add_score(scores, "Cold Brew", 3)
        add_score(scores, "Mocha", 2)
    elif aroma == "Frutal":
        add_score(scores, "V60", 8)
        add_score(scores, "Cold Brew", 6)
        add_score(scores, "Americano", 3)
        add_score(scores, "Espresso", 2)
        add_score(scores, "Mocha", -4)
        add_score(scores, "Latte", -2)
    else:
        add_score(scores, "Cappuccino", 5)
        add_score(scores, "Flat White", 5)
        add_score(scores, "Latte", 4)
        add_score(scores, "Cortado", 3)
        add_score(scores, "V60", 1)

    # Momento: intención de consumo.
    if momento == "Energía":
        add_score(scores, "Espresso", 7)
        add_score(scores, "Americano", 6)
        add_score(scores, "Cold Brew", 5)
        add_score(scores, "Cortado", 4)
        add_score(scores, "Latte", -1)
    elif momento == "Relajarme":
        add_score(scores, "Latte", 6)
        add_score(scores, "Cappuccino", 5)
        add_score(scores, "V60", 3)
        add_score(scores, "Flat White", 3)
        add_score(scores, "Espresso", -2)
    elif momento == "Balance":
        add_score(scores, "Flat White", 6)
        add_score(scores, "Cappuccino", 5)
        add_score(scores, "Americano", 4)
        add_score(scores, "V60", 3)
        add_score(scores, "Cortado", 3)
    else:
        add_score(scores, "Latte", 6)
        add_score(scores, "Mocha", 6)
        add_score(scores, "Cappuccino", 5)
        add_score(scores, "Cold Brew", 2)

    # Reglas de coherencia para evitar resultados raros.
    if leche == "Sin leche":
        for b in ["Latte", "Mocha", "Cappuccino", "Flat White", "Cortado"]:
            scores[b] -= 5

    if leche == "Sí" and textura == "Cremosa":
        scores["Latte"] += 3
        scores["Mocha"] += 2
        scores["Flat White"] += 2

    if leche == "Sí" and aroma == "Frutal":
        # Evita que una señal frutal mande demasiado fuerte a V60 si la persona quiere leche.
        scores["V60"] -= 4
        scores["Cold Brew"] += 1
        scores["Latte"] += 2

    if dulzor == "Mucho" and aroma == "Chocolate" and leche != "Sin leche":
        scores["Mocha"] += 5

    if dulzor == "Nada" and leche == "Sin leche" and textura == "Fuerte":
        scores["Espresso"] += 4
        scores["Americano"] += 3

    if temperatura == "Frío" and leche == "Sí":
        scores["Latte"] += 2
        scores["Mocha"] += 2
        scores["Cold Brew"] += 1

    # No dejar negativos al normalizar.
    scores = {k: max(v, 0) for k, v in scores.items()}

    ordenados = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    mejor_score = max(ordenados[0][1], 1)

    return [(bebida, round((score / mejor_score) * 100, 1)) for bebida, score in ordenados[:3]]


def nombre_final(bebida, temperatura):
    if temperatura == "Frío":
        cold_names = {
            "Latte": "Iced Latte",
            "Americano": "Iced Americano",
            "Mocha": "Iced Mocha",
            "Cappuccino": "Iced Cappuccino",
        }
        return cold_names.get(bebida, bebida)
    return bebida


def descripcion(bebida):
    return BEVERAGE_INFO.get(bebida, {}).get("description", "Una opción alineada con tus respuestas.")


def perfil_usuario(answers):
    leche = answers["leche"]
    temperatura = answers["temperatura"]
    aroma = answers["aroma"]
    dulzor = answers["dulzor"]

    if leche == "Sí":
        base = "cremoso"
    elif leche == "Sin leche":
        base = "directo"
    else:
        base = "balanceado"

    if aroma == "Chocolate":
        sabor = "chocolateado"
    elif aroma == "Caramelo":
        sabor = "acaramelado"
    elif aroma == "Frutal":
        sabor = "cítrico/frutal"
    else:
        sabor = "tostado y avellanado"

    dulzor_texto = {
        "Nada": "poco dulce",
        "Poco": "suavemente dulce",
        "Medio": "dulzor medio",
        "Mucho": "dulce"
    }.get(dulzor, "balanceado")

    return f"Un café {base}, {sabor} y {dulzor_texto}. Ideal para disfrutar {temperatura.lower()}."


def build_result_details(bebida_final, bebida_base):
    info = BEVERAGE_INFO.get(bebida_final) or BEVERAGE_INFO.get(bebida_base, {})
    milk = info.get("milk", "Según preferencia")
    intensity = info.get("intensity", "Media")

    if milk == "Alta":
        estilo = "Cremoso"
        leche_texto = "Con leche"
    elif milk == "Media":
        estilo = "Balanceado"
        leche_texto = "Leche media"
    elif milk == "Baja":
        estilo = "Intenso"
        leche_texto = "Poca leche"
    elif milk == "Sin leche":
        estilo = "Directo"
        leche_texto = "Sin leche"
    else:
        estilo = "Refrescante" if "Iced" in bebida_final or bebida_final == "Cold Brew" else "Balanceado"
        leche_texto = "Leche opcional"

    if intensity in ["Baja-media", "Baja"]:
        intensidad_texto = "Suave"
    elif intensity == "Media":
        intensidad_texto = "Equilibrado"
    elif intensity == "Media-alta":
        intensidad_texto = "Con carácter"
    elif intensity == "Alta":
        intensidad_texto = "Intenso"
    else:
        intensidad_texto = "Equilibrado"

    return f"Perfil: {estilo} · {intensidad_texto} · {leche_texto}"


def choose_option(q):
    options = q["options"]
    cols = st.columns(2, gap="small")

    for idx, option in enumerate(options):
        col = cols[idx % 2]

        with col:
            st.markdown('<div class="option-card">', unsafe_allow_html=True)
            st.image(option["image"], use_container_width=True)
            st.markdown(f'<div class="option-title">{option["label"]}</div>', unsafe_allow_html=True)

            if st.button(
                "Elegir",
                key=f"{q['key']}_{option['value']}",
                use_container_width=True,
                type="primary"
            ):
                st.session_state.answers[q["key"]] = option["value"]
                st.session_state.step += 1
                st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)


def reset_quiz():
    st.session_state.step = 0
    st.session_state.answers = {}
    st.rerun()


st.markdown("""
<div class="hero">
    <div class="hero-title">☕ Coffee Match</div>
    <div class="hero-subtitle">Descubre tu café ideal en menos de 1 minuto.</div>
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

    choose_option(q)

    nav_cols = st.columns([1, 1])
    with nav_cols[0]:
        if current_step > 0:
            if st.button("⬅️ Atrás", use_container_width=True, type="secondary"):
                st.session_state.step -= 1
                st.rerun()
    with nav_cols[1]:
        if current_step > 0:
            if st.button("🔁 Reiniciar", use_container_width=True, type="secondary"):
                reset_quiz()

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
        <div class="result-description">{descripcion(final_1 if final_1 in BEVERAGE_INFO else bebida_1)}</div>
        <br>
        <div style="font-size:13px; opacity:0.9;">{build_result_details(final_1, bebida_1)}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="profile-card">
        <b>El café que va contigo:</b><br>
        {perfil_usuario(st.session_state.answers)}
    </div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2, gap="small")

    with col_a:
        st.markdown(f"""
        <div class="alt-card">
            <b>🔄 Alternativa</b><br>
            {final_2}<br>
            <b>{score_2}% match</b>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown(f"""
        <div class="alt-card">
            <b>🎯 Explora</b><br>
            {final_3}<br>
            <b>{score_3}% match</b>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="small-note">
        Comparte tu resultado y prueba tu match en tu próxima visita.
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔁 Hacer el quiz otra vez", use_container_width=True, type="primary"):
        reset_quiz()
