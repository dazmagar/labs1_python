import sqlite3
import typing as t
from datetime import date


def populate_db() -> None:
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    employees: t.List[t.Tuple[int, str, int, date]] = [(1, "Alice", 1, "2020-01-15"), (2, "Bob", 2, "2019-03-23"), (3, "Charlie", 1, "2021-06-12"), (4, "David", 3, "2018-07-30")]

    departments: t.List[t.Tuple[int, str]] = [(1, "HR"), (2, "Engineering"), (3, "Finance")]

    salaries: t.List[t.Tuple[int, int, float, date]] = [(1, 1, 50000.0, "2023-01-01"), (2, 2, 70000.0, "2023-01-01"), (3, 3, 60000.0, "2023-01-01"), (4, 4, 80000.0, "2023-01-01")]

    projects: t.List[t.Tuple[int, str, date, date]] = [(1, "Project A", "2022-01-01", "2022-12-31"), (2, "Project B", "2022-06-01", "2023-05-31"), (3, "Project C", "2023-01-01", "2023-12-31")]

    employee_projects: t.List[t.Tuple[int, int]] = [(1, 1), (2, 2), (3, 1), (4, 3)]

    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", employees)
    cursor.executemany("INSERT INTO departments VALUES (?, ?)", departments)
    cursor.executemany("INSERT INTO salaries VALUES (?, ?, ?, ?)", salaries)
    cursor.executemany("INSERT INTO projects VALUES (?, ?, ?, ?)", projects)
    cursor.executemany("INSERT INTO employee_projects VALUES (?, ?)", employee_projects)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    populate_db()
