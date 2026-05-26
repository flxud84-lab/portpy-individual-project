from portpy_project.config import load_config

from portpy_project.data_loader import (
    get_data_explorer,
    load_patient_components,
)

from portpy_project.download_data import (
    download_patient_data,
)

from portpy_project.plan_builder import (
    build_plan_components,
)

from portpy_project.optimizer import (
    run_imrt_optimization,
)

from portpy_project.output_manager import (
    save_solution,
)

from portpy_project.evaluator import (
    evaluate_plan,
)

import matplotlib.pyplot as plt
import portpy.photon as pp
import random
import os


# =========================================================
# GUIAS PEDAGOGICAS
# =========================================================

def show_metric_guide(metric):

    print("\n====================================")

    # =====================================================
    # PTV
    # =====================================================

    if metric == "D98_PTV":

        print("GUIA DVH - D98% PTV")
        print("====================================")

        print("""
D98% = dosis minima recibida
por el 98% del PTV.

COMO ENCONTRARLO:

1. Observe la curva PTV
2. Mire el eje Y
3. Busque 98%
4. Intersecte curva PTV
5. Baje al eje X
6. Lea la dosis

INTERPRETACION:

- Alto D98:
  mejor cobertura

- Bajo D98:
  riesgo de subdosificacion
""")

    elif metric == "D50_PTV":

        print("GUIA DVH - D50% PTV")
        print("====================================")

        print("""
D50% = dosis mediana del PTV.

COMO ENCONTRARLO:

1. Busque 50% eje Y
2. Intersecte curva PTV
3. Lea dosis eje X

INTERPRETACION:

- Evalua comportamiento medio
- Evalua distribucion central
""")

    elif metric == "D2_PTV":

        print("GUIA DVH - D2% PTV")
        print("====================================")

        print("""
D2% = dosis maxima aproximada
recibida por el 2% del PTV.

COMO ENCONTRARLO:

1. Observe eje Y
2. Busque 2%
3. Esta cerca parte inferior
4. Toque curva PTV
5. Lea dosis eje X

INTERPRETACION:

- Alto D2:
  hot spots

- Bajo D2:
  mejor homogeneidad
""")

    # =====================================================
    # OARs
    # =====================================================

    elif metric == "V20_PULMON":

        print("GUIA DVH - V20 PULMON")
        print("====================================")

        print("""
V20 Pulmon:

Porcentaje pulmonar que
recibe 20 Gy o mas.

COMO ENCONTRARLO:

1. Busque 20 Gy eje X
2. Suba a curva pulmon
3. Lea porcentaje eje Y

INTERPRETACION:

- Alto V20:
  mayor toxicidad pulmonar

- Bajo V20:
  mejor proteccion
""")

    elif metric == "V5_PULMON":

        print("GUIA DVH - V5 PULMON")
        print("====================================")

        print("""
V5 Pulmon:

Volumen pulmonar que
recibe 5 Gy o mas.

INTERPRETACION:

- Alto V5:
  irradiacion extensa

- Bajo V5:
  mejor proteccion
""")

    elif metric == "Dmean_CORAZON":

        print("GUIA DVH - Dmean CORAZON")
        print("====================================")

        print("""
Dmean Corazon:

Dosis promedio cardiaca.

INTERPRETACION:

- Alto Dmean:
  mayor riesgo cardiaco

- Bajo Dmean:
  mejor proteccion
""")

    elif metric == "Dmax_MEDULA":

        print("GUIA DVH - Dmax MEDULA")
        print("====================================")

        print("""
Dmax Medula:

Dosis maxima medular.

INTERPRETACION:

- Alto Dmax:
  riesgo neurologico

- Bajo Dmax:
  mejor seguridad
""")


# =========================================================
# VALIDACION TEXTO
# =========================================================

def validate_text_answer(answer, keywords):

    return any(
        k.lower() in answer.lower()
        for k in keywords
    )


# =========================================================
# GENERAR 100 PREGUNTAS
# =========================================================

def generate_questions():

    templates = [

        ("¿La cobertura PTV parece adecuada?", ["si"]),
        ("¿Existe hot spot importante?", ["no"]),
        ("¿La homogeneidad parece correcta?", ["si"]),
        ("¿El pulmon parece protegido?", ["si"]),
        ("¿El corazon parece protegido?", ["si"]),
        ("¿Existe sobre dosificacion evidente?", ["no"]),
        ("¿La conformidad parece adecuada?", ["si"]),
        ("¿La medula parece protegida?", ["si"]),
        ("¿La curva PTV domina el DVH?", ["si"]),
        ("¿El plan parece aceptable?", ["si"])

    ]

    questions = []

    for i in range(10):

        for q, k in templates:

            questions.append({

                "question":
                f"{q} [Variante {i+1}]",

                "keywords":
                k
            })

    random.shuffle(questions)

    return questions


# =========================================================
# ANALISIS PEDAGOGICO
# =========================================================

def run_pedagogical_analysis():

    print("\n====================================")
    print("ANALISIS PEDAGOGICO")
    print("====================================")

    questions = generate_questions()

    selected = random.sample(
        questions,
        10
    )

    used = set()

    counter = 1

    for q in selected:

        if q["question"] in used:
            continue

        answered = False

        while not answered:

            ans = input(
                f"\n{counter}. {q['question']}: "
            )

            if validate_text_answer(
                ans,
                q["keywords"]
            ):

                print(
                    "\n[RESPUESTA ACEPTADA]"
                )

                used.add(q["question"])

                answered = True

            else:

                print(
                    "\n[RETROALIMENTACION]"
                )

                print(
                    "Revise nuevamente:"
                )

                print("- Curva DVH")
                print("- Cobertura")
                print("- OARs")
                print("- Homogeneidad")

        counter += 1


# =========================================================
# REGISTRO CASO 1
# =========================================================

def validate_case1_metrics():

    print("\n====================================")
    print("REGISTRO METRICAS CASO 1")
    print("====================================")

    metric_names = [

        "D98_PTV",
        "D50_PTV",
        "D2_PTV",

        "V20_PULMON",
        "V5_PULMON",

        "Dmean_CORAZON",

        "Dmax_MEDULA"

    ]

    metrics = {}

    for metric in metric_names:

        show_metric_guide(metric)

        valid = False

        while not valid:

            try:

                value = float(
                    input(
                        f"\nIngrese valor REAL {metric}: "
                    )
                )

                confirm = input(
                    f"\n¿Confirma {metric} = {value}? (si/no): "
                ).lower()

                if confirm == "si":

                    metrics[metric] = value

                    print(
                        "\n[VALOR REGISTRADO]"
                    )

                    valid = True

            except:

                print(
                    "\nIngrese numero valido."
                )

    return metrics


# =========================================================
# REGISTRO CASO 2
# =========================================================

def validate_case2_metrics():

    print("\n====================================")
    print("REGISTRO METRICAS CASO 2")
    print("====================================")

    metric_names = [

        "D98_PTV",
        "D50_PTV",
        "D2_PTV",

        "V20_PULMON",
        "V5_PULMON",

        "Dmean_CORAZON",

        "Dmax_MEDULA"

    ]

    metrics = {}

    for metric in metric_names:

        knows = input(
            f"\n¿Sabe encontrar {metric}? (si/no): "
        ).lower()

        if knows == "no":

            show_metric_guide(metric)

        valid = False

        while not valid:

            try:

                value = float(
                    input(
                        f"\nIngrese valor REAL {metric}: "
                    )
                )

                metrics[metric] = value

                valid = True

            except:

                print(
                    "\nIngrese numero valido."
                )

    return metrics


# =========================================================
# COMPARACION CLINICA
# =========================================================

def clinical_comparison(case1, case2):

    print("\n====================================")
    print("COMPARACION CLINICA")
    print("====================================")

    comparisons = [

        {
            "metric": "D98_PTV",
            "question":
            "¿Que plan tuvo mejor cobertura tumoral?",
            "better": "higher"
        },

        {
            "metric": "D2_PTV",
            "question":
            "¿Que plan tuvo menor hot spot?",
            "better": "lower"
        },

        {
            "metric": "V20_PULMON",
            "question":
            "¿Que plan protegio mejor pulmon?",
            "better": "lower"
        },

        {
            "metric": "Dmean_CORAZON",
            "question":
            "¿Que plan protegio mejor corazon?",
            "better": "lower"
        },

        {
            "metric": "Dmax_MEDULA",
            "question":
            "¿Que plan protegio mejor medula?",
            "better": "lower"
        }

    ]

    for c in comparisons:

        metric = c["metric"]

        v1 = case1[metric]
        v2 = case2[metric]

        if c["better"] == "higher":

            correct = "1" if v1 > v2 else "2"

        else:

            correct = "1" if v1 < v2 else "2"

        answered = False

        while not answered:

            response = input(
                f"\n{c['question']}: "
            )

            if correct in response:

                print(
                    "\n[RESPUESTA CORRECTA]"
                )

                print(
                    f"\nCaso 1 {metric}: {v1}"
                )

                print(
                    f"Caso 2 {metric}: {v2}"
                )

                explanation = input(
                    "\nExplique clinicamente: "
                )

                while len(
                    explanation.strip()
                ) < 15:

                    print(
                        "\nExplicacion insuficiente."
                    )

                    explanation = input(
                        "\nExplique nuevamente: "
                    )

                print(
                    "\n[ANALISIS ACEPTADO]"
                )

                answered = True

            else:

                print(
                    "\n[RETROALIMENTACION]"
                )

                print(
                    "La respuesta no coincide "
                    "con las metricas."
                )

                print(
                    f"\nCaso 1 {metric}: {v1}"
                )

                print(
                    f"Caso 2 {metric}: {v2}"
                )


# =========================================================
# MAIN
# =========================================================

def main():

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    config = load_config()

    print("====================================")
    print("PORTPY - TUTOR CLINICO IMRT")
    print("====================================")

    # =====================================================
    # DESCARGA DATOS
    # =====================================================

    if config["download_data"]:

        download_patient_data(
            repo_id=config["repo_id"],
            patient_id=config["patient_id"],
            data_dir=config["data_dir"],
        )

    # =====================================================
    # CARGAR PACIENTE
    # =====================================================

    data = get_data_explorer(
        data_dir=config["data_dir"],
        patient_id=config["patient_id"],
    )

    ct, structs, beams = (
        load_patient_components(data)
    )

    # =====================================================
    # CREAR PLAN
    # =====================================================

    (
        clinical_criteria,
        opt_params,
        inf_matrix,
        plan,
    ) = build_plan_components(
        data=data,
        ct=ct,
        structs=structs,
        beams=beams,
        protocol_name=config["protocol_name"],
    )

    print("\nPlan creado correctamente.")

    # =====================================================
    # OPTIMIZACION
    # =====================================================

    if config["run_optimization"]:

        opt, sol = run_imrt_optimization(
            plan=plan,
            clinical_criteria=clinical_criteria,
            opt_params=opt_params,
            solver=config["solver"],
        )

    print("\nOptimizacion completada.")

    # =====================================================
    # GUARDAR
    # =====================================================

    if config["save_outputs"]:

        save_solution(
            sol=sol,
            output_dir="outputs",
            patient_id=config["patient_id"],
        )

    # =====================================================
    # EVALUACION
    # =====================================================

    print("\n====================================")
    print("EVALUACION DOSIMETRICA")
    print("====================================")

    evaluate_plan(
        plan=plan,
        sol=sol,
        clinical_criteria=clinical_criteria,
    )

    # =====================================================
    # DVH
    # =====================================================

    print("\n====================================")
    print("VISUALIZACION DVH")
    print("====================================")

    plt.ion()

    pp.Visualization.plot_dvh(
        my_plan=plan,
        sol=sol,
        clinical_criteria=clinical_criteria
    )

    plt.title(
        f"DVH - {config['patient_id']}"
    )

    plt.show(block=False)

    plt.pause(1)

    print("\nDVH abierto correctamente.")

    # =====================================================
    # CASO 1
    # =====================================================

    case1_metrics = validate_case1_metrics()

    # =====================================================
    # PREGUNTAS
    # =====================================================

    run_pedagogical_analysis()

    # =====================================================
    # SEGUNDO CASO
    # =====================================================

    print("\n====================================")
    print("SEGUNDO CASO")
    print("====================================")

    print("""
Abra segunda terminal.

Ejecute segundo paciente.

Luego vuelva aqui.
""")

    input(
        "\nEscriba CONTINUAR: "
    )

    # =====================================================
    # CASO 2
    # =====================================================

    case2_metrics = validate_case2_metrics()

    # =====================================================
    # COMPARACION
    # =====================================================

    clinical_comparison(
        case1_metrics,
        case2_metrics
    )

    # =====================================================
    # REFLEXION
    # =====================================================

    print("\n====================================")
    print("REFLEXION FINAL")
    print("====================================")

    reflection = input(
        "\n¿Que plan considera mejor y por que?: "
    )

    while len(
        reflection.strip()
    ) < 25:

        print(
            "\nLa reflexion es muy corta."
        )

        reflection = input(
            "\nExplique nuevamente: "
        )

    print("\n====================================")
    print("ANALISIS FINALIZADO")
    print("====================================")


if __name__ == "__main__":

    main()