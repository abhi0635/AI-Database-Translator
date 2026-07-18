from database import get_connection

def validate_sql(sql):
    """
    Allow only SELECT queries.
    """

    sql = sql.strip().upper()

    if not sql.startswith("SELECT"):
        raise Exception("Only SELECT queries are allowed.")

    blocked_words = [
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER",
        "TRUNCATE",
        "CREATE",
        "EXEC",
        "MERGE"
    ]

    for word in blocked_words:
        if word in sql:
            raise Exception(f"Blocked SQL keyword: {word}")


def execute_query(sql):

    # Validate AI-generated SQL
    validate_sql(sql)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(sql)

    columns = [column[0] for column in cursor.description]

    rows = cursor.fetchall()

    conn.close()

    return columns, rows