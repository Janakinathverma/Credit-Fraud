# app/queries.py

# 1. Total Transactions count
QUERY_TOTAL = "SELECT COUNT(*) FROM transactions"

# 2. Fraud Transactions count
QUERY_FRAUD_COUNT = "SELECT COUNT(*) FROM transactions WHERE Class = 1"

# 3. Average Transaction Amount (Genuine vs Fraud)
QUERY_AVG_AMOUNT = "SELECT Class, AVG(Amount) as avg_amt FROM transactions GROUP BY Class"

# 4. Max Fraud Amount
QUERY_MAX_FRAUD = "SELECT MAX(Amount) FROM transactions WHERE Class = 1"

# 5. Fraud Percentage
QUERY_FRAUD_PERCENT = """
SELECT (SUM(CASE WHEN Class = 1 THEN 1.0 ELSE 0 END) / COUNT(*)) * 100 
FROM transactions
"""

# 6. Time vs Fraud (Time column analysis)
QUERY_TIME_TREND = "SELECT Time, Amount, Class FROM transactions WHERE Class = 1 LIMIT 100"

# 7. Chart Data
QUERY_DONUT = "SELECT Class, COUNT(*) as count FROM transactions GROUP BY Class"
QUERY_HIST = "SELECT Amount, Class FROM transactions LIMIT 5000"