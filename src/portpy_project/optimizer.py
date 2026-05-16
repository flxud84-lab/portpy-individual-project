import portpy.photon as pp


def run_imrt_optimization(
    plan,
    clinical_criteria,
    opt_params,
    solver: str = "SCS",
):
    """
    Ejecuta optimización IMRT.
    """

    print("Inicializando optimizador...")

    opt = pp.Optimization(
        plan,
        opt_params=opt_params,
        clinical_criteria=clinical_criteria,
    )

    print("Creando problema CVXPY...")
    opt.create_cvxpy_problem()

    print("Ejecutando optimizacion...")

    sol = opt.solve(
        solver=solver,
        verbose=False,
    )

    print("Optimizacion completada.")

    return opt, sol