# Tutor Inteligente para Evaluación de Planes IMRT con PortPy

Sistema inteligente para construcción, evaluación clínica y análisis pedagógico de planes IMRT utilizando PortPy.

---

# Descripción del Proyecto

Este proyecto implementa un sistema interactivo capaz de:

- Construir planes IMRT automáticamente.
- Optimizar distribuciones de dosis.
- Generar curvas DVH.
- Evaluar criterios clínicos.
- Guiar pedagógicamente al estudiante.
- Comparar múltiples pacientes clínicamente.
- Validar respuestas automáticamente.
- Generar retroalimentación clínica y pedagógica.

El sistema funciona como un tutor inteligente para enseñanza de radioterapia IMRT.

---

# Características Principales

## Optimización IMRT

- Construcción automática del plan.
- Generación de matriz de influencia.
- Optimización usando CVXPY.
- Evaluación clínica automática.

---

## Evaluación Dosimétrica

El sistema analiza:

### Métricas PTV

- D98%
- D50%
- D2%

### Órganos a Riesgo (OAR)

- V20 pulmón
- Dmean cardíaco
- Restricciones clínicas DVH

---

## Visualización DVH

- Generación automática de DVH.
- Visualización interactiva.
- La gráfica permanece abierta durante el análisis.
- Soporte pedagógico para interpretación.

---

## Tutor Inteligente Pedagógico

El sistema incluye:

- Más de 100 preguntas pedagógicas.
- Preguntas aleatorias.
- Validación automática.
- Retroalimentación inmediata.
- Corrección interactiva.
- No repite preguntas correctamente respondidas.

---

## Comparación Clínica Entre Casos

Permite comparar:

- Cobertura PTV.
- Hot spots.
- Protección pulmonar.
- Protección cardíaca.
- Homogeneidad.
- Calidad global del plan.

---

# Arquitectura del Sistema

El sistema se divide en seis etapas:

1. Inicialización y carga de datos.
2. Construcción del plan IMRT.
3. Optimización clínica.
4. Visualización DVH y análisis pedagógico.
5. Comparación clínica entre pacientes.
6. Reflexión final y retroalimentación.

---

# Flujo General

```text
Inicio
  ↓
Carga configuración
  ↓
Carga paciente
  ↓
Construcción plan IMRT
  ↓
Optimización
  ↓
Evaluación clínica
  ↓
Generación DVH
  ↓
Análisis pedagógico
  ↓
Segundo caso clínico
  ↓
Comparación clínica
  ↓
Retroalimentación final
