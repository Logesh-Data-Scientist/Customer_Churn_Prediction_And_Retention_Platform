

-- Creating Indexes


CREATE INDEX idx_churn
ON Customer_churn_Data(Churn_Value);



CREATE INDEX idx_contract
ON Customer_churn_Data(Contract);



CREATE INDEX idx_tenure
ON Customer_churn_Data(Tenure_Months);