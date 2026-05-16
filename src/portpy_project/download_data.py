from pathlib import Path
from huggingface_hub import snapshot_download


def download_patient_data(
    repo_id: str,
    patient_id: str,
    data_dir: str,
) -> None:
    """
    Descarga los datos de un paciente desde Hugging Face.
    """

    output_dir = Path(data_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Descargando paciente: {patient_id}")

    snapshot_download(
        repo_id=repo_id,
        repo_type="dataset",
        local_dir=str(output_dir),
        allow_patterns=f"data/{patient_id}/**",
    )

    downloaded_patient_dir = output_dir / "data" / patient_id
    final_patient_dir = output_dir / patient_id

    if downloaded_patient_dir.exists() and not final_patient_dir.exists():
        downloaded_patient_dir.rename(final_patient_dir)

    print("Descarga completada.")