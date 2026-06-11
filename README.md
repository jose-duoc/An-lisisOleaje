# 🏄‍♂️ Monitoreo de Olas Costeras

¡Bienvenido al sistema de **Monitoreo de Olas Costeras**! Esta es una aplicación de consola interactiva desarrollada en Python, diseñada para surfistas y entusiastas del mar. El sistema permite evaluar las condiciones climáticas y marítimas actuales para determinar si el día es apto para el surf y si existen riesgos de seguridad.

---

## 🚀 Características principales

El script ofrece un menú interactivo con las siguientes funcionalidades:
* **Evaluación de Olas:** Determina si el tamaño de la ola es ideal para surfear.
* **Alerta de Viento:** Analiza la velocidad del viento y advierte si las corrientes representan un peligro.
* **Guía de Equipamiento:** Consulta los límites de temperatura del agua para recomendar el uso de trajes de neopreno adecuados.
* **Avisos Oficiales:** Muestra las alertas de marejadas vigentes emitidas por la Armada.
* **Actualización en Tiempo Real:** Permite modificar los datos de olas y viento sin necesidad de reiniciar la aplicación.

---

## 🛠️ Estructura del Código

El proyecto está diseñado de forma modular, aplicando diferentes tipos de funciones para resolver problemas específicos:

| Tipo de Función | Ejemplo en el Código | Descripción |
| :--- | :--- | :--- |
| **Con parámetros y con retorno** | `es_surfeable(altura)` | Evalúa la altura y devuelve un valor booleano (`True`/`False`). |
| **Con parámetros y sin retorno** | `alertar_viento_peligroso(viento)` | Imprime alertas en pantalla según los nudos ingresados. |
| **Sin parámetros y con retorno** | `obtener_temperatura_limite_traje()` | Retorna el umbral de temperatura crítica configurado. |
| **Sin parámetros y sin retorno** | `mostrar_advertencia_marejada()` | Despliega un aviso estático de la Armada. |

---

## 📋 Requisitos Previos

Solo necesitas tener instalado **Python 3.x** en tu sistema. No requiere librerías externas de terceros.

---

## 🔧 Instalación y Ejecución

1. **Clona este repositorio** en tu máquina local:
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
