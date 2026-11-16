
import pytest
import psycopg2

from students import add_student, get_student, average_grade


@pytest.fixture
def conn():
    connection = psycopg2.connect(
        host="localhost",
        database="tp",
        user="postgres",
        password="postgres"
    )

    with connection.cursor() as cur:
        cur.execute("DELETE FROM students")
    connection.commit()

    yield connection

    connection.close()


def test_ajouter_et_lire_etudiant(conn):
    add_student(conn, "Amel", 15)

    student = get_student(conn, "Amel")

    assert student == ("Amel", 15)


def test_etudiant_inexistant(conn):
    student = get_student(conn, "Inexistant")

    assert student is None


def test_moyenne(conn):
    add_student(conn, "Amel", 10)
    add_student(conn, "Karim", 14)

    assert average_grade(conn) == 12
