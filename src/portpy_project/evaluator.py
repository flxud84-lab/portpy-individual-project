import portpy.photon as pp


def evaluate_plan(
    plan,
    sol,
    clinical_criteria,
):
    """
    Evalua el plan optimizado.
    """

    print("Evaluando plan...")

    pp.Evaluation.display_clinical_criteria(
        my_plan=plan,
        sol=sol,
        clinical_criteria=clinical_criteria,
    )

    print("Evaluacion completada.")