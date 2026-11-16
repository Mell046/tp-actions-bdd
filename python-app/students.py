def add_student(conn, name, grade):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO students (name, grade) VALUES (%s, %s)",
            (name, grade)
        )
    conn.commit()


def get_student(conn, name):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT name, grade FROM students WHERE name = %s",
            (name,)
        )
        return cur.fetchone()


def average_grade(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT AVG(grade) FROM students")
        return cur.fetchone()[0]