# Write your MySQL query statement below
select P.firstName, P.lastName, A.city, A.state from Person as P Left join Address as A on P.personId = A.personId;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna