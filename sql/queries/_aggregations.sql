-- Этот запрос использует агрегацию, чтобы вычислить среднюю зарплату (AVG) для каждого отдела.
-- Он группирует результаты по department_id.
SELECT employees.department_id, AVG(salaries.amount) 
FROM salaries 
INNER JOIN employees ON salaries.employee_id = employees.id 
GROUP BY employees.department_id;

-- Этот запрос использует агрегацию и условие HAVING для фильтрации групп.
-- Он вычисляет среднюю зарплату для каждого отдела и возвращает только те отделы,
-- где средняя зарплата превышает 60000.
SELECT employees.department_id, AVG(salaries.amount) as avg_salary
FROM salaries 
INNER JOIN employees ON salaries.employee_id = employees.id 
GROUP BY employees.department_id
HAVING AVG(salaries.amount) > 60000;

-- Этот запрос использует агрегацию, чтобы подсчитать количество сотрудников (COUNT) в каждом отделе.
-- Он группирует результаты по department_id.
SELECT employees.department_id, COUNT(employees.id) as employee_count
FROM employees 
GROUP BY employees.department_id;

-- Этот запрос вычисляет среднюю зарплату для каждого проекта.
-- Он объединяет таблицы projects, employee_projects и salaries, затем группирует результаты по имени проекта.
SELECT projects.name, AVG(salaries.amount) as avg_salary
FROM projects
INNER JOIN employee_projects ON projects.id = employee_projects.project_id
INNER JOIN salaries ON employee_projects.employee_id = salaries.employee_id
GROUP BY projects.name;
