# analysis/ab_test.py
import sqlite3
import pandas as pd
from scipy import stats

DB = "../data/marketing.db"
conn = sqlite3.connect(DB)

# Pull revenue per user for A vs B
df = pd.read_sql("""
SELECT campaign, user_id, SUM(revenue) AS total_revenue
FROM campaign_data
GROUP BY campaign, user_id;
""", conn)

a = df[df.campaign=="A"].total_revenue
b = df[df.campaign=="B"].total_revenue

tstat, pval = stats.ttest_ind(a, b, equal_var=False)
print(f"A mean rev: {a.mean():.2f}, B mean rev: {b.mean():.2f}")
print(f"T-statistic: {tstat:.3f}, p-value: {pval:.3f}")
if pval < 0.05:
    print("→ Significant difference in revenue between A & B")
else:
    print("→ No significant difference detected")
