
-- Verifiyng data import

SELECT *
FROM Customer_churn_Data;


-- Check total records:

SELECT COUNT(*) AS TotalRecords
FROM Customer_Churn_data;



-- Understand Table Structure

SELECT
    COLUMN_NAME,
    DATA_TYPE,
    CHARACTER_MAXIMUM_LENGTH,
    NUMERIC_PRECISION,
    NUMERIC_SCALE,
    IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Customer_Churn_Data'
ORDER BY ORDINAL_POSITION;



-- Check for NULL Values


SELECT
    COUNT(*) AS NullCustomerID
FROM Customer_Churn_data
WHERE CustomerID IS NULL;


-- Check for Duplicate Customers
-- there is currently no duplicates 

SELECT
    CustomerID,
    COUNT(*)
FROM Customer_Churn_data
GROUP BY CustomerID
HAVING COUNT(*) > 1;