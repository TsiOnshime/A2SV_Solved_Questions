# Write your MySQL query statement below
select name Employee from Employee e1 where e1.salary > (select e2.salary from Employee e2 where e2.id = e1.managerId)

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna