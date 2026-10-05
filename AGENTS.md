# Agent Rules for Master Big Data & IA

## Project Context
Este repositorio se utiliza para almacenar los apuntes, trabajos, documentación y ejercicios de la especialidad de Big Data e Inteligencia Artificial para FP.

## Directory Structure
- `clases/`: Contiene una carpeta por cada asignatura.
  - Cada asignatura contiene las subcarpetas: `presentaciones`, `grabaciones`, `entregables`, `calificaciones`, `anotaciones`.
    - **Gestión de `grabaciones`**: Debido al gran volumen de estos ficheros, no se almacenan directamente en el repositorio; se incluirán archivos Markdown con los enlaces a las grabaciones en Google Drive.
- `calendario/`: Documentación y calendarios del curso.
- `facturas/`: Facturas y temas administrativos.

## Workflow Rules (Working on Specs)
1. **Trabajo basado en Specs**: El enfoque principal es "trabajar sobre specs". Antes de generar código, resolver entregables o crear documentación extensa, debes buscar, leer o solicitar las especificaciones (specs) correspondientes.
2. **Alineación**: Todo trabajo generado debe estar estrictamente alineado con los requisitos indicados en los specs.
3. **Estructura Estricta**: Al generar archivos, respeta siempre la estructura de directorios descrita arriba. Coloca los documentos en las carpetas de sus respectivas asignaturas.
4. **Idioma**: Utiliza español por defecto, a menos que se solicite lo contrario.
5. **Formato de Documentación**: Toda la documentación adicional que se genere debe escribirse siempre en **Markdown**, utilizando texto enriquecido, formato adecuado, tablas y otros recursos visuales para hacerla lo más clara y estructurada posible. Para diagramas se utilizará **Mermaid** con la sintaxis **`flowchart`** (`flowchart TD` o `flowchart LR`) como estándar por defecto. Para bloques destacados o notas, se usará formato de cita estándar compatible con VS Code y GitHub (`> 💡 **Nota:**`, `> 📌`, etc.), evitando etiquetas propietarias no renderizables como `[!NOTE]`.
6. **Nombres de Carpetas**: El nombre de las carpetas siempre debe estar todo en minúsculas y en formato `snake_case` (sin espacios ni acentos, ej. `sistemas_de_big_data`).
7. **Ejemplos Prácticos en Python**: Siempre que se documente teoría o se expliquen conceptos, es **obligatorio** que todos los ejemplos de código se implementen siempre en **Python** (utilizando librerías del ecosistema de datos como Pandas, PySpark o Python estándar), directamente aplicados al caso de uso y la documentación explicada.
8. **Gestión de Grabaciones**: Al ser archivos de gran volumen, nunca se almacenarán directamente en el repositorio. En su lugar, se creará un archivo Markdown dentro de la carpeta `grabaciones/` de la asignatura con los enlaces correspondientes a las grabaciones en Google Drive.

