import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=ABHII\\SQLEXPRESS;"
        "Database=FoodDeliveryDB;"
        "Trusted_Connection=yes;"
    )
    return conn