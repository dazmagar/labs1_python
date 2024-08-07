import sqlite3


def clear_db() -> None:
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM employees")
    cursor.execute("DELETE FROM departments")
    cursor.execute("DELETE FROM salaries")
    cursor.execute("DELETE FROM projects")
    cursor.execute("DELETE FROM employee_projects")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    clear_db()
