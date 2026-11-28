from flask import Flask, jsonify, request
from flask_cors import CORS
import os, psycopg2
from psycopg2.extras import RealDictCursor
app = Flask(__name__)
CORS(app)
DB_HOST=os.getenv("DB_HOST","postgres")
DB_NAME=os.getenv("DB_NAME","tasksdb")
DB_USER=os.getenv("DB_USER","tasksuser")
DB_PASSWORD=os.getenv("DB_PASSWORD","taskspass")
def conn():
    return psycopg2.connect(host=DB_HOST,dbname=DB_NAME,user=DB_USER,password=DB_PASSWORD)
def init_db():
    with conn() as c:
        with c.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS tasks (id SERIAL PRIMARY KEY, title TEXT NOT NULL, done BOOLEAN DEFAULT FALSE)")
@app.route("/api/health")
def health():
    return jsonify(status="healthy")
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    with conn() as c:
        with c.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT id,title,done FROM tasks ORDER BY id")
            return jsonify(cur.fetchall())
@app.route("/api/tasks", methods=["POST"])
def add_task():
    title=(request.json or {}).get("title","").strip()
    if not title: return jsonify(error="title required"),400
    with conn() as c:
        with c.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("INSERT INTO tasks(title) VALUES(%s) RETURNING id,title,done",(title,))
            return jsonify(cur.fetchone()),201
@app.route("/api/tasks/<int:task_id>", methods=["PATCH"])
def toggle(task_id):
    with conn() as c:
        with c.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("UPDATE tasks SET done=NOT done WHERE id=%s RETURNING id,title,done",(task_id,))
            row=cur.fetchone()
            if not row: return jsonify(error="not found"),404
            return jsonify(row)
@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete(task_id):
    with conn() as c:
        with c.cursor() as cur: cur.execute("DELETE FROM tasks WHERE id=%s",(task_id,))
    return jsonify(message="deleted")
if __name__=="__main__":
    init_db()
    app.run(host="0.0.0.0",port=5000)
