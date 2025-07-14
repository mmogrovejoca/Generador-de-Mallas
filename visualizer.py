from pyvis.network import Network
from weasyprint import HTML
import os

def create_interactive_visualization(graph, output_filename="lineage.html"):
    """
    Crea una visualización de red interactiva a partir de un grafo de networkx.

    Args:
        graph (networkx.DiGraph): El grafo a visualizar.
        output_filename (str): El nombre del archivo HTML de salida.
    """
    net = Network(notebook=True, directed=True, cdn_resources='in_line')
    net.from_nx(graph)

    # Opciones de personalización
    net.set_options("""
    var options = {
      "nodes": {
        "font": {
          "size": 20
        }
      },
      "edges": {
        "color": {
          "inherit": true
        },
        "smooth": {
          "enabled": true,
          "type": "dynamic"
        }
      },
      "interaction": {
        "dragNodes": true,
        "hideEdgesOnDrag": false,
        "hideNodesOnDrag": false
      },
      "physics": {
        "enabled": false
      }
    }
    """)

    net.show(output_filename)

def export_html_to_pdf(html_file, pdf_file):
    """
    Convierte un archivo HTML a PDF.

    Args:
        html_file (str): La ruta al archivo HTML de entrada.
        pdf_file (str): La ruta al archivo PDF de salida.
    """
    if not os.path.exists(html_file):
        print(f"Error: El archivo HTML '{html_file}' no fue encontrado.")
        return

    print(f"Convirtiendo {html_file} a {pdf_file}...")
    HTML(html_file).write_pdf(pdf_file)
    print("Conversión a PDF completada.")
