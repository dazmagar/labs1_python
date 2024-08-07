import sqlite3
import typing as t


def execute_query_with_header(query: str, header: str) -> None:
    print(header)
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute(query)
    results: t.List[t.Tuple] = cursor.fetchall()

    # Print column headers
    col_names = [description[0] for description in cursor.description]
    print(col_names)

    # Print each row
    for row in results:
        print(row)

    conn.close()
    print("\n" + "-" * 50 + "\n")


def inner_join() -> None:
    query = """
    SELECT employees.name, departments.name 
    FROM employees 
    INNER JOIN departments ON employees.department_id = departments.id
    """
    execute_query_with_header(query, "Inner Join: Employees and Departments")


def left_join() -> None:
    query = """
    SELECT employees.name, departments.name 
    FROM employees 
    LEFT JOIN departments ON employees.department_id = departments.id
    """
    execute_query_with_header(query, "Left Join: Employees and Departments")


def right_join() -> None:
    query = """
    SELECT employees.name, departments.name 
    FROM departments 
    LEFT JOIN employees ON employees.department_id = departments.id
    """
    execute_query_with_header(query, "Right Join (simulated): Departments and Employees")


def aggregation() -> None:
    query = """
    SELECT employees.department_id, AVG(salaries.amount) 
    FROM salaries 
    INNER JOIN employees ON salaries.employee_id = employees.id 
    GROUP BY employees.department_id
    """
    execute_query_with_header(query, "Aggregation: Average Salary by Department")


def aggregation_with_having() -> None:
    query = """
    SELECT employees.department_id, AVG(salaries.amount) as avg_salary
    FROM salaries 
    INNER JOIN employees ON salaries.employee_id = employees.id 
    GROUP BY employees.department_id
    HAVING AVG(salaries.amount) > 60000
    """
    execute_query_with_header(query, "Aggregation with HAVING: Average Salary > 60000")


def aggregation_with_count() -> None:
    query = """
    SELECT employees.department_id, COUNT(employees.id) as employee_count
    FROM employees 
    GROUP BY employees.department_id
    """
    execute_query_with_header(query, "Aggregation with COUNT: Number of Employees by Department")


def complex_query() -> None:
    query = """
    SELECT projects.name, AVG(salaries.amount) as avg_salary
    FROM projects
    INNER JOIN employee_projects ON projects.id = employee_projects.project_id
    INNER JOIN salaries ON employee_projects.employee_id = salaries.employee_id
    GROUP BY projects.name
    """
    execute_query_with_header(query, "Complex Query: Average Salary by Project")


if __name__ == "__main__":
    inner_join()
    left_join()
    right_join()
    aggregation()
    aggregation_with_having()
    aggregation_with_count()
    complex_query()
