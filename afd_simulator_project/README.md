# Simulador de AFD / AFND con interfaz gráfica

## Introducción y objetivo
Esta práctica implementa una aplicación de escritorio en **Python + Tkinter** para:
- definir autómatas de manera manual,
- importar/exportar autómatas en **.jff, .json y .xml**,
- simular cadenas,
- ejecutar validación paso a paso,
- convertir **AFND** y **AFND-λ** a **AFD**,
- calcular **subcadenas, prefijos, sufijos**, y
- generar **cerradura de Kleene (Σ\*)** y **cerradura positiva (Σ+)**.

La aplicación fue pensada para cubrir la práctica solicitada. Como en la consigna no se adjuntaron los ejercicios concretos de la **Lista 2** y **Lista 3**, el repositorio incluye la **aplicación completa**, varios **autómatas de ejemplo** y la **estructura lista** para que agregues/exportes los ejercicios específicos cuando tengas la lista oficial.

## Tecnologías usadas
- Python 3.10+
- Tkinter (incluido en Python estándar)
- xml.etree.ElementTree
- json

No requiere librerías externas.

## Estructura del repositorio
```text
afd_simulator_project/
├── src/
│   ├── automaton.py         # Modelo de autómata, simulación y utilidades
│   ├── io_formats.py        # Importación y exportación .jff/.json/.xml
│   ├── gui_app.py           # Interfaz gráfica
│   └── main.py              # Punto de entrada
├── examples/
│   ├── jff/                 # Ejemplos en formato JFLAP
│   ├── json/                # Ejemplos en JSON
│   ├── xml/                 # Ejemplos en XML
│   └── strings/             # Cadenas de prueba
├── output/
│   ├── Lista2_AFD/
│   ├── Lista3_AFND_A/
│   ├── Lista3_AFND_B/
│   └── Conversiones_AFD/
└── README.md
```

## Funcionalidades implementadas

### 1) Creación y definición interactiva
- Captura manual de:
  - alfabeto,
  - estados,
  - estado inicial,
  - estados de aceptación,
  - tabla de transición.
- Edición directa de la función de transición.
- Visualización del autómata en un lienzo.
- Tabla de transición mostrada en el panel de información.

### 2) Importación desde archivos
- Carga archivos:
  - `.jff` (JFLAP)
  - `.json`
  - `.xml`
- Se interpretan:
  - alfabeto,
  - estados,
  - estado inicial,
  - aceptación,
  - transiciones.

### 3) Simulación y validación
- Validación directa de cadenas.
- Resultado: **ACEPTADA** o **RECHAZADA**.
- Simulación **paso a paso** con traza completa.
- Resaltado del estado actual y transición usada.
- Si el autómata cargado es AFND o AFND-λ, primero se convierte a AFD para simular.

### 4) Funcionalidades adicionales
- Exportación a:
  - `.jff`
  - `.json`
  - `.xml`
- Cálculo de:
  - prefijos,
  - sufijos,
  - subcadenas.
- Exportación de resultados a `.txt`.
- Generación de:
  - `Σ*`
  - `Σ+`
  con longitud máxima configurable.

## Conversión de AFND y AFND-λ
La app incluye determinización por construcción de subconjuntos:
- **AFND → AFD**
- **AFND-λ → AFD** usando cerradura-ε (representada como `λ`)

## Instrucciones de instalación y ejecución

### Opción 1: ejecutar directo
```bash
cd afd_simulator_project/src
python main.py
```

### Opción 2: desde la raíz
```bash
python src/main.py
```

## Cómo usar la aplicación
1. Abre la app.
2. En la pestaña **Definición** captura alfabeto y estados.
3. Presiona **Construir tabla**.
4. Llena la tabla de transición.
5. Presiona **Aplicar cambios**.
6. Usa **Cargar** para importar `.jff`, `.json` o `.xml`.
7. Usa **Guardar .jff** o exporta a `.json` / `.xml`.
8. En **Simulación**, escribe una cadena y presiona **Validar**.
9. Para ver la traza, usa **Preparar paso a paso** y luego **Siguiente paso**.
10. En **Utilidades**, calcula subcadenas/prefijos/sufijos o Σ\*/Σ+.

## Autómatas de ejemplo incluidos
Se incluyen 3 ejemplos base:
1. **dfa_ends_with_1**: AFD que acepta cadenas binarias que terminan en `1`.
2. **nfa_contains_ab**: AFND que reconoce cadenas sobre `{a,b}` que contienen `ab`.
3. **nfae_even_a_or_b**: AFND-λ de ejemplo con transición lambda.

## Ejemplos de cadenas para validación
En `examples/strings/` hay archivos `.txt` con ejemplos de prueba.

## Capturas de pantalla
No pude generar capturas reales desde este entorno porque no hay escritorio gráfico disponible. El proyecto está listo para que abras la app y tomes capturas para tu README de GitHub.

## Entregable cubierto
Este proyecto cubre:
- código fuente organizado,
- documentación interna básica,
- README,
- ejemplos de prueba,
- importación/exportación en `.jff`, `.json`, `.xml`,
- simulación y validación,
- utilidades solicitadas.

## Pendiente para dejarlo 100% idéntico a tu curso
Solo falta agregar los autómatas exactos de la **Lista 2** y **Lista 3**, porque la consigna compartida no incluye los ejercicios concretos. La carpeta `output/` ya quedó preparada para guardarlos y organizarlos tal como pide la entrega.
