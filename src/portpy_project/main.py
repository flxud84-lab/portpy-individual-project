from portpy_project.config import load_config
from portpy_project.data_loader import (
    get_data_explorer,
    load_patient_components,
)
from portpy_project.download_data import download_patient_data
from portpy_project.plan_builder import (
    build_plan_components,
)


def main() -> None:
    config = load_config()

    print("Proyecto PortPy iniciado correctamente.")

    if config["download_data"]:
        download_patient_data(
            repo_id=config["repo_id"],
            patient_id=config["patient_id"],
            data_dir=config["data_dir"],
        )

    data = get_data_explorer(
        data_dir=config["data_dir"],
        patient_id=config["patient_id"],
    )

    ct, structs, beams = load_patient_components(data)

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

    print("Plan creado correctamente.")
    print(plan)


if __name__ == "__main__":
    main()