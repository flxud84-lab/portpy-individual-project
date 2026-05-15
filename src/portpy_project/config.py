from pathlib import Path
import yaml


def load_config(config_path: str = "config/settings.yaml") -> dict:
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(f"No existe el archivo de configuración: {path}")

    with path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if config is None:
        raise ValueError("El archivo de configuración está vacío.")

    return config