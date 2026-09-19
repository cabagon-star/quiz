import html
from pathlib import Path

import streamlit as st

from coffee_quiz_1 import (
    questions,
    conditional_questions,
    calculate_scores,
    get_top_recommendations,
    method_names,
    flavor_add_map
)


# ============================================================
# RUTAS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "Blue_coffee.png"


# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Coffee Match",
    page_icon="☕",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ============================================================
# ESTILO
# ============================================================

st.markdown("""
<style>

/* =========================================================
   PÁGINA
========================================================= */

.stApp {
    background:
        radial-gradient(
            circle at 50% 0%,
            rgba(0, 210, 240, 0.08),
            transparent 28%
        ),
        linear-gradient(
            180deg,
            #020202 0%,
            #080808 100%
        );

    color: #FFFFFF;
}

.block-container {
    max-width: 760px;
    padding-top: 32px;
    padding-bottom: 70px;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* =========================================================
   LOGO
========================================================= */

div[data-testid="stImage"] img {
    border-radius: 28px;

    border:
        1px solid
        rgba(211, 155, 38, 0.55);

    box-shadow:
        0 16px 38px
        rgba(0, 0, 0, 0.55);
}


/* =========================================================
   MARCA
========================================================= */

.brand-title {
    text-align: center;

    font-size: 42px;
    font-weight: 800;

    letter-spacing: -1.3px;

    color: #FFFFFF;

    margin-top: 10px;
    margin-bottom: 5px;
}

.brand-title span {
    color: #00D5EE;
}

.brand-subtitle {
    text-align: center;

    color: #C8C8C8;

    font-size: 15px;

    margin-bottom: 24px;
}

.gold-line {
    width: 130px;
    height: 3px;

    margin:
        0 auto
        38px auto;

    border-radius: 20px;

    background:
        linear-gradient(
            90deg,
            transparent,
            #D39B26,
            #FFD43B,
            #D39B26,
            transparent
        );
}


/* =========================================================
   PROGRESO
========================================================= */

.progress-row {
    display: flex;
    justify-content: space-between;
    align-items: center;

    font-size: 12px;
    font-weight: 700;

    letter-spacing: 0.9px;

    color: #D8B15D;

    margin-bottom: 9px;
}

.progress-bg {
    width: 100%;
    height: 8px;

    border-radius: 999px;

    background: #191919;

    border:
        1px solid
        rgba(211, 155, 38, 0.30);

    overflow: hidden;

    margin-bottom: 28px;
}

.progress-fill {
    height: 100%;

    border-radius: 999px;

    background:
        linear-gradient(
            90deg,
            #C78A17,
            #FFD43B
        );

    box-shadow:
        0 0 14px
        rgba(255, 212, 59, 0.35);
}


/* =========================================================
   PREGUNTA
========================================================= */

.question-card {
    background: #0D0D0D;

    border:
        1px solid
        rgba(211, 155, 38, 0.42);

    border-radius: 28px;

    padding: 34px;

    margin-bottom: 24px;

    box-shadow:
        0 18px 42px
        rgba(0, 0, 0, 0.40);
}

.question-number {
    color: #00D5EE;

    font-size: 12px;
    font-weight: 800;

    letter-spacing: 1.4px;

    margin-bottom: 14px;
}

.question-title {
    color: #FFFFFF;

    font-size: 28px;
    font-weight: 760;

    line-height: 1.25;

    letter-spacing: -0.5px;

    margin-bottom: 10px;
}

.question-helper {
    color: #BEBEBE;

    font-size: 14px;
}


/* =========================================================
   OPCIONES
========================================================= */

div[role="radiogroup"] {
    gap: 8px;
}

div[role="radiogroup"] > label {
    background: #111111;

    border:
        1px solid
        rgba(255, 255, 255, 0.11);

    border-radius: 17px;

    padding: 15px 18px;

    margin-bottom: 8px;

    min-height: 58px;

    color: #FFFFFF;

    font-size: 16px;

    transition: 0.15s ease;
}

div[role="radiogroup"] > label:hover {
    border-color: #00D5EE;

    background: #101A1C;
}

div[role="radiogroup"] p {
    color: #F5F5F5 !important;
}


/* =========================================================
   BOTONES
========================================================= */

div.stButton > button {
    width: 100%;

    min-height: 54px;

    border-radius: 16px;

    border: 1px solid #D39B26;

    background:
        linear-gradient(
            180deg,
            #D39B26 0%,
            #A97112 100%
        );

    color: #FFFFFF;

    font-size: 15px;

    font-weight: 750;

    margin-top: 8px;

    transition: 0.15s ease;
}

div.stButton > button:hover {
    border-color: #00D5EE;

    background:
        linear-gradient(
            180deg,
            #00D5EE,
            #00A9C1
        );

    color: #061013;
}


/* =========================================================
   RESULTADOS: HEADER
========================================================= */

.result-header {
    background: #090909;

    border:
        1.5px solid
        #D39B26;

    border-radius: 28px;

    padding: 34px;

    text-align: center;

    margin-bottom: 28px;

    box-shadow:
        0 18px 42px
        rgba(0, 0, 0, 0.45);
}

.result-label {
    color: #00D5EE;

    font-size: 12px;

    font-weight: 800;

    letter-spacing: 1.5px;

    margin-bottom: 10px;
}

.result-title {
    color: #FFFFFF;

    font-size: 31px;

    font-weight: 800;

    margin-bottom: 7px;
}

.result-subtitle {
    color: #BDBDBD;

    font-size: 14px;
}


/* =========================================================
   RESULTADOS: CAJA
========================================================= */

.result-box {
    background: #0D0D0D;

    border:
        1px solid
        rgba(211, 155, 38, 0.55);

    border-radius: 24px;

    padding: 26px;

    margin-top: 10px;
    margin-bottom: 22px;

    box-shadow:
        0 12px 32px
        rgba(0, 0, 0, 0.40);
}

.result-box pre {
    margin: 0;

    white-space: pre-wrap;

    word-wrap: break-word;

    overflow-wrap: anywhere;

    color: #F5F1E8 !important;

    font-size: 15px;

    line-height: 1.75;

    font-family:
        "Courier New",
        monospace;
}


/* =========================================================
   ALERTAS
========================================================= */

div[data-baseweb="notification"] {
    background: #111111;

    border:
        1px solid
        #D39B26;

    color: white;
}


/* =========================================================
   FOOTER
========================================================= */

.footer-text {
    text-align: center;

    color: #8E8E8E;

    font-size: 11px;

    letter-spacing: 0.7px;

    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "step" not in st.session_state:
    st.session_state.step = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "finished" not in st.session_state:
    st.session_state.finished = False


# ============================================================
# LOGO CENTRADO
# ============================================================

if LOGO_PATH.exists():

    col_left, col_center, col_right = st.columns(
        [1, 2, 1]
    )

    with col_center:

        st.image(
            str(LOGO_PATH),
            use_container_width=True
        )

else:

    st.error(
        "No encontré Blue_coffee.png. "
        f"Debe estar en: {LOGO_PATH}"
    )


# ============================================================
# MARCA
# ============================================================

brand_html = (
    '<div class="brand-title">'
    'Coffee<span>Match</span>'
    '</div>'
    '<div class="brand-subtitle">'
    'Descubre el café que mejor se adapta a tus gustos.'
    '</div>'
    '<div class="gold-line"></div>'
)

st.markdown(
    brand_html,
    unsafe_allow_html=True
)


# ============================================================
# SECUENCIA DINÁMICA
# ============================================================

def get_question_sequence():

    sequence = list(
        questions.keys()
    )

    # P9 es la pregunta 7.1.
    # Solo aparece si P8 = A veces o Sí.

    if (
        st.session_state.answers.get("P8")
        in ["B", "C"]
    ):

        position = (
            sequence.index("P8") + 1
        )

        sequence.insert(
            position,
            "P9"
        )

    return sequence


question_keys = get_question_sequence()

total_questions = len(
    question_keys
)


# ============================================================
# QUIZ
# ============================================================

if not st.session_state.finished:

    step = st.session_state.step

    question_key = question_keys[
        step
    ]


    # ========================================================
    # OBTENER PREGUNTA
    # ========================================================

    if question_key == "P9":

        question_text, options = (
            conditional_questions["P9"]
        )

    else:

        question_text, options = (
            questions[question_key]
        )


    # ========================================================
    # PROGRESO
    # ========================================================

    progress = (
        (step + 1)
        / total_questions
    ) * 100


    progress_html = (
        '<div class="progress-row">'
        '<span>PERFIL DE CAFÉ</span>'
        f'<span>{step + 1} / {total_questions}</span>'
        '</div>'
        '<div class="progress-bg">'
        f'<div class="progress-fill" '
        f'style="width:{progress}%;"></div>'
        '</div>'
    )


    st.markdown(
        progress_html,
        unsafe_allow_html=True
    )


    # ========================================================
    # NÚMERO REAL DE LA PREGUNTA
    # ========================================================

    first_part = question_text.split(
        " ",
        1
    )[0]

    display_number = (
        first_part.rstrip(".")
    )


    if " " in question_text:

        clean_question = (
            question_text.split(
                " ",
                1
            )[1]
        )

    else:

        clean_question = (
            question_text
        )


    # ========================================================
    # TARJETA DE PREGUNTA
    # ========================================================

    question_html = (
        '<div class="question-card">'
        '<div class="question-number">'
        f'PREGUNTA {display_number}'
        '</div>'
        '<div class="question-title">'
        f'{clean_question}'
        '</div>'
        '<div class="question-helper">'
        'Selecciona la opción que mejor describa tu preferencia.'
        '</div>'
        '</div>'
    )


    st.markdown(
        question_html,
        unsafe_allow_html=True
    )


    # ========================================================
    # OPCIONES
    # ========================================================

    option_keys = list(
        options.keys()
    )


    previous_answer = (
        st.session_state.answers.get(
            question_key
        )
    )


    if previous_answer in option_keys:

        default_index = (
            option_keys.index(
                previous_answer
            )
        )

    else:

        default_index = None


    selected = st.radio(

        "Respuesta",

        option_keys,

        index=default_index,

        format_func=lambda key:
            f"{key} · {options[key]}",

        key=f"radio_{question_key}",

        label_visibility="collapsed"
    )


    # ========================================================
    # CONTINUAR
    # ========================================================

    if st.button(

        "Continuar →",

        use_container_width=True,

        key=f"continue_{question_key}"
    ):

        if selected is None:

            st.warning(
                "Selecciona una respuesta antes de continuar."
            )

        else:

            st.session_state.answers[
                question_key
            ] = selected


            # =================================================
            # PREGUNTA 7.1
            # =================================================

            if question_key == "P8":

                # NO QUIERE LECHE
                if selected == "A":

                    st.session_state.answers[
                        "P9"
                    ] = "F"


                    if (
                        "radio_P9"
                        in st.session_state
                    ):

                        del st.session_state[
                            "radio_P9"
                        ]


                # A VECES / SÍ
                else:

                    if (
                        st.session_state.answers.get(
                            "P9"
                        )
                        == "F"
                    ):

                        del st.session_state.answers[
                            "P9"
                        ]


            # Recalcular secuencia
            new_sequence = (
                get_question_sequence()
            )


            if (
                step
                < len(new_sequence) - 1
            ):

                st.session_state.step += 1

            else:

                st.session_state.finished = True


            st.rerun()


    # ========================================================
    # REGRESAR
    # ========================================================

    if step > 0:

        if st.button(

            "← Regresar",

            use_container_width=True,

            key=f"back_{question_key}"
        ):

            st.session_state.step -= 1

            st.rerun()


# ============================================================
# RESULTADOS
# ============================================================

else:

    answers = (
        st.session_state.answers
    )


    # ========================================================
    # MOTOR ORIGINAL
    # ========================================================

    scores = calculate_scores(
        answers
    )


    top = get_top_recommendations(
        scores,
        answers
    )


    # ========================================================
    # HEADER
    # ========================================================

    result_header = (
        '<div class="result-header">'
        '<div class="result-label">'
        'COFFEE MATCH COMPLETADO'
        '</div>'
        '<div class="result-title">'
        'Tus recomendaciones'
        '</div>'
        '<div class="result-subtitle">'
        'Basadas en tus preferencias de café.'
        '</div>'
        '</div>'
    )


    st.markdown(
        result_header,
        unsafe_allow_html=True
    )


    # ========================================================
    # RESULTADOS
    # SIN SCORES INTERNOS
    # ========================================================

    output = ""

    output += (
        "--- RESULTADOS ---\n\n"
    )


    for i, r in enumerate(
        top,
        1
    ):


        # TEMPERATURA

        temp_label = (

            "Frío"

            if r["temperatura"] == "iced"

            else "Caliente"

        )


        # PORCENTAJE

        score_label = (

            f"{r['score']}%"

            if isinstance(
                r["score"],
                (int, float)
            )

            else r["score"]

        )


        # NOMBRE

        output += (
            f"{i}. "
            f"{r['bebida']} "
            f"({temp_label}) "
            f"({score_label})\n"
        )


        p = r["perfil"]


        # MÉTODO

        output += (
            f"   Método: "
            f"{method_names[r['metodo']]}\n"
        )


        # ORIGEN

        output += (
            f"   Origen: "
            f"{p['origen']}\n"
        )


        # PERFIL

        output += (
            f"   Perfil: "
            f"{p['sabor']} | "
            f"Acidez {p['acidez']} | "
            f"Cuerpo {p['cuerpo']}\n"
        )


        # TOSTADO

        output += (
            f"   Tostado: "
            f"{p['tostado']}\n"
        )


        # LECHE

        output += (
            f"   Leche: "
            f"{p['leche']}\n"
        )


        # ====================================================
        # SABOR AÑADIDO
        # ====================================================

        if (
            answers.get("P12")
            == "A"
        ):

            output += (
                "   Sabor añadido: Ninguno\n"
            )

        else:

            output += (
                f"   Sabor añadido: "
                f"{flavor_add_map[answers['P12']]}\n"
            )


        # ====================================================
        # ETIQUETAS ORIGINALES
        # ====================================================

        if i == 1:

            output += (
                "   ✅ Mejor match contigo\n"
            )

        elif i == 2:

            output += (
                "   🔄 Alternativa cercana a lo que tdentifica\n"
            )

        elif i == 3:

            output += (
                "   🎯 Opción para explorar algo diferente\n"
            )


        # ====================================================
        # RECOMENDACIÓN BARISTA
        # ====================================================

        if p.get(
            "recomendacion"
        ):

            output += (
                f"   💡 "
                f"{p['recomendacion'].strip()}\n"
            )


        output += "\n"


    # ========================================================
    # CAJA DE RESULTADOS
    # ========================================================

    safe_output = html.escape(
        output
    )


    result_html = (
        '<div class="result-box">'
        f'<pre>{safe_output}</pre>'
        '</div>'
    )


    st.markdown(
        result_html,
        unsafe_allow_html=True
    )


    # ========================================================
    # REINICIAR
    # ========================================================

    if st.button(

        "↻ Hacer Coffee Match nuevamente",

        use_container_width=True,

        key="restart_button"
    ):


        keys_to_delete = [

            key

            for key
            in st.session_state.keys()

            if key.startswith(
                "radio_"
            )

        ]


        for key in keys_to_delete:

            del st.session_state[
                key
            ]


        st.session_state.step = 0

        st.session_state.answers = {}

        st.session_state.finished = False


        st.rerun()


# ============================================================
# FOOTER
# ============================================================

footer_html = (
    '<div class="footer-text">'
    'COFFEE MATCH · PERSONALIZED COFFEE EXPERIENCE'
    '</div>'
)


st.markdown(
    footer_html,
    unsafe_allow_html=True
)