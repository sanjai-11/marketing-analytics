# data/generate_data.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_marketing_data(num_days=90, num_campaigns=5):
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=num_days)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # Initialize empty lists to store data
    data = []
    
    # Campaign names
    campaigns = [f'Campaign_{i}' for i in range(1, num_campaigns + 1)]
    
    # Generate data for each date and campaign
    for date in dates:
        for campaign in campaigns:
            # Generate base metrics
            impressions = np.random.randint(1000, 10000)
            clicks = int(impressions * np.random.uniform(0.02, 0.08))
            conversions = int(clicks * np.random.uniform(0.05, 0.15))
            revenue = conversions * np.random.uniform(50, 200)
            cost = impressions * np.random.uniform(0.1, 0.5)
            
            # Add some seasonality
            if date.weekday() in [5, 6]:  # Weekend effect
                impressions *= 1.2
                clicks *= 1.15
                conversions *= 1.1
            
            # Add some campaign-specific effects
            campaign_multiplier = 1 + (campaigns.index(campaign) * 0.1)
            impressions *= campaign_multiplier
            clicks *= campaign_multiplier
            conversions *= campaign_multiplier
            revenue *= campaign_multiplier
            cost *= campaign_multiplier
            
            # Calculate metrics
            ctr = clicks / impressions
            cpc = cost / clicks
            cac = cost / conversions if conversions > 0 else 0
            ltv = revenue / conversions if conversions > 0 else 0
            
            data.append({
                'date': date,
                'campaign': campaign,
                'impressions': int(impressions),
                'clicks': int(clicks),
                'conversions': int(conversions),
                'revenue': round(revenue, 2),
                'cost': round(cost, 2),
                'ctr': round(ctr, 4),
                'cpc': round(cpc, 2),
                'cac': round(cac, 2),
                'ltv': round(ltv, 2)
            })
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv('data/marketing_metrics.csv', index=False)
    print(f"Generated marketing data with {len(df)} rows")
    return df

if __name__ == "__main__":
    df = generate_marketing_data()
