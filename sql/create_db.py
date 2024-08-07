import sqlite3


def create_db() -> None:
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department_id INTEGER,
        hire_date DATE
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS salaries (
        id INTEGER PRIMARY KEY,
        employee_id INTEGER,
        amount REAL,
        pay_date DATE
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY,
        name TEXT,
        start_date DATE,
        end_date DATE
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS employee_projects (
        employee_id INTEGER,
        project_id INTEGER,
        PRIMARY KEY (employee_id, project_id)
    )
    """
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_db()
