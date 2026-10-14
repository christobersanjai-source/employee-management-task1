from app.db.session import get_db_connection
def _dict(row):
    if row is None: return None
    return {"id":row[0],"name":row[1],"email":row[2],"department":row[3],"job_title":row[4]}
def create_employee(e):
    q="INSERT INTO employees (name,email,department,job_title) VALUES (%s,%s,%s,%s) RETURNING id,name,email,department,job_title"
    with get_db_connection() as c:
        with c.cursor() as cur:
            cur.execute(q,(e.name,str(e.email),e.department,e.job_title)); row=cur.fetchone()
    return _dict(row)
def get_all_employees():
    with get_db_connection() as c:
        with c.cursor() as cur:
            cur.execute("SELECT id,name,email,department,job_title FROM employees ORDER BY id"); rows=cur.fetchall()
    return [_dict(r) for r in rows]
def get_employee_by_id(i):
    with get_db_connection() as c:
        with c.cursor() as cur:
            cur.execute("SELECT id,name,email,department,job_title FROM employees WHERE id=%s",(i,)); row=cur.fetchone()
    return _dict(row)
def update_employee(i,e):
    q="UPDATE employees SET name=%s,email=%s,department=%s,job_title=%s WHERE id=%s RETURNING id,name,email,department,job_title"
    with get_db_connection() as c:
        with c.cursor() as cur:
            cur.execute(q,(e.name,str(e.email),e.department,e.job_title,i)); row=cur.fetchone()
    return _dict(row)
def delete_employee(i):
    with get_db_connection() as c:
        with c.cursor() as cur:
            cur.execute("DELETE FROM employees WHERE id=%s RETURNING id",(i,)); row=cur.fetchone()
    return row is not None
