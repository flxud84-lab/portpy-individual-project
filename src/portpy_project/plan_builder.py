import portpy.photon as pp


def build_plan_components(
    data,
    ct,
    structs,
    beams,
    protocol_name: str,
):
    print("Cargando clinical criteria...")
    clinical_criteria = pp.ClinicalCriteria(
        data,
        protocol_name=protocol_name,
    )

    print("Cargando parametros de optimizacion...")
    opt_params = data.load_config_opt_params(
        protocol_name=protocol_name,
    )

    print("Cargando influence matrix...")
    inf_matrix = pp.InfluenceMatrix(
        ct=ct,
        structs=structs,
        beams=beams,
    )

    print("Creando plan...")
    plan = pp.Plan(
        ct=ct,
        structs=structs,
        beams=beams,
        inf_matrix=inf_matrix,
        clinical_criteria=clinical_criteria,
    )

    return clinical_criteria, opt_params, inf_matrix, plan