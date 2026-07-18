from flask import Flask, render_template, request

# Import your AI and SQL functions
from translator import generate_sql
from executor import execute_query

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    question = ""
    sql = ""
    columns = []
    rows = []

    if request.method == "POST":

        # Get question from HTML form
        question = request.form["question"]

        # Generate SQL using AI
        sql = generate_sql(question)

        # Execute SQL on SQL Server
        columns, rows = execute_query(sql)

    return render_template(
        "index.html",
        question=question,
        sql=sql,
        columns=columns,
        rows=rows
    )

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)