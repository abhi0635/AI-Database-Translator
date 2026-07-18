from translator import generate_sql
from executor import execute_query

question = "Show all restaurants in Hyderabad"

sql = generate_sql(question)

print("Generated SQL:")
print(sql)

columns, rows = execute_query(sql)

print("\nResults:")

print(columns)

for row in rows:
    print(row)