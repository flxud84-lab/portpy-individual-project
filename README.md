# PortPy Individual Project

## Descripción General

Este proyecto es una implementación educativa y experimental basada en el framework **PortPy** para planificación de tratamientos de radioterapia.

El objetivo principal es transformar los notebooks originales de PortPy en una aplicación Python modular, mantenible y escalable, siguiendo buenas prácticas de desarrollo de software.

Actualmente el proyecto permite:

* Descarga automática de datasets de pacientes
* Carga de estructuras clínicas y CT
* Construcción de planes de tratamiento
* Optimización IMRT
* Evaluación clínica del plan
* Guardado de resultados
* Preparación para múltiples pacientes

---

# Objetivos del Proyecto

Este proyecto fue creado para:

* Aprender arquitectura de proyectos en Python
* Comprender flujos de optimización IMRT
* Explorar planificación radioterapéutica
* Construir pipelines reproducibles
* Crear una base para futuras herramientas educativas

---

# Tecnologías Utilizadas

* Python
* PortPy
* CVXPY
* NumPy
* YAML
* Hugging Face Datasets

---

# Estructura del Proyecto

```txt
portpy-individual-project/
├── config/
│   └── settings.yaml
│
├── data/
│
├── outputs/
│
├── src/
│   └── portpy_project/
│       ├── config.py
│       ├── data_loader.py
│       ├── download_data.py
│       ├── evaluator.py
│       ├── optimizer.py
│       ├── output_manager.py
│       ├── patient_manager.py
│       ├── plan_builder.py
│       └── main.py
│
├── run.py
├── requirements.txt
└── README.md
```

---

# Instalación

## 1. Clonar el repositorio

```bash
[git clone https://github.com/flxud84-lab/portpy-individual-project.git
cd portpy-individual-project
```

---

## 2. Crear entorno virtual

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución del Proyecto

```bash
python run.py
```

---

# Configuración

La configuración principal del proyecto se encuentra en:

```txt
config/settings.yaml
```

Ejemplo:

```yaml
patient_id: "Lung_Patient_3"
solver: "SCS"

run_optimization: true
run_evaluation: true
save_outputs: true
```

---

# Funcionalidades Actuales

## Gestión de Pacientes

* Descarga automática de datasets
* Detección de pacientes locales
* Selección configurable de pacientes

## Planificación de Tratamiento

* Carga de criterios clínicos
* Generación de influence matrix
* Construcción del plan
* Optimización IMRT

## Evaluación Clínica

* Evaluación de restricciones clínicas
* Métricas relacionadas con DVH
* Exportación de resultados

---

# Flujo Actual del Sistema

```txt
Descarga de Dataset
        ↓
Carga del Paciente
        ↓
Construcción del Plan
        ↓
Generación de Influence Matrix
        ↓
Optimización IMRT
        ↓
Evaluación Clínica
        ↓
Guardado de Resultados
```

---

# Mejoras Futuras

## Ingeniería de Software

* Sistema de logging
* Manejo de errores
* Tests unitarios
* Interfaz CLI
* Docker

## Características Científicas

* Visualización DVH
* Visualización de dosis
* Visualización de beams
* Benchmarking de solvers
* Experimentos multi-paciente

## Características Educativas

* Módulos interactivos
* Sistema de evaluación clínica
* Ajuste dinámico de constraints
* Ejercicios de planificación

---

# Visión Educativa

Este proyecto busca evolucionar hacia una plataforma educativa de planificación radioterapéutica donde los estudiantes puedan:

* Explorar conceptos de planificación
* Experimentar con parámetros de optimización
* Comparar planes clínicos
* Comprender flujos IMRT de manera interactiva

---

# Créditos

* PortPy Project
* CVXPY
* Hugging Face Datasets

---
