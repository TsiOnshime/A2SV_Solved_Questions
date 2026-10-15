# Write your MySQL query statement below
select Customers.name Customers from Customers left join Orders on Customers.id = Orders.customerId where Orders.customerId is Null; 



-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna