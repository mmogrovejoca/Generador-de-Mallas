from pyvis.network import Network

def create_interactive_visualization(graph, output_filename="lineage.html"):
    """
    Crea una visualización de red interactiva a partir de un grafo de networkx.

    Args:
        graph (networkx.DiGraph): El grafo a visualizar.
        output_filename (str): El nombre del archivo HTML de salida.
    """
    net = Network(notebook=True, directed=True)
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
        "enabled": true,
        "solver": "repulsion"
      }
    }
    """)

    net.show(output_filename)
