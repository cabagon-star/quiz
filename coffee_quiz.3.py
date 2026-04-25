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

.hero {
    background: linear-gradient(135deg, #006241 0%, #1e3932 100%);
    padding: 26px;
    border-radius: 26px;
    color: white;
    text-align: center;
    margin-bottom: 18px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.14);
}

.hero-title {
    font-size: 36px;
    font-weight: 900;
}

.hero-subtitle {
    font-size: 15px;
    opacity: 0.95;
}

.question-card {
    background-color: white;
    padding: 18px;
    border-radius: 22px;
    border: 1px solid #e5dfd4;
    box-shadow: 0 6px 18px rgba(0,0,0,0.07);
    margin-bottom: 14px;
}

.question-title {
    color: #1e3932;
    font-size: 23px;
    font-weight: 900;
    text-align: center;
}

.helper {
    color: #6f6259;
    text-align: center;
    font-size: 14px;
    margin-top: 4px;
}

.option-card {
    background-color: white;
    border: 1px solid #ded6c8;
    border-radius: 18px;
    padding: 8px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    margin-bottom: 10px;
}

.option-title {
    color: #1e3932;
    font-size: 15px;
    font-weight: 800;
    margin-top: 4px;
    margin-bottom: 6px;
}

.stButton > button {
    background-color: #006241;
    color: white;
    border-radius: 999px;
    border: none;
    padding: 8px 14px;
    font-weight: 800;
    width: 100%;
}

.stButton > button:hover {
    background-color: #1e3932;
    color: white;
}

.result-card {
    background: linear-gradient(135deg, #006241 0%, #1e3932 100%);
    color: white;
    padding: 28px;
    border-radius: 28px;
    text-align: center;
    margin-top: 20px;
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
}

.result-name {
    font-size: 34px;
    font-weight: 900;
}

.match {
    font-size: 17px;
    opacity: 0.95;
    margin-top: 6px;
}

.profile-card {
    background-color: #d4e9e2;
    color: #1e3932;
    padding: 18px;
    border-radius: 20px;
    margin-top: 16px;
}

.alt-card {
    background-color: white;
    color: #1e3932;
    padding: 16px;
    border-radius: 18px;
    margin-top: 12px;
    border: 1px solid #d8d0c3;
    box-shadow: 0 4px 14px rgba(0,0,0,0.04);
}

.small-note {
    color: #6f6259;
    font-size: 13px;
    text-align: center;
    margin-top: 18px;
}

@media (max-width: 600px) {
    .hero {
        padding: 20px;
        border-radius: 20px;
    }

    .hero-title {
        font-size: 29px;
    }

    .hero-subtitle {
        font-size: 14px;
    }

    .question-card {
        padding: 15px;
        border-radius: 18px;
    }

    .question-title {
        font-size: 20px;
    }

    .helper {
        font-size: 13px;
    }

    .option-card {
        padding: 6px;
        border-radius: 16px;
    }

    .option-title {
        font-size: 14px;
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
        "helper": "Elige el nivel de dulzor que más va contigo.",
        "options": [
            {"value": "Nada", "label": "Nada dulce", "image": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=500"},
            {"value": "Poco", "label": "Poco dulce", "image": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=500"},
            {"value": "Medio", "label": "Dulzor medio", "image": "https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=500"},
            {"value": "Mucho", "label": "Muy dulce", "image": "https://images.unsplash.com/photo-1541167760496-1628856ab772?w=500"},
        ]
    },
    {
        "key": "leche",
        "title": "¿Prefieres café con leche?",
        "helper": "La leche cambia textura, cuerpo y suavidad.",
        "options": [
            {"value": "Sin leche", "label": "Sin leche", "image": "https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?w=500"},
            {"value": "A veces", "label": "A veces", "image": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=500"},
            {"value": "Sí", "label": "Con leche", "image": "https://images.unsplash.com/photo-1570968915860-54d5c301fa9f?w=500"},
        ]
    },
    {
        "key": "textura",
        "title": "¿Qué textura prefieres?",
        "helper": "Piensa en cómo quieres sentir el café.",
        "options": [
            {"value": "Ligera", "label": "Ligera", "image": "https://images.unsplash.com/photo-1502462041640-b3d7e50d0662?w=500"},
            {"value": "Cremosa", "label": "Cremosa", "image": "https://images.unsplash.com/photo-1534778101976-62847782c213?w=500"},
            {"value": "Fuerte", "label": "Fuerte", "image": "https://images.unsplash.com/photo-1510707577719-ae7c14805e3a?w=500"},
        ]
    },
    {
        "key": "temperatura",
        "title": "¿Cómo lo prefieres?",
        "helper": "Caliente para clásico, frío para refrescante.",
        "options": [
            {"value": "Caliente", "label": "Caliente", "image": "https://images.unsplash.com/photo-1498804103079-a6351b050096?w=500"},
            {"value": "Frío", "label": "Frío", "image": "https://images.unsplash.com/photo-1517701604599-bb29b565090c?w=500"},
        ]
    },
    {
        "key": "aroma",
        "title": "¿Qué aroma te atrae más?",
        "helper": "Esto define el perfil sensorial.",
        "options": [
            {"value": "Chocolate", "label": "Chocolate", "image": "https://images.unsplash.com/photo-1606313564200-e75d5e30476c?w=500"},
            {"value": "Caramelo", "label": "Caramelo", "image": "https://images.unsplash.com/photo-1551024506-0bccd828d307?w=500"},
            {"value": "Frutal", "label": "Frutal", "image": "https://images.unsplash.com/photo-1567306226416-28f0efdc88ce?w=500"},
            {"value": "Nuez / Avellana", "label": "Nuez / Avellana", "image": "https://images.unsplash.com/photo-1508061253366-f7da158b6d46?w=500"},
        ]
    },
    {
        "key": "momento",
        "title": "¿Qué buscas al tomar café?",
        "helper": "Elige según tu mood del momento.",
        "options": [
            {"value": "Energía", "label": "Energía", "image": "https://images.unsplash.com/photo-1497636577773-f1231844b336?w=500"},
            {"value": "Relajarme", "label": "Relajarme", "image": "https://images.unsplash.com/photo-1511081692775-05d0f180a065?w=500"},
            {"value": "Balance", "label": "Balance", "image": "https://images.unsplash.com/photo-1523942839745-7848c839b661?w=500"},
            {"value": "Acompañar algo dulce", "label": "Algo dulce", "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=500"},
        ]
    },
]


if "step" not in st.session_state:
    st.session_state.step = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}


def calcular_recomendacion(answers):
    dulzor = answers["dulzor"]
    leche = answers["leche"]
    textura = answers["textura"]
    temperatura = answers["temperatura"]
    aroma = answers["aroma"]
    momento = answers["momento"]

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


def perfil_usuario(answers):
    leche = answers["leche"]
    textura = answers["textura"]
    temperatura = answers["temperatura"]
    aroma = answers["aroma"]

    if leche == "Sí":
        base = "cremoso"
    elif leche == "Sin leche":
        base = "intenso y directo"
    else:
        base = "balanceado"

    return f"Perfil {base}, con preferencia {aroma.lower()}, textura {textura.lower()} y estilo {temperatura.lower()}."


def choose_option(q):
    options = q["options"]
    cols = st.columns(2)

    for idx, option in enumerate(options):
        col = cols[idx % 2]

        with col:
            st.markdown('<div class="option-card">', unsafe_allow_html=True)
            st.image(option["image"], width=150)
            st.markdown(f'<div class="option-title">{option["label"]}</div>', unsafe_allow_html=True)

            if st.button(
                "Elegir",
                key=f"{q['key']}_{option['value']}",
                use_container_width=True
            ):
                st.session_state.answers[q["key"]] = option["value"]
                st.session_state.step += 1
                st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <div class="hero-title">☕ Coffee Match</div>
    <div class="hero-subtitle">Elige con imágenes y descubre tu café ideal.</div>
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

    if current_step > 0:
        if st.button("⬅️ Atrás", use_container_width=True):
            st.session_state.step -= 1
            st.rerun()

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
        <br>
        <div>{descripcion(bebida_1)}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="profile-card">
        <b>Tu perfil de sabor:</b><br>
        {perfil_usuario(st.session_state.answers)}
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

    if st.button("🔁 Reiniciar quiz", use_container_width=True):
        st.session_state.step = 0
        st.session_state.answers = {}
        st.rerun()

    st.markdown("""
    <div class="small-note">
        Este demo puede adaptarse al menú real de cualquier cafetería.
    </div>
    """, unsafe_allow_html=True)
