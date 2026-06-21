

-- Creating Business Views


-- Churn Summary View

CREATE VIEW vw_ChurnSummary AS
SELECT
    CustomerID,
    Gender,
    Tenure_Months,
    Contract,
    Monthly_Charges,
    Total_Charges,
    Churn_value
FROM Customer_Churn_Data;

SELECT *
FROM vw_ChurnSummary;


-- KPI View

CREATE VIEW vw_KPI_Churn AS
SELECT
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn_value = 1 THEN 1 ELSE 0 END) AS ChurnedCustomers,
    SUM(CASE WHEN Churn_value = 0 THEN 1 ELSE 0 END) AS RetainedCustomers
FROM Customer_Churn_Data;


SELECT *
FROM vw_KPI_Churn;


-- Contract Analysis

CREATE VIEW vw_Contract_Analysis AS
SELECT
    Contract,
    COUNT(*) AS TotalCustomers,
    AVG(Monthly_Charges) AS AvgMonthlyCharges
FROM Customer_Churn_Data
GROUP BY Contract;


SELECT *
FROM vw_Contract_Analysis;