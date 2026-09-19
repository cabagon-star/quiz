from collections import defaultdict

method_names = {
    "ESP": "Espresso",
    "V60": "V60 / Filtrado",
    "MOK": "Moka italiana",
    "PRS": "Prensa francesa",
    "CLD": "Cold Brew"
}

milk_map = {
    "A": "Leche entera",
    "B": "Leche deslactosada",
    "C": "Leche de soya",
    "D": "Leche de avena",
    "E": "Leche de almendra",
    "F": "Sin leche"
}

flavor_add_map = {
    "A": "Natural",
    "B": "Vainilla",
    "C": "Caramelo",
    "D": "Avellana",
    "E": "Chocolate"
}

scoring = {
    "P1_A": {"BODY": 2, "ACID": -1, "CHO": 2, "ESP": 1, "MOK": 1},
    "P1_B": {"BODY": 1, "BAL": 1},
    "P1_C": {"ACID": 2, "FRU": 2, "V60": 1, "CLD": 1},

    "P2_A": {"CHO": 3, "BODY": 1},
    "P2_B": {"CAR": 3, "SWEET": 2},
    "P2_C": {"FRU": 3, "ACID": 2, "V60": 1, "CLD": 1},
    "P2_D": {"NUT": 3, "BODY": 1, "PRS": 1},

    "P3_A": {"ACID": 3, "FRU": 2, "V60": 1},
    "P3_B": {"ACID": 1, "BAL": 1},
    "P3_C": {"ACID": -2, "BODY": 1, "CHO": 1, "MOK": 1, "CLD": 1},

    "P4_A": {"BODY": -1, "ACID": 1, "V60": 2, "CLD": 1},
    "P4_B": {"BODY": 2, "MILK": 2},
    "P4_C": {"BODY": 3, "ESP": 2, "MOK": 1},
    "P4_D": {"BODY": 1, "PRS": 2},

    "P5_A": {"HIGH": 3, "ESP": 2, "MOK": 1, "BODY": 1},
    "P5_B": {"LOW": 3, "PRS": 2, "BODY": 1},
    "P5_C": {"BAL": 3, "ESP": 1, "CLD": 1},
    "P5_D": {"MILK": 2, "SWEET": 2, "LOW": 1},

    "P7_A": {"SWEET": -1, "BLACK": 1},
    "P7_B": {"SWEET": 1},
    "P7_C": {"SWEET": 3, "MILK": 2},
    "P7_D": {"SWEET": 2, "CAR": 1},

    "P8_A": {"BLACK": 3},
    "P8_B": {"MILK": 2},
    "P8_C": {"MILK": 3},

    "P9_A": {"MILK": 3, "BODY": 1},
    "P9_B": {"MILK": 3},
    "P9_C": {"MILK": 3},
    "P9_D": {"MILK": 3, "SWEET": 1},
    "P9_E": {"MILK": 3},
    "P9_F": {"BLACK": 3},

    "P10_A": {"ESP": 1, "MOK": 2},
    "P10_B": {"V60": 2, "PRS": 2},
    "P10_C": {"ESP": 2, "MILK": 1},
    "P10_D": {"BAL": 2, "CLD": 1},

    "P11_A": {"HOT": 3},
    "P11_B": {"COLD": 3, "CLD": 2},
    "P11_C": {"HOT": 1, "COLD": 1},

    "P12_A": {"PURE": 3},
    "P12_B": {"ADD_VAN": 3, "MILK": 1},
    "P12_C": {"ADD_CAR": 3, "SWEET": 1},
    "P12_D": {"ADD_NUT": 3, "NUT": 1},
    "P12_E": {"ADD_CHO": 3, "CHO": 1, "SWEET": 1},
}

questions = {
    "P1": ("1. ¿Te gusta lo amargo?", {
        "A": "Sí",
        "B": "Lo tolero",
        "C": "No"
    }),

    "P2": ("2. Aroma favorito:", {
        "A": "Chocolate",
        "B": "Caramelo / vainilla",
        "C": "Frutal / cítrico",
        "D": "Nuez / avellana"
    }),

    "P3": ("3. ¿Acidez?", {
        "A": "Me encanta",
        "B": "Un poco",
        "C": "No me gusta"
    }),

    "P4": ("4. Textura:", {
        "A": "Ligera",
        "B": "Cremosa",
        "C": "Fuerte",
        "D": "Suave"
    }),

    "P5": ("5. ¿Qué buscas?", {
        "A": "Energía",
        "B": "Disfrutar",
        "C": "Balance",
        "D": "Acompañar comida"
    }),

    "P7": ("6. Dulzor:", {
        "A": "Nada",
        "B": "Poco",
        "C": "Mucho",
        "D": "Natural"
    }),

    "P8": ("7. ¿Con leche?", {
        "A": "No",
        "B": "A veces",
        "C": "Sí"
    }),

    "P10": ("8. ¿Cómo prefieres prepararlo?", {
        "A": "Rápido (sin esfuerzo)",
        "B": "Manual (me gusta el proceso)",
        "C": "Como en cafetería",
        "D": "Fácil y sin complicaciones"
    }),

    "P11": ("9. Temperatura:", {
        "A": "Caliente",
        "B": "Frío",
        "C": "Me da igual"
    }),

    "P12": ("10. Sabor extra:", {
        "A": "Natural",
        "B": "Vainilla",
        "C": "Caramelo",
        "D": "Avellana",
        "E": "Chocolate"
    }),
}

conditional_questions = {
    "P9": ("7.1 ¿Qué leche prefieres?", {
        "A": "Entera",
        "B": "Deslactosada",
        "C": "Soya",
        "D": "Avena",
        "E": "Almendra"
    })
}


def select_mode():
    print("☕ ¿Qué quieres hacer?\n")
    print("A) Recomiéndame un café")
    print("B) Crear mi café")

    while True:
        choice = input("Respuesta: ").upper().strip()
        if choice in ["A", "B"]:
            return choice
        print("❌ Opción inválida")


def run_quiz():
    answers = {}

    for key, (question, options) in questions.items():
        print(f"\n{question}")
        for k, v in options.items():
            print(f"{k}) {v}")

        while True:
            choice = input("Respuesta: ").upper().strip()
            if choice in options:
                break
            print("❌ Opción inválida, intenta de nuevo.")

        answers[key] = choice

        if key == "P8":
            if answers["P8"] in ["B", "C"]:
                question_81, options_81 = conditional_questions["P9"]

                print(f"\n{question_81}")
                for k, v in options_81.items():
                    print(f"{k}) {v}")

                while True:
                    milk_choice = input("Respuesta: ").upper().strip()
                    if milk_choice in options_81:
                        break
                    print("❌ Opción inválida, intenta de nuevo.")

                answers["P9"] = milk_choice
            else:
                answers["P9"] = "F"

    return answers


def apply_weight(key, value):
    if key in ["ESP", "V60", "PRS", "MOK", "CLD"]:
        return value * 1.4
    if key in ["SWEET", "ACID", "BODY"]:
        return value * 1.3
    if key in ["CHO", "CAR", "FRU", "NUT"]:
        return value * 1.2
    if key in ["HIGH", "LOW", "BAL"]:
        return value * 0.8
    return value


def normalize_scores(scores):
    if not scores:
        return scores

    max_val = max(scores.values())

    if max_val == 0:
        return scores

    return {k: round(v / max_val * 10, 2) for k, v in scores.items()}


def calculate_scores(answers):
    scores = defaultdict(float)

    for q, a in answers.items():
        key = f"{q}_{a}"

        if key in scoring:
            for trait, value in scoring[key].items():
                scores[trait] += apply_weight(trait, value)

    if answers.get("P8") == "A":
        scores["MILK"] -= 1.5
        scores["BLACK"] += 1.0

    if answers.get("P9") == "F":
        scores["MILK"] -= 2.5
        scores["BLACK"] += 1.5

    if scores["MILK"] < 0:
        scores["MILK"] = 0

    return normalize_scores(dict(scores))


def body_high(scores):
    return scores.get("BODY", 0) >= 6


def prefers_black(scores, answers):
    black = scores.get("BLACK", 0)
    milk = scores.get("MILK", 0)

    if answers.get("P9") == "F":
        return True

    if answers.get("P8") == "A" and black >= milk:
        return True

    return False


def generate_beverage(metodo_key, scores, answers):
    milk = scores.get("MILK", 0)
    choco = scores.get("CHO", 0)
    fruity = scores.get("FRU", 0)
    sweet = scores.get("SWEET", 0)
    caramel = scores.get("CAR", 0)
    intensity = scores.get("HIGH", 0)

    cold = scores.get("COLD", 0)
    hot = scores.get("HOT", 0)

    black_preferred = prefers_black(scores, answers)

    if metodo_key == "V60":
        if cold > hot:
            return "Cold Brew" if fruity >= 6 else "Iced Filtrado"

        if fruity >= 6:
            return "V60 frutal"
        elif choco >= 5 or caramel >= 5:
            return "Filtrado balanceado"
        else:
            return "V60 suave"

    if cold > hot:
        if metodo_key == "ESP":
            if black_preferred or milk < 2:
                bebida = "Iced Americano"
            elif milk < 4:
                bebida = "Iced Cortado"
            elif milk < 7:
                bebida = "Iced Cappuccino"
            else:
                bebida = "Iced Latte"

            if not black_preferred and milk >= 5 and choco >= 6 and sweet >= 6:
                bebida = "Iced Mocha"

            return bebida

        elif metodo_key == "CLD":
            return "Cold Brew" if black_preferred or milk < 5 else "Cold Brew con leche"

        elif metodo_key == "PRS":
            return "Prensa francesa" if black_preferred or milk < 5 else "Prensa francesa con leche"

        elif metodo_key == "MOK":
            return "Moka intensa" if black_preferred or milk < 5 else "Moka con leche"

    if metodo_key == "ESP":
        if black_preferred or milk < 2:
            if intensity >= 6:
                bebida = "Doble espresso"
            elif scores.get("LOW", 0) >= 5:
                bebida = "Americano"
            else:
                bebida = "Espresso"
        elif milk < 4:
            bebida = "Cortado"
        elif milk < 7:
            if body_high(scores) and choco >= 4:
                bebida = "Flat White"
            else:
                bebida = "Cappuccino"
        else:
            if sweet >= 7 or caramel >= 5:
                bebida = "Latte"
            elif body_high(scores) and choco >= 4:
                bebida = "Flat White"
            else:
                bebida = "Cappuccino"

        if not black_preferred and milk >= 5 and choco >= 6 and sweet >= 6:
            bebida = "Mocha"

        return bebida

    elif metodo_key == "PRS":
        return "Prensa francesa" if black_preferred or milk < 5 else "Prensa francesa con leche"

    elif metodo_key == "MOK":
        return "Moka intensa" if black_preferred or milk < 5 else "Moka con leche"

    elif metodo_key == "CLD":
        return "Cold Brew" if black_preferred or milk < 5 else "Cold Brew con leche"

    return "Café"


def build_coffee_profile(metodo_key, bebida, scores, answers):
    choco = scores.get("CHO", 0)
    caramel = scores.get("CAR", 0)
    fruity = scores.get("FRU", 0)

    acidity_val = scores.get("ACID", 0)
    body_val = scores.get("BODY", 0)

    # Si no hay señal clara de sabor, usar balanceado como default
    if max(choco, caramel, fruity) == 0:
        sabor = "balanceado"
    elif choco >= caramel and choco >= fruity:
        sabor = "chocolateado"
    elif caramel >= choco and caramel >= fruity:
        sabor = "caramelo"
    elif fruity >= choco and fruity >= caramel:
        sabor = "frutal"
    else:
        sabor = "balanceado"

    if acidity_val >= 6:
        acidez = "alta"
    elif acidity_val >= 3:
        acidez = "media"
    else:
        acidez = "baja"

    if body_val >= 6:
        cuerpo = "alto"
    elif body_val >= 3:
        cuerpo = "medio"
    else:
        cuerpo = "ligero"

    if metodo_key == "ESP" and bebida in [
        "Latte", "Cappuccino", "Cortado", "Flat White", "Mocha",
        "Iced Latte", "Iced Cappuccino", "Iced Cortado", "Iced Mocha", "Iced Americano"
    ]:
        if sabor == "frutal":
            sabor = "caramelo" if caramel >= choco else "chocolateado"

        if bebida in ["Latte", "Mocha", "Iced Latte", "Iced Mocha"]:
            acidez = "baja"
        elif acidez == "alta":
            acidez = "media"

        if cuerpo == "ligero":
            cuerpo = "medio"

    if metodo_key == "V60":
        if fruity >= 5:
            sabor = "frutal"
        elif choco >= 5 or caramel >= 5:
            sabor = "balanceado"
        else:
            sabor = "ligero"

        if sabor == "frutal":
            acidez = "alta"
        elif acidez == "baja":
            acidez = "media"

        if cuerpo == "alto":
            cuerpo = "medio"
        elif cuerpo not in ["medio", "ligero"]:
            cuerpo = "ligero"

    if metodo_key == "PRS":
        if sabor == "frutal":
            sabor = "chocolateado" if choco >= caramel else "caramelo"

        if acidez == "alta":
            acidez = "media"

        if cuerpo == "ligero":
            cuerpo = "alto"

    if metodo_key == "MOK":
        if sabor == "frutal":
            sabor = "chocolateado"

        if acidez == "alta":
            acidez = "media"

        if cuerpo == "ligero":
            cuerpo = "alto"

    if metodo_key == "CLD":
        if sabor == "frutal":
            acidez = "media"
        elif acidez == "alta":
            acidez = "media"

        if cuerpo == "alto":
            cuerpo = "medio"

    if metodo_key == "V60":
        if sabor == "frutal":
            origen = "Etiopía o Kenia"
        elif sabor == "balanceado":
            origen = "Colombia"
        else:
            origen = "Centroamérica"
    elif metodo_key in ["ESP", "PRS", "MOK"]:
        if sabor == "chocolateado":
            origen = "Brasil"
        elif sabor == "caramelo":
            origen = "Colombia"
        else:
            origen = "Blend latinoamericano"
    elif metodo_key == "CLD":
        if sabor == "frutal":
            origen = "Etiopía o Kenia"
        elif sabor == "caramelo":
            origen = "Colombia"
        else:
            origen = "Blend latinoamericano"
    else:
        origen = "Blend latinoamericano"

    if bebida in [
        "Latte", "Cappuccino", "Cortado", "Flat White", "Mocha",
        "Iced Latte", "Iced Cappuccino", "Iced Cortado", "Iced Mocha",
        "Prensa francesa con leche", "Cold Brew con leche",
        "Moka con leche", "Moka fría con leche"
    ] and origen == "Etiopía o Kenia":
        origen = "Colombia"

    milk_choice = answers.get("P9", "F")
    leche = milk_map.get(milk_choice, "Sin leche")

    if metodo_key == "V60":
        leche = "Sin leche"

    if bebida in [
        "Espresso", "Doble espresso", "Americano", "Iced Americano",
        "V60 frutal", "Filtrado balanceado", "V60 suave", "Iced Filtrado",
        "Prensa francesa", "Moka intensa", "Cold Brew"
    ]:
        leche = "Sin leche"

    if bebida in [
        "Cold Brew", "Cold Brew con leche", "Iced Latte", "Iced Cappuccino",
        "Iced Cortado", "Iced Mocha", "Iced Americano", "Iced Filtrado",
        "Moka fría con leche", "Café frío estilo moka"
    ]:
        tostado = "medio"
    elif metodo_key == "V60":
        tostado = "claro" if sabor == "frutal" else "medio"
    elif metodo_key in ["ESP", "MOK", "PRS"]:
        tostado = "oscuro" if sabor == "chocolateado" else "medio"
    else:
        tostado = "medio"

    flavor_choice = answers.get("P12", "A")
    flavor_text = flavor_add_map.get(flavor_choice, "Natural")

    recomendacion = ""

    if flavor_choice != "A":
        if metodo_key == "V60" and bebida in ["V60 frutal", "V60 suave"]:
            recomendacion = f"Recomendación: añadir un toque de {flavor_text.lower()} en la taza o jarra receptora para mantener claridad."

        elif bebida in ["Filtrado balanceado", "Iced Filtrado"]:
            recomendacion = f"Recomendación: el toque de {flavor_text.lower()} sea infusionado durante la preparación."

        elif metodo_key == "PRS":
            recomendacion = f"Recomendación: añadir un toque de {flavor_text.lower()} al final o infusionarlo ligeramente para respetar el cuerpo de la prensa francesa."

    return {
        "origen": origen,
        "sabor": sabor,
        "acidez": acidez,
        "cuerpo": cuerpo,
        "leche": leche,
        "tostado": tostado,
        "recomendacion": recomendacion
    }


def enrich_beverage_name(bebida, scores, perfil, answers):
    sweet = scores.get("SWEET", 0)
    choco = scores.get("CHO", 0)
    caramel = scores.get("CAR", 0)
    nutty = scores.get("NUT", 0)
    fruity = scores.get("FRU", 0)

    added = answers.get("P12", "A")

    flavor_allowed = {
        "Latte", "Iced Latte",
        "Cappuccino", "Iced Cappuccino",
        "Flat White",
        "Cortado", "Iced Cortado",
        "Mocha", "Iced Mocha",
        "Moka con leche", "Moka fría con leche",
        "Cold Brew con leche",
        "Prensa francesa con leche",
        "Prensa francesa",
        "Cold Brew",
        "Americano",
        "Iced Americano",
        "Espresso",
        "Moka intensa"
    }

    def apply_added_flavor(base_name):
        if base_name not in flavor_allowed:
            return base_name

        if added == "B":
            return f"{base_name} de vainilla"
        if added == "C":
            return f"{base_name} de caramelo"
        if added == "D":
            return f"{base_name} avellanado"
        if added == "E":
            if base_name in ["Latte", "Cappuccino", "Flat White", "Cortado"]:
                return "Mocha"
            if base_name in ["Iced Latte", "Iced Cappuccino", "Iced Cortado"]:
                return "Iced Mocha"
            return f"{base_name} chocolateado"

        return base_name

    if bebida == "Latte":
        if added != "A":
            return apply_added_flavor("Latte")
        if choco >= 5:
            return "Latte cremoso"
        elif caramel >= 5:
            return "Latte balanceado"
        elif nutty >= 5:
            return "Latte tostado"
        elif sweet >= 5:
            return "Latte suave"
        return "Latte clásico"

    if bebida == "Iced Latte":
        if added != "A":
            return apply_added_flavor("Iced Latte")
        if choco >= 5:
            return "Iced Latte cremoso"
        elif caramel >= 5:
            return "Iced Latte balanceado"
        elif nutty >= 5:
            return "Iced Latte tostado"
        return "Iced Latte"

    if bebida == "Cappuccino":
        if added != "A":
            return apply_added_flavor("Cappuccino")
        if choco >= 5:
            return "Cappuccino intenso"
        elif caramel >= 5:
            return "Cappuccino suave"
        elif nutty >= 5:
            return "Cappuccino tostado"
        return "Cappuccino clásico"

    if bebida == "Iced Cappuccino":
        if added != "A":
            return apply_added_flavor("Iced Cappuccino")
        if choco >= 5:
            return "Iced Cappuccino intenso"
        elif caramel >= 5:
            return "Iced Cappuccino suave"
        elif nutty >= 5:
            return "Iced Cappuccino tostado"
        return "Iced Cappuccino"

    if bebida == "Flat White":
        if added != "A":
            return apply_added_flavor("Flat White")
        if choco >= 5:
            return "Flat White intenso"
        elif caramel >= 5:
            return "Flat White balanceado"
        elif nutty >= 5:
            return "Flat White tostado"
        return "Flat White clásico"

    if bebida == "Cortado":
        if added != "A":
            return apply_added_flavor("Cortado")
        if choco >= 5:
            return "Cortado intenso"
        elif caramel >= 5:
            return "Cortado balanceado"
        return "Cortado clásico"

    if bebida == "Iced Cortado":
        if added != "A":
            return apply_added_flavor("Iced Cortado")
        if choco >= 5:
            return "Iced Cortado intenso"
        elif caramel >= 5:
            return "Iced Cortado balanceado"
        return "Iced Cortado"

    if bebida == "Mocha":
        if added == "C":
            return "Mocha de caramelo"
        return "Mocha"

    if bebida == "Iced Mocha":
        if added == "C":
            return "Iced Mocha de caramelo"
        return "Iced Mocha"

    if bebida == "Espresso":
        if added != "A":
            return apply_added_flavor("Espresso")
        if choco >= 5:
            return "Espresso intenso"
        elif fruity >= 5:
            return "Espresso brillante"
        elif caramel >= 5:
            return "Espresso balanceado"
        return "Espresso clásico"

    if bebida == "Doble espresso":
        return "Doble espresso"

    if bebida == "Americano":
        if added != "A":
            return apply_added_flavor("Americano")
        if caramel >= 5:
            return "Americano balanceado"
        elif fruity >= 5:
            return "Americano brillante"
        return "Americano clásico"

    if bebida == "Iced Americano":
        if added != "A":
            return apply_added_flavor("Iced Americano")
        if caramel >= 5:
            return "Iced Americano balanceado"
        elif fruity >= 5:
            return "Iced Americano brillante"
        return "Iced Americano"

    if bebida == "V60 frutal":
        return "V60 frutal"

    if bebida == "Filtrado balanceado":
        return "Filtrado balanceado"

    if bebida == "V60 suave":
        return "V60 suave"

    if bebida == "Iced Filtrado":
        return "Iced Filtrado"

    if bebida == "Prensa francesa":
        if added != "A":
            return apply_added_flavor("Prensa francesa")
        if choco >= 5:
            return "Prensa francesa intensa"
        elif caramel >= 5:
            return "Prensa francesa balanceada"
        elif nutty >= 5:
            return "Prensa francesa tostada"
        return "Prensa francesa clásica"

    if bebida == "Prensa francesa con leche":
        if added != "A":
            return apply_added_flavor("Prensa francesa con leche")
        if choco >= 5:
            return "Prensa francesa con leche intensa"
        elif caramel >= 5:
            return "Prensa francesa con leche suave"
        return "Prensa francesa con leche"
    
    if bebida == "Moka intensa" and answers.get("P11") == "B":
        if added == "E":
            return "Moka fría chocolateada"
        return "Moka fría intensa"

    if bebida == "Moka intensa":
        if added != "A":
            return apply_added_flavor("Moka intensa")
        if choco >= 5:
            return "Moka intensa"
        elif caramel >= 5:
            return "Moka balanceada"
        return "Moka clásica"

    if bebida == "Moka con leche":
        if added != "A":
            return apply_added_flavor("Moka con leche")
        if caramel >= 5:
            return "Moka con leche suave"
        elif choco >= 5:
            return "Moka con leche intensa"
        return "Moka con leche"

    if bebida == "Cold Brew":
        if added != "A":
            return apply_added_flavor("Cold Brew")
        if caramel >= 5:
            return "Cold Brew suave"
        elif fruity >= 5:
            return "Cold Brew brillante"
        return "Cold Brew"

    if bebida == "Cold Brew con leche":
        if added != "A":
            return apply_added_flavor("Cold Brew con leche")
        if caramel >= 5:
            return "Cold Brew con leche suave"
        return "Cold Brew con leche"

    return bebida


def get_temperature(scores, answers, bebida):
    cold = scores.get("COLD", 0)
    hot = scores.get("HOT", 0)

    if answers.get("P11") == "B":
        return "iced"

    if answers.get("P11") == "A":
        return "hot"

    return "iced" if cold > hot else "hot"


def suggest_related_option(scores, answers, existing_beverages):
    milk = scores.get("MILK", 0)
    sweet = scores.get("SWEET", 0)
    caramel = scores.get("CAR", 0)
    choco = scores.get("CHO", 0)
    fruity = scores.get("FRU", 0)

    candidates = []

    if milk >= 7:
        candidates = [
            ("Latte", "ESP"),
            ("Cappuccino", "ESP"),
            ("Flat White", "ESP"),
            ("Prensa francesa con leche", "PRS"),
            ("Moka con leche", "MOK"),
            ("Cold Brew con leche", "CLD")
        ]

        if choco >= 5 or sweet >= 7:
            candidates.insert(0, ("Mocha", "ESP"))

    elif milk >= 4:
        candidates = [
            ("Cappuccino", "ESP"),
            ("Flat White", "ESP"),
            ("Cortado", "ESP"),
            ("Prensa francesa con leche", "PRS")
        ]

    else:
        if fruity >= 5:
            candidates = [
                ("V60 frutal", "V60"),
                ("Cold Brew", "CLD"),
                ("Iced Filtrado", "V60")
            ]
        else:
            candidates = [
                ("Americano", "ESP"),
                ("Espresso", "ESP"),
                ("Prensa francesa", "PRS"),
                ("Moka intensa", "MOK")
            ]

    for bebida_base, metodo in candidates:
        perfil = build_coffee_profile(metodo, bebida_base, scores, answers)
        bebida_final = enrich_beverage_name(bebida_base, scores, perfil, answers)

        if bebida_final not in existing_beverages:
            temperatura = get_temperature(scores, answers, bebida_final)

            return {
                "metodo": metodo,
                "bebida": bebida_final,
                "score": "Sugerencia",
                "perfil": perfil,
                "temperatura": temperatura
            }

    return None

def calculate_recommendation_score(r, scores):
    metodo = r["metodo"]
    perfil = r["perfil"]
    bebida = r["bebida"]

    score = 0

    score += scores.get(metodo, 0) * 2.0

    if perfil["leche"] != "Sin leche":
        score += scores.get("MILK", 0) * 1.5
    else:
        score += scores.get("BLACK", 0) * 1.5

    score += scores.get("BODY", 0) * 1.2
    score += scores.get("SWEET", 0) * 1.1

    sabor = perfil["sabor"]

    if sabor == "chocolateado":
        score += scores.get("CHO", 0) * 1.3
    elif sabor == "caramelo":
        score += scores.get("CAR", 0) * 1.3
    elif sabor == "frutal":
        score += scores.get("FRU", 0) * 1.3
    elif sabor == "balanceado":
        score += scores.get("BAL", 0) * 1.1

    if r["temperatura"] == "iced":
        score += scores.get("COLD", 0)
    else:
        score += scores.get("HOT", 0)

    milk = scores.get("MILK", 0)

    if milk >= 7:
        if metodo == "ESP":
            score += 3.0
        elif metodo == "PRS":
            score -= 1.5
        elif metodo == "MOK":
            score -= 0.5
        elif metodo == "CLD":
            score -= 1.0

    if "Latte" in bebida:
        score += 2.0
    elif "Cappuccino" in bebida:
        score += 1.5
    elif "Flat White" in bebida:
        score += 1.3
    elif "Prensa francesa con leche" in bebida:
        score -= 1.0
    elif "Moka con leche" in bebida:
        score += 0.5
    elif "Cold Brew con leche" in bebida:
        score -= 0.5
    
    cold = scores.get("COLD", 0)
    hot = scores.get("HOT", 0)

    if cold > hot:
        if metodo == "CLD":
            score += 3.0
        elif metodo == "ESP":
            score += 1.5
        elif metodo == "V60":
            score += 1.0
        elif metodo in ["MOK", "PRS"]:
            score -= 1.5

    if hot > cold:
        if metodo in ["ESP", "MOK", "PRS", "V60"]:
            score += 1.0
        elif metodo == "CLD":
            score -= 1.0
    
    return round(score, 2)


def get_top_recommendations(scores, answers):
    methods = ["ESP", "V60", "PRS", "MOK", "CLD"]

    candidates = []
    milk_level = scores.get("MILK", 0)

    for m in methods:
        raw_score = scores.get(m, 0)

        if raw_score <= 0:
            continue

        bebida_base = generate_beverage(m, scores, answers)
        perfil = build_coffee_profile(m, bebida_base, scores, answers)

        if milk_level >= 7 and perfil["leche"] == "Sin leche":
            continue

        bebida = enrich_beverage_name(bebida_base, scores, perfil, answers)
        temperatura = get_temperature(scores, answers, bebida)

        candidate = {
            "metodo": m,
            "bebida": bebida,
            "score": 0,
            "perfil": perfil,
            "temperatura": temperatura
        }

        candidate["score_final"] = calculate_recommendation_score(candidate, scores)
        candidates.append(candidate)

    candidates = sorted(candidates, key=lambda x: x["score_final"], reverse=True)

    unique_results = []
    used_names = set()

    for r in candidates:
        if r["bebida"] not in used_names:
            unique_results.append(r)
            used_names.add(r["bebida"])

        if len(unique_results) == 3:
            break

    if len(unique_results) < 3:
        existing_beverages = [r["bebida"] for r in unique_results]
        suggestion = suggest_related_option(scores, answers, existing_beverages)

        if suggestion is not None:
            suggestion["score_final"] = calculate_recommendation_score(suggestion, scores)
            unique_results.append(suggestion)

    scored_results = [r for r in unique_results if isinstance(r.get("score_final"), (int, float)) and r["score_final"] > 0]

    if scored_results:
        max_score = max(r["score_final"] for r in scored_results)

        for r in unique_results:
            if r.get("score_final", 0) > 0:
                r["score"] = round((r["score_final"] / max_score) * 100, 1)
            else:
                r["score"] = "Sugerencia"

    unique_results = sorted(
        unique_results,
        key=lambda x: x["score"] if isinstance(x["score"], (int, float)) else 0,
        reverse=True
    )

    return unique_results

def build_custom_coffee():
    print("\n🔧 Crear tu café\n")

    metodo_map = {
        "A": "ESP",
        "B": "V60",
        "C": "CLD",
        "D": "MOK",
        "E": "PRS"
    }

    print("1. Base:")
    print("A) Espresso")
    print("B) Filtrado / V60")
    print("C) Cold Brew")
    print("D) Moka")
    print("E) Prensa francesa")

    while True:
        metodo = input("Respuesta: ").upper().strip()
        if metodo in metodo_map:
            break
        print("❌ Opción inválida")

    metodo_key = metodo_map[metodo]

    print("\n2. Intensidad:")
    print("A) Suave")
    print("B) Media")
    print("C) Fuerte")

    while True:
        intensidad = input("Respuesta: ").upper().strip()
        if intensidad in ["A", "B", "C"]:
            break
        print("❌ Opción inválida")

    print("\n3. Temperatura:")
    print("A) Caliente")
    print("B) Frío")

    while True:
        temp = input("Respuesta: ").upper().strip()
        if temp in ["A", "B"]:
            break
        print("❌ Opción inválida")

    temperatura = "iced" if temp == "B" else "hot"

    print("\n4. Dulzor:")
    print("A) Nada")
    print("B) Poco")
    print("C) Medio")
    print("D) Mucho")

    while True:
        dulzor = input("Respuesta: ").upper().strip()
        if dulzor in ["A", "B", "C", "D"]:
            break
        print("❌ Opción inválida")

    milk_choice = "F"
    usa_leche = "A"

    if metodo_key != "V60":
        print("\n5. ¿Leche?")
        print("A) No")
        print("B) Sí")

        while True:
            usa_leche = input("Respuesta: ").upper().strip()
            if usa_leche in ["A", "B"]:
                break
            print("❌ Opción inválida")

        if usa_leche == "B":
            print("\n5.1 Tipo de leche:")
            for k, v in milk_map.items():
                if k != "F":
                    print(f"{k}) {v}")

            while True:
                milk_choice = input("Respuesta: ").upper().strip()
                if milk_choice in ["A", "B", "C", "D", "E"]:
                    break
                print("❌ Opción inválida")
    else:
        print("\nℹ️ V60 / filtrado se prepara sin leche para mantener claridad.")

    sabor = "A"

    if dulzor != "A":
        print("\n6. Sabor extra:")
        print("A) Natural")
        print("B) Vainilla")
        print("C) Caramelo")
        print("D) Avellana")
        print("E) Chocolate")

        while True:
            sabor = input("Respuesta: ").upper().strip()
            if sabor in flavor_add_map:
                break
            print("❌ Opción inválida")
    else:
        print("\nℹ️ Sin sabor extra para mantener el café natural.")

    answers = {
        "P7": dulzor,
        "P8": "C" if usa_leche == "B" else "A",
        "P9": milk_choice,
        "P11": "B" if temperatura == "iced" else "A",
        "P12": sabor
    }

    scores = defaultdict(float)

    scores[metodo_key] = 10

    # Intensidad
    if intensidad == "A":
        scores["LOW"] += 8
        scores["BODY"] -= 1

    elif intensidad == "B":
        scores["BAL"] += 8

    elif intensidad == "C":
        scores["HIGH"] += 8
        scores["BODY"] += 2

    # Dulzor
    if dulzor == "A":
        scores["SWEET"] = 0
        scores["BLACK"] += 2

    elif dulzor == "B":
        scores["SWEET"] = 3

    elif dulzor == "C":
        scores["SWEET"] = 6

    elif dulzor == "D":
        scores["SWEET"] = 9
        scores["MILK"] += 1

    # Leche
    if usa_leche == "B":
        scores["MILK"] += 8
    else:
        scores["BLACK"] += 8

    # Sabor añadido
    if sabor == "B":
        scores["SWEET"] += 2
        scores["CAR"] += 1

    elif sabor == "C":
        scores["CAR"] += 6
        scores["SWEET"] += 2

    elif sabor == "D":
        scores["NUT"] += 6

    elif sabor == "E":
        scores["CHO"] += 6
        scores["SWEET"] += 2

    # Temperatura
    if temperatura == "iced":
        scores["COLD"] = 10
        scores["HOT"] = 0
    else:
        scores["HOT"] = 10
        scores["COLD"] = 0

    bebida_base = generate_beverage(metodo_key, scores, answers)
    perfil = build_coffee_profile(metodo_key, bebida_base, scores, answers)
    bebida = enrich_beverage_name(bebida_base, scores, perfil, answers)

    print("\n--- TU CAFÉ ---\n")
    print(f"{bebida} ({'Frío' if temperatura == 'iced' else 'Caliente'})")
    print(f"Método: {method_names[metodo_key]}")
    print(f"Origen: {perfil['origen']}")
    print(f"Perfil: {perfil['sabor']} | Acidez {perfil['acidez']} | Cuerpo {perfil['cuerpo']}")
    print(f"Tostado: {perfil['tostado']}")
    print(f"Leche: {perfil['leche']}")

    if sabor == "A":
        print("Sabor añadido: Ninguno")
    else:
        print(f"Sabor añadido: {flavor_add_map[sabor]}")

    if perfil.get("recomendacion"):
        print(f"💡 {perfil['recomendacion'].strip()}")


def show_recommendations():
    print("\n☕ Coffee Quiz\n")

    answers = run_quiz()
    scores = calculate_scores(answers)

    print("\n--- SCORES ---")
    for k, v in sorted(scores.items(), key=lambda x: -x[1]):
        print(f"{k}: {v}")

    print("\n--- RESULTADOS ---\n")
    top = get_top_recommendations(scores, answers)

    for i, r in enumerate(top, 1):
        temp_label = "Frío" if r["temperatura"] == "iced" else "Caliente"
        score_label = f"{r['score']}%" if isinstance(r["score"], (int, float)) else r["score"]

        print(f"{i}. {r['bebida']} ({temp_label}) ({score_label})")

        p = r["perfil"]

        print(f"   Método: {method_names[r['metodo']]}")
        print(f"   Origen: {p['origen']}")
        print(f"   Perfil: {p['sabor']} | Acidez {p['acidez']} | Cuerpo {p['cuerpo']}")
        print(f"   Tostado: {p['tostado']}")
        print(f"   Leche: {p['leche']}")

        if answers["P12"] == "A":
            print("   Sabor añadido: Ninguno")
        else:
            print(f"   Sabor añadido: {flavor_add_map[answers['P12']]}")

        if i == 1:
            print("   ✅ Mejor match contigo")
        elif i == 2:
            print("   🔄 Alternativa cercana a lo que tdentifica")
        elif i == 3:
            print("   🎯 Opción para explorar algo diferente")

        if p.get("recomendacion"):
            print(f"   💡 {p['recomendacion'].strip()}")

        print()

def main():
    mode = select_mode()

    if mode == "A":
        show_recommendations()
    else:
        build_custom_coffee()


if __name__ == "__main__":
    main()