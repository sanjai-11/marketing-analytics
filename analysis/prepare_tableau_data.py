import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def prepare_tableau_data():
    # Load the marketing data
    df = pd.read_csv('data/marketing_metrics.csv')
    
    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Add time-based dimensions
    df['month'] = df['date'].dt.month
    df['month_name'] = df['date'].dt.strftime('%B')
    df['week'] = df['date'].dt.isocalendar().week
    df['day_of_week'] = df['date'].dt.day_name()
    df['quarter'] = df['date'].dt.quarter
    
    # Calculate additional metrics
    df['roi'] = ((df['revenue'] - df['cost']) / df['cost'] * 100).round(2)
    df['conversion_rate'] = (df['conversions'] / df['clicks'] * 100).round(2)
    df['profit'] = df['revenue'] - df['cost']
    
    # Calculate rolling averages (7-day)
    for metric in ['ctr', 'cac', 'ltv', 'roi']:
        df[f'{metric}_7d_avg'] = df.groupby('campaign')[metric].transform(
            lambda x: x.rolling(window=7, min_periods=1).mean()
        ).round(4)
    
    # Create campaign performance summary
    campaign_summary = df.groupby('campaign').agg({
        'impressions': 'sum',
        'clicks': 'sum',
        'conversions': 'sum',
        'revenue': 'sum',
        'cost': 'sum',
        'ctr': 'mean',
        'cac': 'mean',
        'ltv': 'mean',
        'roi': 'mean'
    }).reset_index()
    
    # Save the enhanced dataset
    df.to_csv('data/tableau_marketing_data.csv', index=False)
    campaign_summary.to_csv('data/tableau_campaign_summary.csv', index=False)
    
    print("Tableau data preparation completed!")
    print(f"Enhanced dataset saved to: data/tableau_marketing_data.csv")
    print(f"Campaign summary saved to: data/tableau_campaign_summary.csv")

if __name__ == "__main__":
    prepare_tableau_data() 