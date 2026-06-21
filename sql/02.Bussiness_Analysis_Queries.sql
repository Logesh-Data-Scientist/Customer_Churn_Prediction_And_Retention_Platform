

-- Total Customers

SELECT 
    COUNT(*) AS TotalCustomers
FROM Customer_Churn_Data;


-- Total Churned Customers
-- churn value - 'yes' = 1

SELECT 
    COUNT(*) AS ChurnedCustomers
FROM Customer_Churn_Data
WHERE Churn_Value=1;


-- Total not Churned Customers
-- churn value - 'No' = 0

SELECT 
    COUNT(*) AS ChurnedCustomers
FROM Customer_Churn_Data
WHERE Churn_Value=0;


-- Churn Rate

SELECT
    ROUND((SELECT 
    COUNT(*) AS ChurnedCustomers
    FROM Customer_Churn_Data
    WHERE Churn_Value=1) * 100.0 / COUNT(*),2) AS ChurnRate
FROM Customer_Churn_Data;



-- Customers by Contract

SELECT
    Contract,
    COUNT(*) AS CustomerCount
FROM Customer_Churn_Data
GROUP BY Contract;


-- Churn by Contract


SELECT
    Contract,
    (CASE WHEN Churn_Value = 1 THEN 'Churned' ELSE 'Not Churned' END),
    COUNT(*) AS Customers
FROM Customer_Churn_Data
GROUP BY Contract, Churn_Value
ORDER BY Contract;


