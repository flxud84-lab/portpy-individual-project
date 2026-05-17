from pathlib import Path
import pickle


def save_solution(sol: dict, output_dir: str, patient_id: str) -> Path:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    file_path = output_path / f"{patient_id}_solution.pkl"

    with file_path.open("wb") as file:
        pickle.dump(sol, file)

    print(f"Solucion guardada en: {file_path}")

    return file_path