from translator import generate_sql

question = "Show all restaurants in Hyderabad"

sql = generate_sql(question)

print(sql)