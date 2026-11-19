SELECT
    Department.name AS department,
    Employee.name AS Employee,
    salary
FROM Employee
JOIN Department
    ON Employee.departmentId = Department.id
WHERE (departmentId, salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
);

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna