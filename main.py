import argparse
import os
from sql_analyzer import extract_tables_from_sql
from python_interpreter import extract_sql_from_python
from graph_builder import build_graph
from visualizer import create_interactive_visualization, export_html_to_pdf

def main():
    parser = argparse.ArgumentParser(
        description="Genera un diagrama de linaje de tablas a partir de un script SQL o Python."
    )
    parser.add_argument(
        "input_file",
        help="La ruta al archivo de entrada (.sql o .py)."
    )
    parser.add_argument(
        "-o", "--output",
        help="El nombre del archivo de salida (sin extensión)."
    )
    parser.add_argument(
        "-f", "--format",
        default="html",
        choices=['html', 'pdf'],
        help="El formato de salida (html o pdf)."
    )
    args = parser.parse_args()

    input_file = args.input_file
    output_base_name = args.output or "lineage"
    output_format = args.format

    if not os.path.exists(input_file):
        print(f"Error: El archivo '{input_file}' no fue encontrado.")
        return

    file_extension = os.path.splitext(input_file)[1].lower()

    sql_script = ""
    if file_extension == '.sql':
        with open(input_file, 'r') as f:
            sql_script = f.read()
    elif file_extension == '.py':
        with open(input_file, 'r') as f:
            python_script = f.read()
        sql_queries = extract_sql_from_python(python_script)
        sql_script = "\n".join(sql_queries)
    else:
        print(f"Error: Tipo de archivo no soportado '{file_extension}'. Use .sql o .py.")
        return

    if not sql_script.strip():
        print("No se encontraron consultas SQL en el archivo de entrada.")
        return

    relations = extract_tables_from_sql(sql_script)
    if not relations:
        print("No se pudieron extraer relaciones de tablas del script SQL.")
        return

    graph = build_graph(relations)

    html_file = f"{output_base_name}.html"
    create_interactive_visualization(graph, output_filename=html_file)

    if output_format == 'pdf':
        pdf_file = f"{output_base_name}.pdf"
        export_html_to_pdf(html_file, pdf_file)
        os.remove(html_file) # Limpiar el archivo HTML intermedio
        print(f"¡Diagrama de linaje generado con éxito! Guardado como '{pdf_file}'.")
    else:
        print(f"¡Diagrama de linaje generado con éxito! Abre '{html_file}' en tu navegador.")

if __name__ == "__main__":
    main()
