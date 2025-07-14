import ast
import re

def extract_sql_from_python(python_script):
    """
    Analiza un script de Python para extraer cadenas que contengan consultas SQL.

    Args:
        python_script (str): El script de Python como una cadena de texto.

    Returns:
        list: Una lista de cadenas, donde cada cadena es una consulta SQL.
    """
    sql_queries = []
    try:
        tree = ast.parse(python_script)
        for node in ast.walk(tree):
            if isinstance(node, ast.Str):
                # Usar una expresión regular para detectar palabras clave de SQL
                if re.search(r'\b(SELECT|FROM|JOIN|WHERE|INSERT|UPDATE|DELETE)\b', node.s, re.IGNORECASE):
                    sql_queries.append(node.s)
    except SyntaxError as e:
        print(f"Error de sintaxis en el script de Python: {e}")

    return sql_queries
