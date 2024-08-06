from app.database import get_db

def output_formatter(results):
    out = []
    for result in results:
        res = {
            "id":result[0],
            "name":result[1],
            "summary":result[2],
            "description":result[3],
            "is_done":result[4]
        }
        out.append(res)
    return out

def scan():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task WHERE id=?",(task_id))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def select_by_id():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task WHERE id=?",(task_id))
    results = cursor.fetchall()
    cursor.close()
    if results:
        return output_formatter(results)[0]
    return {}

def insert(task_data):
    task_tuple = (
        task_data.get("name"),
        task_data.get("summary"),
        task_data.get("description")
    )
    statement = }