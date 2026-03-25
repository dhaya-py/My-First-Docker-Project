from fastapi import FastAPI
import psycopg2

app = FastAPI()

def get_db_connection():
    conn = psycopg2.connect(
        host="db",           # IMPORTANT
        database="erp",
        user="postgres",
        password="password"
    )
    return conn

@app.get("/")
def read_root():
    return {"message": "ERP backend is running!"}

@app.get("/test-db")
def test_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()
        conn.close()
        return {"db_status": "connected", "result": result}
    except Exception as e:
        return {"error": str(e)}
