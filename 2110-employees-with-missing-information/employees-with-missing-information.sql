/* Write your T-SQL query statement below */
select employee_id from employees
where employee_id not in (select employee_id from Salaries)
union
select employee_id from Salaries
where employee_id not in (select employee_id from Employees)