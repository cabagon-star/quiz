import html
import json
from pathlib import Path
from urllib.parse import urlencode

import streamlit as st
import streamlit.components.v1 as components

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

PUBLIC_APP_URL = "https://coffeeonematch.streamlit.app"


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
   GENERAL
========================================================= */

.stApp {
    background:
        radial-gradient(
            circle at 50% 0%,
            rgba(0, 210, 240, 0.07),
            transparent 24%
        ),
        linear-gradient(
            180deg,
            #020202 0%,
            #080808 100%
        );

    color: #FFFFFF;
}

.block-container {
    max-width: 720px;
    padding-top: 18px;
    padding-bottom: 50px;
}

#MainMenu,
footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* =========================================================
   CABECERA
========================================================= */

.brand-mini {
    text-align: center;
    margin-bottom: 18px;
}

.brand-name {
    font-size: 24px;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: -0.6px;
    margin-top: 6px;
}

.brand-name span {
    color: #00D5EE;
}

.brand-tagline {
    color: #AFAFAF;
    font-size: 12px;
    margin-top: 2px;
}

div[data-testid="stImage"] img {

    border-radius: 20px;

    border:
        1px solid
        rgba(211,155,38,0.52);

    box-shadow:
        0 10px 28px
        rgba(0,0,0,0.50);
}


/* =========================================================
   PROGRESO
========================================================= */

.progress-row {

    display: flex;
    justify-content: space-between;
    align-items: center;

    font-size: 11px;
    font-weight: 700;

    letter-spacing: 0.7px;

    color: #C8A85A;

    margin-bottom: 7px;
}

.progress-bg {

    width: 100%;
    height: 6px;

    border-radius: 999px;

    background: #1B1B1B;

    overflow: hidden;

    margin-bottom: 18px;
}

.progress-fill {

    height: 100%;

    border-radius: 999px;

    background:
        linear-gradient(
            90deg,
            #C88C1D,
            #FFD43B
        );

    box-shadow:
        0 0 10px
        rgba(255,212,59,0.30);

    transition: width 0.25s ease;
}


/* =========================================================
   PREGUNTA
========================================================= */

.question-card {

    background: #0C0C0C;

    border:
        1px solid
        rgba(211,155,38,0.38);

    border-radius: 24px;

    padding: 25px 26px;

    margin-bottom: 16px;

    box-shadow:
        0 14px 35px
        rgba(0,0,0,0.38);
}

.question-number {

    color: #00D5EE;

    font-size: 11px;
    font-weight: 800;

    letter-spacing: 1.2px;

    margin-bottom: 8px;
}

.question-title {

    color: #FFFFFF;

    font-size: 27px;
    font-weight: 760;

    line-height: 1.18;

    letter-spacing: -0.5px;
}


/* =========================================================
   OPCIONES
========================================================= */

div[role="radiogroup"] {
    gap: 7px;
}

div[role="radiogroup"] > label {

    background: #101010;

    border:
        1px solid
        rgba(255,255,255,0.10);

    border-radius: 16px;

    padding: 14px 16px;

    margin-bottom: 5px;

    min-height: 54px;

    transition:
        background 0.15s ease,
        border-color 0.15s ease,
        transform 0.15s ease;
}

div[role="radiogroup"] > label:hover {

    border-color: #00D5EE;

    background: #10191B;

    transform: translateY(-1px);
}

div[role="radiogroup"] > label:has(input:checked) {

    border-color: #D9A52D;

    background:
        linear-gradient(
            90deg,
            rgba(211,155,38,0.15),
            rgba(0,213,238,0.05)
        );
}

div[role="radiogroup"] p {

    color: #F6F6F6 !important;

    font-size: 16px !important;

    font-weight: 550 !important;
}


/* =========================================================
   BOTONES
========================================================= */

div.stButton > button {

    width: 100%;

    min-height: 45px;

    border-radius: 14px;

    border:
        1px solid
        rgba(211,155,38,0.50);

    background: #101010;

    color: #D4D4D4;

    font-size: 13px;

    font-weight: 650;

    margin-top: 6px;
}

div.stButton > button:hover {

    border-color: #00D5EE;

    color: #FFFFFF;

    background: #10191B;
}


/* link button */

a[data-testid="stBaseLinkButton-primary"],
a[data-testid="stBaseLinkButton-secondary"] {

    border-radius: 14px !important;

    min-height: 48px;

    font-weight: 700 !important;
}


/* =========================================================
   RESULTADOS
========================================================= */

.result-intro {

    text-align: center;

    margin-bottom: 20px;
}

.result-kicker {

    color: #00D5EE;

    font-size: 11px;

    font-weight: 800;

    letter-spacing: 1.5px;
}

.result-heading {

    color: #FFFFFF;

    font-size: 31px;

    font-weight: 800;

    letter-spacing: -0.8px;

    margin-top: 4px;
}


/* =========================================================
   COMPRA RÁPIDA
========================================================= */

.buy-now {

    background:
        linear-gradient(
            135deg,
            rgba(211,155,38,0.16),
            rgba(0,213,238,0.06)
        );

    border:
        1.5px solid
        #D39B26;

    border-radius: 26px;

    padding: 25px;

    margin-bottom: 20px;

    box-shadow:
        0 15px 38px
        rgba(0,0,0,0.42);
}

.buy-label {

    color: #FFD348;

    font-size: 11px;

    font-weight: 850;

    letter-spacing: 1.5px;

    margin-bottom: 8px;
}

.buy-title {

    color: #FFFFFF;

    font-size: 29px;

    font-weight: 820;

    line-height: 1.1;

    letter-spacing: -0.5px;

    margin-bottom: 8px;
}

.buy-description {

    color: #D4D4D4;

    font-size: 14px;

    line-height: 1.55;
}


/* =========================================================
   TARJETAS DE RECOMENDACIÓN
========================================================= */

.recommendation-card {

    background: #0D0D0D;

    border:
        1px solid
        rgba(211,155,38,0.30);

    border-radius: 23px;

    padding: 23px;

    margin-bottom: 15px;

    box-shadow:
        0 11px 28px
        rgba(0,0,0,0.32);
}

.recommendation-card.primary {

    border:
        1.5px solid
        #D39B26;
}

.card-top {

    display: flex;

    justify-content: space-between;

    gap: 16px;

    align-items: flex-start;

    margin-bottom: 15px;
}

.rank-label {

    color: #00D5EE;

    font-size: 10px;

    font-weight: 850;

    letter-spacing: 1.2px;

    margin-bottom: 5px;
}

.coffee-name {

    color: #FFFFFF;

    font-size: 22px;

    font-weight: 800;

    line-height: 1.15;
}

.match-score {

    white-space: nowrap;

    color: #FFD348;

    font-size: 14px;

    font-weight: 800;
}


/* =========================================================
   ATRIBUTOS
========================================================= */

.quick-meta {

    color: #BDBDBD;

    font-size: 13px;

    margin-bottom: 15px;
}

.attribute-grid {

    display: grid;

    grid-template-columns:
        repeat(2, minmax(0,1fr));

    gap: 8px;
}

.attribute {

    background: #151515;

    border-radius: 12px;

    padding: 10px 12px;
}

.attribute-label {

    color: #858585;

    font-size: 9px;

    font-weight: 800;

    letter-spacing: 0.8px;

    margin-bottom: 2px;
}

.attribute-value {

    color: #F2F2F2;

    font-size: 13px;

    font-weight: 650;
}


/* =========================================================
   TIP
========================================================= */

.coffee-tip {

    margin-top: 14px;

    background:
        rgba(0,213,238,0.07);

    border-left:
        3px solid
        #00D5EE;

    border-radius: 8px;

    padding: 11px 13px;

    color: #DCDCDC;

    font-size: 12px;

    line-height: 1.45;
}


/* =========================================================
   COMPARTIR
========================================================= */

.share-title {

    text-align: center;

    color: #AFAFAF;

    font-size: 11px;

    font-weight: 700;

    letter-spacing: 0.8px;

    margin-top: 23px;
    margin-bottom: 8px;
}


/* =========================================================
   RESULTADO COMPARTIDO
========================================================= */

.shared-note {

    text-align: center;

    color: #AFAFAF;

    font-size: 13px;

    line-height: 1.5;

    margin:
        -5px 0
        20px 0;
}


/* =========================================================
   FOOTER
========================================================= */

.footer-text {

    text-align: center;

    color: #707070;

    font-size: 10px;

    letter-spacing: 0.7px;

    margin-top: 28px;
}


/* =========================================================
   MÓVIL
========================================================= */

@media (max-width: 640px) {

    .block-container {
        padding:
            12px 16px
            35px 16px;
    }

    .question-card {
        padding: 22px 20px;
    }

    .question-title {
        font-size: 24px;
    }

    div[role="radiogroup"] > label {
        min-height: 52px;
        padding: 13px 14px;
    }

    .result-heading {
        font-size: 27px;
    }

    .buy-title {
        font-size: 25px;
    }

    .coffee-name {
        font-size: 20px;
    }

    .attribute-grid {
        grid-template-columns: 1fr 1fr;
    }
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
# LOGO
# 20% MÁS PEQUEÑO
# ============================================================

logo_left, logo_center, logo_right = st.columns(
    [2.3, 0.8, 2.3]
)

with logo_center:

    if LOGO_PATH.exists():

        st.image(
            str(LOGO_PATH),
            use_container_width=True
        )


# ============================================================
# MARCA
# ============================================================

brand_html = (
    '<div class="brand-mini">'
    '<div class="brand-name">'
    'Coffee<span>Match</span>'
    '</div>'
    '<div class="brand-tagline">'
    'Tu café ideal, sin complicaciones.'
    '</div>'
    '</div>'
)

st.markdown(
    brand_html,
    unsafe_allow_html=True
)


# ============================================================
# RESULTADO COMPARTIDO
# ============================================================

shared_result = (
    st.query_params.get("shared")
    == "1"
)


if shared_result:

    shared_coffee = st.query_params.get(
        "coffee",
        "Coffee Match"
    )

    shared_origin = st.query_params.get(
        "origin",
        ""
    )

    shared_roast = st.query_params.get(
        "roast",
        ""
    )

    shared_flavor = st.query_params.get(
        "flavor",
        ""
    )

    shared_acidity = st.query_params.get(
        "acidity",
        ""
    )

    shared_body = st.query_params.get(
        "body",
        ""
    )

    shared_method = st.query_params.get(
        "method",
        ""
    )

    shared_temperature = st.query_params.get(
        "temperature",
        ""
    )

    shared_score = st.query_params.get(
        "score",
        ""
    )


    # ========================================================
    # ENCABEZADO
    # ========================================================

    st.markdown(
        (
            '<div class="result-intro">'
            '<div class="result-kicker">'
            'COFFEE MATCH COMPARTIDO'
            '</div>'
            '<div class="result-heading">'
            'Este fue su Coffee Match'
            '</div>'
            '</div>'
        ),
        unsafe_allow_html=True
    )


    st.markdown(
        (
            '<div class="shared-note">'
            'Mira su recomendación y después descubre cuál sería la tuya.'
            '</div>'
        ),
        unsafe_allow_html=True
    )


    # ========================================================
    # SCORE
    # ========================================================

    score_html = ""

    if shared_score:

        score_html = (
            '<div class="match-score">'
            f'{html.escape(str(shared_score))}% match'
            '</div>'
        )


    # ========================================================
    # MÉTODO + TEMPERATURA
    # ========================================================

    meta_parts = []

    if shared_method:
        meta_parts.append(
            html.escape(
                str(shared_method)
            )
        )

    if shared_temperature:
        meta_parts.append(
            html.escape(
                str(shared_temperature)
            )
        )

    shared_meta = (
        " · ".join(
            meta_parts
        )
    )


    # ========================================================
    # TARJETA COMPARTIDA
    # ========================================================

    shared_card = (
        '<div class="recommendation-card primary">'

        '<div class="card-top">'

        '<div>'

        '<div class="rank-label">'
        '⭐ COFFEE MATCH'
        '</div>'

        '<div class="coffee-name">'
        f'{html.escape(str(shared_coffee))}'
        '</div>'

        '</div>'

        f'{score_html}'

        '</div>'

        f'<div class="quick-meta">'
        f'{shared_meta}'
        '</div>'

        '<div class="attribute-grid">'

        '<div class="attribute">'
        '<div class="attribute-label">'
        'ORIGEN'
        '</div>'
        '<div class="attribute-value">'
        f'{html.escape(str(shared_origin))}'
        '</div>'
        '</div>'

        '<div class="attribute">'
        '<div class="attribute-label">'
        'TOSTADO'
        '</div>'
        '<div class="attribute-value">'
        f'{html.escape(str(shared_roast))}'
        '</div>'
        '</div>'

        '<div class="attribute">'
        '<div class="attribute-label">'
        'PERFIL'
        '</div>'
        '<div class="attribute-value">'
        f'{html.escape(str(shared_flavor))}'
        '</div>'
        '</div>'

        '<div class="attribute">'
        '<div class="attribute-label">'
        'ACIDEZ'
        '</div>'
        '<div class="attribute-value">'
        f'{html.escape(str(shared_acidity))}'
        '</div>'
        '</div>'

        '<div class="attribute">'
        '<div class="attribute-label">'
        'CUERPO'
        '</div>'
        '<div class="attribute-value">'
        f'{html.escape(str(shared_body))}'
        '</div>'
        '</div>'

        '</div>'

        '</div>'
    )


    st.markdown(
        shared_card,
        unsafe_allow_html=True
    )


    # ========================================================
    # HACER SU PROPIO TEST
    # ========================================================

    st.link_button(
        "☕ Descubre tu propio Coffee Match",
        PUBLIC_APP_URL,
        use_container_width=True
    )


    st.markdown(
        (
            '<div class="footer-text">'
            'COFFEE MATCH · FIND YOUR COFFEE'
            '</div>'
        ),
        unsafe_allow_html=True
    )


    st.stop()


# ============================================================
# SECUENCIA DINÁMICA
# ============================================================

def get_question_sequence():

    sequence = list(
        questions.keys()
    )

    # P9 = pregunta 7.1
    # Solo aparece si P8 = A veces o Sí

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


# ============================================================
# AVANZAR
# ============================================================

def go_forward():

    sequence = get_question_sequence()

    if (
        st.session_state.step
        < len(sequence) - 1
    ):

        st.session_state.step += 1

    else:

        st.session_state.finished = True


# ============================================================
# RESPONDER + AVANZAR
# ============================================================

def answer_question(
    question_key,
    widget_key
):

    selected = (
        st.session_state.get(
            widget_key
        )
    )

    if selected is None:
        return


    st.session_state.answers[
        question_key
    ] = selected


    # ========================================================
    # LÓGICA 7.1
    # ========================================================

    if question_key == "P8":

        # NO QUIERE LECHE
        if selected == "A":

            st.session_state.answers[
                "P9"
            ] = "F"

            if (
                "answer_P9"
                in st.session_state
            ):

                del st.session_state[
                    "answer_P9"
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


    go_forward()


# ============================================================
# QUIZ
# ============================================================

if not st.session_state.finished:

    question_keys = (
        get_question_sequence()
    )

    step = (
        st.session_state.step
    )

    question_key = (
        question_keys[step]
    )


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
    # NÚMERO
    # ========================================================

    first_part = (
        question_text.split(
            " ",
            1
        )[0]
    )

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
    # PROGRESO
    # ========================================================

    try:

        main_number = int(
            float(
                display_number
            )
        )

    except:

        main_number = 1


    progress = min(
        main_number * 10,
        100
    )


    progress_html = (
        '<div class="progress-row">'
        '<span>ENCUENTRA TU MATCH</span>'
        f'<span>{display_number} / 10</span>'
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
    # TARJETA DE PREGUNTA
    # ========================================================

    question_html = (
        '<div class="question-card">'
        '<div class="question-number">'
        f'PREGUNTA {display_number}'
        '</div>'
        '<div class="question-title">'
        f'{html.escape(clean_question)}'
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


    if (
        previous_answer
        in option_keys
    ):

        default_index = (
            option_keys.index(
                previous_answer
            )
        )

    else:

        default_index = None


    widget_key = (
        f"answer_{question_key}"
    )


    st.radio(

        "Respuesta",

        option_keys,

        index=default_index,

        format_func=lambda key:
            options[key],

        key=widget_key,

        label_visibility="collapsed",

        on_change=answer_question,

        args=(
            question_key,
            widget_key
        )
    )


    # ========================================================
    # NAVEGACIÓN
    # ========================================================

    nav_left, nav_right = (
        st.columns(
            [1, 1]
        )
    )


    if step > 0:

        with nav_left:

            if st.button(
                "← Atrás",
                use_container_width=True,
                key=f"back_{question_key}"
            ):

                st.session_state.step -= 1

                st.rerun()


    if (
        question_key
        in st.session_state.answers
    ):

        with nav_right:

            if st.button(
                "Siguiente →",
                use_container_width=True,
                key=f"forward_{question_key}"
            ):

                go_forward()

                st.rerun()


# ============================================================
# RESULTADOS
# ============================================================

else:

    answers = (
        st.session_state.answers
    )


    scores = calculate_scores(
        answers
    )


    top = get_top_recommendations(
        scores,
        answers
    )


    # ========================================================
    # ENCABEZADO
    # ========================================================

    st.markdown(
        (
            '<div class="result-intro">'
            '<div class="result-kicker">'
            'TU COFFEE MATCH'
            '</div>'
            '<div class="result-heading">'
            'Esto es lo que compraría'
            '</div>'
            '</div>'
        ),
        unsafe_allow_html=True
    )


    # ========================================================
    # COMPRA RÁPIDA
    # ========================================================

    if top:

        best = top[0]

        best_profile = (
            best["perfil"]
        )


        best_name = html.escape(
            str(
                best["bebida"]
            )
        )

        origin = html.escape(
            str(
                best_profile["origen"]
            )
        )

        roast = html.escape(
            str(
                best_profile["tostado"]
            )
        )

        flavor = html.escape(
            str(
                best_profile["sabor"]
            )
        )

        acidity = html.escape(
            str(
                best_profile["acidez"]
            )
        )

        body = html.escape(
            str(
                best_profile["cuerpo"]
            )
        )


        quick_buy_html = (
            '<div class="buy-now">'
            '<div class="buy-label">'
            '⚡ SI VAS A COMPRAR AHORA'
            '</div>'
            '<div class="buy-title">'
            f'{best_name}'
            '</div>'
            '<div class="buy-description">'
            f'Busca un café de <b>{origin}</b>, '
            f'tostado <b>{roast}</b>, '
            f'con perfil <b>{flavor}</b>. '
            f'Acidez {acidity} y cuerpo {body}.'
            '</div>'
            '</div>'
        )


        st.markdown(
            quick_buy_html,
            unsafe_allow_html=True
        )


    # ========================================================
    # TARJETAS DE RECOMENDACIONES
    # ========================================================

    for i, r in enumerate(
        top,
        1
    ):

        p = r["perfil"]


        # ====================================================
        # ETIQUETA
        # ====================================================

        if i == 1:

            rank_text = (
                "⭐ MEJOR MATCH"
            )

            card_class = (
                "recommendation-card primary"
            )

        elif i == 2:

            rank_text = (
                "ALTERNATIVA CERCANA"
            )

            card_class = (
                "recommendation-card"
            )

        else:

            rank_text = (
                "PARA EXPLORAR"
            )

            card_class = (
                "recommendation-card"
            )


        # ====================================================
        # SCORE
        # ====================================================

        if isinstance(
            r["score"],
            (int, float)
        ):

            score_text = (
                f"{r['score']}% match"
            )

        else:

            score_text = (
                str(
                    r["score"]
                )
            )


        # ====================================================
        # TEMPERATURA
        # ====================================================

        temperature = (
            "Frío"
            if r["temperatura"] == "iced"
            else "Caliente"
        )


        # ====================================================
        # SABOR EXTRA
        # ====================================================

        if (
            answers.get("P12")
            == "A"
        ):

            added_flavor = (
                "Ninguno"
            )

        else:

            added_flavor = (
                flavor_add_map.get(
                    answers.get("P12"),
                    "Natural"
                )
            )


        # ====================================================
        # TEXTO
        # ====================================================

        bebida = html.escape(
            str(
                r["bebida"]
            )
        )

        method = html.escape(
            str(
                method_names[
                    r["metodo"]
                ]
            )
        )

        origin = html.escape(
            str(
                p["origen"]
            )
        )

        flavor = html.escape(
            str(
                p["sabor"]
            )
        )

        acidity = html.escape(
            str(
                p["acidez"]
            )
        )

        body = html.escape(
            str(
                p["cuerpo"]
            )
        )

        roast = html.escape(
            str(
                p["tostado"]
            )
        )

        milk = html.escape(
            str(
                p["leche"]
            )
        )

        added_flavor = html.escape(
            str(
                added_flavor
            )
        )


        # ====================================================
        # TIP
        # ====================================================

        tip_html = ""

        if p.get(
            "recomendacion"
        ):

            tip = html.escape(
                str(
                    p[
                        "recomendacion"
                    ]
                ).strip()
            )

            tip_html = (
                '<div class="coffee-tip">'
                f'💡 {tip}'
                '</div>'
            )


        # ====================================================
        # CARD
        # ====================================================

        card_html = (
            f'<div class="{card_class}">'

            '<div class="card-top">'

            '<div>'

            '<div class="rank-label">'
            f'{rank_text}'
            '</div>'

            '<div class="coffee-name">'
            f'{bebida}'
            '</div>'

            '</div>'

            '<div class="match-score">'
            f'{score_text}'
            '</div>'

            '</div>'

            '<div class="quick-meta">'
            f'{method} · {temperature}'
            '</div>'

            '<div class="attribute-grid">'

            '<div class="attribute">'
            '<div class="attribute-label">'
            'ORIGEN'
            '</div>'
            '<div class="attribute-value">'
            f'{origin}'
            '</div>'
            '</div>'

            '<div class="attribute">'
            '<div class="attribute-label">'
            'TOSTADO'
            '</div>'
            '<div class="attribute-value">'
            f'{roast}'
            '</div>'
            '</div>'

            '<div class="attribute">'
            '<div class="attribute-label">'
            'PERFIL'
            '</div>'
            '<div class="attribute-value">'
            f'{flavor}'
            '</div>'
            '</div>'

            '<div class="attribute">'
            '<div class="attribute-label">'
            'ACIDEZ'
            '</div>'
            '<div class="attribute-value">'
            f'{acidity}'
            '</div>'
            '</div>'

            '<div class="attribute">'
            '<div class="attribute-label">'
            'CUERPO'
            '</div>'
            '<div class="attribute-value">'
            f'{body}'
            '</div>'
            '</div>'

            '<div class="attribute">'
            '<div class="attribute-label">'
            'LECHE'
            '</div>'
            '<div class="attribute-value">'
            f'{milk}'
            '</div>'
            '</div>'

            '<div class="attribute">'
            '<div class="attribute-label">'
            'SABOR EXTRA'
            '</div>'
            '<div class="attribute-value">'
            f'{added_flavor}'
            '</div>'
            '</div>'

            '</div>'

            f'{tip_html}'

            '</div>'
        )


        st.markdown(
            card_html,
            unsafe_allow_html=True
        )


    # ========================================================
    # COMPARTIR COFFEE MATCH
    # ========================================================

    if top:

        best = top[0]

        best_profile = (
            best["perfil"]
        )


        # ====================================================
        # SCORE PARA COMPARTIR
        # ====================================================

        if isinstance(
            best["score"],
            (int, float)
        ):

            share_score = (
                f"{best['score']:g}"
            )

        else:

            share_score = ""


        # ====================================================
        # TEMPERATURA
        # ====================================================

        share_temperature = (
            "Frío"
            if best["temperatura"] == "iced"
            else "Caliente"
        )


        # ====================================================
        # CREAR URL DEL RESULTADO
        # ====================================================

        share_params = {

            "shared": "1",

            "coffee":
                best["bebida"],

            "origin":
                best_profile["origen"],

            "roast":
                best_profile["tostado"],

            "flavor":
                best_profile["sabor"],

            "acidity":
                best_profile["acidez"],

            "body":
                best_profile["cuerpo"],

            "method":
                method_names[
                    best["metodo"]
                ],

            "temperature":
                share_temperature,

            "score":
                share_score
        }


        share_url = (
            PUBLIC_APP_URL
            + "?"
            + urlencode(
                share_params
            )
        )


        # ====================================================
        # TEXTO
        # ====================================================

        share_title = (
            "Mi Coffee Match"
        )


        share_text = (
            f"☕ Mi Coffee Match fue: "
            f"{best['bebida']}\n"
            f"Origen: {best_profile['origen']} · "
            f"Tostado: {best_profile['tostado']}\n\n"
            "Mira mi resultado y descubre cuál es el tuyo."
        )


        # ====================================================
        # CONVERTIR PARA JAVASCRIPT
        # ====================================================

        js_title = json.dumps(
            share_title
        )

        js_text = json.dumps(
            share_text
        )

        js_url = json.dumps(
            share_url
        )


        st.markdown(
            (
                '<div class="share-title">'
                'COMPARTE TU RESULTADO'
                '</div>'
            ),
            unsafe_allow_html=True
        )


        # ====================================================
        # BOTÓN SHARE
        # ====================================================

        components.html(
            f"""
            <style>

            html, body {{
                margin: 0;
                padding: 0;
                background: transparent;

                font-family:
                    Arial,
                    Helvetica,
                    sans-serif;
            }}


            .share-button {{

                width: 100%;
                height: 52px;

                border-radius: 14px;

                border:
                    1px solid
                    #00D5EE;

                background:
                    linear-gradient(
                        135deg,
                        #10191B,
                        #101010
                    );

                color: #FFFFFF;

                font-size: 15px;

                font-weight: 700;

                cursor: pointer;

                transition:
                    all 0.15s ease;
            }}


            .share-button:hover {{

                background:
                    linear-gradient(
                        135deg,
                        #00D5EE,
                        #009FB5
                    );

                color: #061013;
            }}


            .share-message {{

                display: none;

                color: #D2D2D2;

                text-align: center;

                font-size: 12px;

                padding-top: 7px;
            }}

            </style>


            <button
                class="share-button"
                onclick="shareCoffee()"
            >
                ↗ Compartir mi Coffee Match
            </button>


            <div
                id="share-message"
                class="share-message"
            >
            </div>


            <script>

            async function shareCoffee() {{

                const title =
                    {js_title};

                const text =
                    {js_text};

                const url =
                    {js_url};


                const message =
                    document.getElementById(
                        "share-message"
                    );


                if (navigator.share) {{

                    try {{

                        await navigator.share({{
                            title: title,
                            text: text,
                            url: url
                        }});

                    }}

                    catch (error) {{

                        // Si el usuario cancela,
                        // no mostramos error.

                    }}

                }}

                else {{

                    const fullText =
                        text
                        + "\\n"
                        + url;


                    try {{

                        await navigator.clipboard.writeText(
                            fullText
                        );


                        message.innerText =
                            "✓ Resultado y enlace copiados";


                        message.style.display =
                            "block";

                    }}

                    catch (error) {{

                        message.innerText =
                            "Copia este enlace: "
                            + url;


                        message.style.display =
                            "block";

                    }}

                }}

            }}

            </script>
            """,

            height=78
        )


    # ========================================================
    # VOLVER A HACER EL TEST
    # ========================================================

    if st.button(
        "↻ Volver a hacer el test",
        use_container_width=True,
        key="restart_button"
    ):

        keys_to_delete = [

            key

            for key
            in st.session_state.keys()

            if (
                key.startswith(
                    "answer_"
                )
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

st.markdown(
    (
        '<div class="footer-text">'
        'COFFEE MATCH · FIND YOUR COFFEE'
        '</div>'
    ),
    unsafe_allow_html=True
)
