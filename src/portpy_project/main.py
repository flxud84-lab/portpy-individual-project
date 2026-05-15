from portpy_project.config import load_config


def main() -> None:
    config = load_config()

    print("Proyecto PortPy iniciado correctamente.")
    print(f"Paciente seleccionado: {config['patient_id']}")
    print(f"Protocolo seleccionado: {config['protocol_name']}")
    print(f"Solver seleccionado: {config['solver']}")


if __name__ == "__main__":
    main()