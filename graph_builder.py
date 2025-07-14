import networkx as nx

def build_graph(relations):
    """
    Construye un grafo de networkx a partir de una lista de relaciones de tablas.

    Args:
        relations (list): Una lista de diccionarios de relaciones, donde cada
                          diccionario tiene 'source', 'target', y 'type'.

    Returns:
        networkx.DiGraph: Un grafo dirigido que representa las relaciones de las tablas.
    """
    G = nx.DiGraph()
    for rel in relations:
        source = rel['source']
        target = rel['target']
        join_type = rel['type']

        # Añadir nodos si no existen
        if not G.has_node(source):
            G.add_node(source, title=source)
        if not G.has_node(target):
            G.add_node(target, title=target)

        # Añadir una arista dirigida desde la tabla de origen a la de destino
        G.add_edge(source, target, label=join_type)

    return G
