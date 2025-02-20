-- data/schema.sql
DROP TABLE IF EXISTS campaign_data;
CREATE TABLE campaign_data (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_date DATE,
    campaign TEXT,          -- 'A' or 'B'
    user_id INTEGER,
    cost REAL,              -- ad spend per user
    revenue REAL,           -- revenue per user
    clicks INTEGER,
    impressions INTEGER
);
