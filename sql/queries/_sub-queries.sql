-- Подзапрос для нахождения сотрудников с зарплатой выше средней
-- Этот запрос сначала вычисляет среднюю зарплату, а затем выбирает имена сотрудников,
-- чья зарплата выше этой средней.
SELECT name, amount 
FROM employees 
JOIN salaries ON employees.id = salaries.employee_id 
WHERE amount > (SELECT AVG(amount) FROM salaries);

-- Подзапрос для нахождения отделов с количеством сотрудников больше 1
-- Этот запрос сначала подсчитывает количество сотрудников в каждом отделе,
-- а затем выбирает только те отделы, где количество сотрудников больше 1.
SELECT name 
FROM departments 
WHERE id IN (SELECT department_id FROM employees GROUP BY department_id HAVING COUNT(*) > 1);

-- Коррелированный подзапрос для нахождения сотрудников с самой высокой зарплатой в каждом отделе
-- Этот запрос использует коррелированный подзапрос для нахождения максимальной зарплаты в каждом отделе,
-- а затем выбирает сотрудников с этой максимальной зарплатой.
SELECT name, department_id, amount 
FROM employees e 
JOIN salaries s ON e.id = s.employee_id 
WHERE amount = (SELECT MAX(amount) 
                FROM salaries s2 
                JOIN employees e2 ON s2.employee_id = e2.id 
                WHERE e2.department_id = e.department_id);

-- Подзапрос в FROM для нахождения средней зарплаты по отделам и количества сотрудников в одном запросе
-- Этот запрос использует подзапрос в секции FROM для получения средней зарплаты по отделам,
-- а затем объединяет эти данные с количеством сотрудников в каждом отделе.
SELECT d.name, avg_salaries.avg_salary, emp_counts.employee_count 
FROM departments d 
JOIN (SELECT department_id, AVG(amount) AS avg_salary 
      FROM salaries s 
      JOIN employees e ON s.employee_id = e.id 
      GROUP BY department_id) avg_salaries 
ON d.id = avg_salaries.department_id 
JOIN (SELECT department_id, COUNT(*) AS employee_count 
      FROM employees 
      GROUP BY department_id) emp_counts 
ON d.id = emp_counts.department_id;
