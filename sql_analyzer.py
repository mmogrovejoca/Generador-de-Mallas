import sqlparse
from sqlparse.sql import Identifier, IdentifierList
from sqlparse.tokens import Keyword, DML

def extract_tables_from_sql(sql_script):
    """
    Analiza un script SQL para extraer las tablas y sus relaciones (FROM y JOINs).
    Utiliza un enfoque más robusto para identificar tablas.

    Args:
        sql_script (str): El script SQL como una cadena de texto.

    Returns:
        list: Una lista de diccionarios, donde cada diccionario representa una relación
              entre tablas.
    """
    relations = []
    statements = sqlparse.parse(sql_script)

    for statement in statements:
        if statement.get_type() != 'SELECT':
            continue

        from_table = None

        # Flatten the statement to get all tokens
        tokens = statement.flatten()

        # Find the main table in the FROM clause
        from_seen = False
        for token in tokens:
            if from_seen and token.ttype is sqlparse.tokens.Name:
                from_table = token.value
                break
            if token.ttype is Keyword and token.value.upper() == 'FROM':
                from_seen = True

        # Find all JOINs
        join_seen = False
        join_type = None
        for token in tokens:
            if join_seen and token.ttype is sqlparse.tokens.Name:
                if from_table:
                    relations.append({
                        'source': from_table,
                        'target': token.value,
                        'type': join_type
                    })
                join_seen = False

            if token.ttype is Keyword and 'JOIN' in token.value.upper():
                join_seen = True
                join_type = token.value.upper()

    return relations
