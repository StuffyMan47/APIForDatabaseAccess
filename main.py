from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import sqlite3

app = FastAPI()

#Подключение к бд
conn = sqlite3.connect('InformationAboutLessons.db')

#Через объект cur выполняются запросы к бд в формате cur.execute("SQL-ЗАПРОС-ЗДЕСЬ;")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS technologies(
    technologies_id INT PRIMARY KEY,
    technologies_name TEXT);
""")
# Сохранение изменений
conn.commit()

cur.executescript("""
PRAGMA foreign_keys=on;
CREATE TABLE IF NOT EXISTS theme(
    technologies_id INT,
    theme_id INTEGER PRIMARY KEY AUTOINCREMENT,
    theme_name TEXT,
    file_path TEXT,
    FOREIGN KEY(technologies_id) REFERENCES technologies (technologies_id) ON DELETE CASCADE);
""")
conn.commit()
conn.close()

@app.get("/data")
def default_root():
    htmlContent = cur.execute("SELECT technologies_name FROM technologies")
    return HTMLResponse(content=htmlContent)

@app.get("/C#")
def root():
    htmlContent = cur.execute("SELECT theme_name FROM theme WHERE technologies_id='1'")
    return HTMLResponse(content=htmlContent)