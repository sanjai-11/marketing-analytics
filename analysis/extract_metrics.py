# analysis/extract_metrics.py
import sqlite3
import pandas as pd

DB = "../data/marketing.db"
conn = sqlite3.connect(DB)

# SQL to compute daily CAC, LTV, CTR by campaign
sql = """
SELECT
  event_date,
  campaign,
  ROUND(SUM(cost)/COUNT(DISTINCT user_id), 2)    AS CAC,
  ROUND(SUM(revenue)/COUNT(DISTINCT user_id), 2) AS LTV,
  ROUND(SUM(clicks)*1.0/SUM(impressions), 4)     AS CTR
FROM campaign_data
GROUP BY event_date, campaign
ORDER BY event_date, campaign;
"""
df = pd.read_sql(sql, conn, parse_dates=["event_date"])
print(df.head())

# Save for Tableau
df.to_csv("analysis/metrics.csv", index=False)
print("Saved metrics.csv for Tableau import")
