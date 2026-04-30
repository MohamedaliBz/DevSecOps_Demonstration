from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

def get_db():
    return sqlite3.connect("users.db")

@app.route("/")
def home():
    return "DevSecOps Demo"

@app.route("/search")
def search():
    name = request.args.get("name", "")
    
    # ❌ SQL Injection
    cursor = conn.execute(
    "SELECT * FROM users WHERE name = ?",
    (name,)
)
    
    conn = get_db()
    result = conn.execute(query).fetchall()
    
    return str(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)