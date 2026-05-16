from pathlib import Path

import portpy.photon as pp


# def get_data_explorer(data_dir: str):
def get_data_explorer(data_dir: str, patient_id: str):
    """
    Inicializa el explorador de datos de PortPy.
    """

    data_path = Path(data_dir)

    data_path.mkdir(parents=True, exist_ok=True)

    data = pp.DataExplorer(data_dir=str(data_path))
    data.patient_id = patient_id

    return data


# def load_patient(data, patient_id: str):
#     """
#     Carga un paciente desde PortPy.
#     """

#     print(f"Cargando paciente: {patient_id}")

#     patient = data.load_patient(patient_id=patient_id)

#     return patient

def load_patient_components(data):
    """
    Carga los componentes principales del paciente.
    """

    print("Cargando CT...")
    ct = pp.CT(data)

    print("Cargando estructuras...")
    structs = pp.Structures(data)

    print("Cargando beams...")
    beams = pp.Beams(data)

    return ct, structs, beams