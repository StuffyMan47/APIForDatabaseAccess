from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import sqlite3

app = FastAPI()

#Подключение к бд
conn = sqlite3.connect('InformationAboutLessons.db')

#Через объект cur выполняются запросы к бд в формате cur.execute("SQL-ЗАПРОС-ЗДЕСЬ;")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS technologies(
    technologies id INT PRIMARY KEY,
    technologiesName TEXT);
""")
#Сохранение изменений
conn.commit()

cur.execute("""
PRAGMA foreign_keys=on;
CREATE TABLE IF NOT EXISTS theme(
    technologies id INT,
    FOREIGN KEY (technologies id) REFERENCES technologies (technologies id) ON DELETE CASCADE,
    theme id INT PRIMARY KEY AUTOINCREMENT,
    theme name TEXT,
    file path TEXT);
""")
conn.commit()


@app.get("/")
def read_root():
    html_content = "<h2>Hello METANIT.COM!</h2>"
    return HTMLResponse(content=html_content)