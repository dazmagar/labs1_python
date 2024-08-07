-- SQLite
SELECT d.* FROM departments as d;
SELECT e.* FROM employees as e;
SELECT s.* FROM salaries as s;

-- Этот запрос использует внутреннее соединение, чтобы выбрать имена сотрудников и
-- названия их отделов. Внутреннее соединение (inner join) возвращает только те строки,
-- для которых существует соответствие в обеих таблицах.
SELECT employees.name, departments.name 
FROM employees 
INNER JOIN departments ON employees.department_id = departments.id;

-- Этот запрос использует левое соединение, чтобы выбрать имена сотрудников и
-- названия их отделов. Левое соединение (left join) возвращает все строки из левой таблицы (employees),
-- и соответствующие строки из правой таблицы (departments). Если соответствующих строк нет, возвращаются NULL значения.
SELECT employees.name, departments.name 
FROM employees 
LEFT JOIN departments ON employees.department_id = departments.id;

-- Этот запрос использует левое соединение для имитации правого соединения. 
-- Он выбирает все строки из правой таблицы (departments), и соответствующие строки из левой таблицы (employees).
-- Если соответствующих строк нет, возвращаются NULL значения.
SELECT employees.name, departments.name 
FROM departments 
LEFT JOIN employees ON employees.department_id = departments.id;
