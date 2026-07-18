# 🍽️ AI Database Translator

An AI-powered application that converts natural language questions into SQL queries using a local Large Language Model (LLM) through LM Studio.

## 🚀 Features

- Convert English to SQL
- Uses Qwen2.5 3B via LM Studio
- Executes SQL on Microsoft SQL Server
- Flask Web Interface
- Built-in SQL validation
- Only SELECT queries are allowed for security
- Displays query results in a clean interface

## 🛠️ Tech Stack

- Python
- Flask
- Microsoft SQL Server
- PyODBC
- LM Studio
- OpenAI Python SDK
- HTML
- CSS

## 📂 Project Structure

```
AI-Database-Translator/
│
├── app.py
├── translator.py
├── executor.py
├── database.py
├── templates/
│   ├── index.html
│   └── static/
│       └── style.css
├── test_ai.py
├── test_execute.py
├── test_connection.py
└── README.md
```

## ⚙️ How it Works

1. User enters a question.
2. LM Studio converts it into SQL.
3. SQL validation ensures only SELECT statements run.
4. SQL Server executes the query.
5. Results are displayed on the web page.

## 🔒 Security

- Only SELECT queries are executed.
- DROP, DELETE, UPDATE, INSERT, ALTER and TRUNCATE are blocked.

## 📸 Demo

Coming Soon

## 👨‍💻 Author

**Kotakonda Abhinay**

GitHub:
https://github.com/abhi0635