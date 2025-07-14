# SQL & Python Lineage Visualizer

Esta herramienta te permite analizar scripts de SQL y Python para identificar la conectividad entre tablas y generar un diagrama de flujo visual e interactivo que muestra su linaje y trazabilidad.

## Características

-   **Analizador de SQL:** Extrae tablas y sus relaciones (FROM y JOINs) de scripts SQL.
-   **Intérprete de Python:** Encuentra y extrae consultas SQL de scripts de Python.
-   **Visualización Interactiva:** Genera un diagrama de red interactivo (HTML) donde puedes mover los nodos (tablas) para explorar las relaciones.
-   **Exportación a PDF:** Convierte el diagrama de linaje en un archivo PDF.

## Instalación

Sigue estos pasos para configurar el entorno y empezar a usar la herramienta.

### 1. Clona el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd Generador-de-Mallas
```

### 2. Crea un entorno virtual (Recomendado)

Es una buena práctica usar un entorno virtual para aislar las dependencias del proyecto.

```bash
python -m venv venv
source venv/bin/activate  # En Windows, usa `venv\Scripts\activate`
```

### 3. Instala las dependencias

Instala todas las librerías necesarias desde el archivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

## Uso

La herramienta se ejecuta desde la línea de comandos. A continuación se muestran algunos ejemplos.

### Sintaxis Básica

```bash
python main.py <archivo_de_entrada> [opciones]
```

### Argumentos

-   `input_file`: La ruta al archivo de entrada (`.sql` o `.py`).
-   `-o, --output`: El nombre base para el archivo de salida (sin extensión). Por defecto, es `lineage`.
-   `-f, --format`: El formato de salida. Puede ser `html` (por defecto) o `pdf`.

### Ejemplos

#### 1. Analizar un archivo SQL y generar un HTML

Supongamos que tienes un archivo `queries.sql` con tus consultas.

```bash
python main.py queries.sql
```

Esto generará un archivo `lineage.html` en la misma carpeta.

#### 2. Analizar un archivo Python y generar un PDF

Si tienes un script `data_pipeline.py` que contiene consultas SQL.

```bash
python main.py data_pipeline.py --format pdf
```

Esto generará un archivo `lineage.pdf`.

#### 3. Especificar un nombre de salida personalizado

Puedes darle un nombre específico a tu archivo de salida.

```bash
python main.py queries.sql --output mi_diagrama --format pdf
```

Esto creará un archivo llamado `mi_diagrama.pdf`.
