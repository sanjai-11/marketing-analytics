import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

def load_data():
    return pd.read_csv('data/marketing_metrics.csv')

def calculate_roi(df):
    """Calculate ROI for each campaign"""
    roi = df.groupby('campaign').apply(
        lambda x: (x['revenue'].sum() - x['cost'].sum()) / x['cost'].sum() * 100
    ).reset_index()
    roi.columns = ['campaign', 'roi']
    return roi

def calculate_weekly_metrics(df):
    """Calculate weekly aggregated metrics"""
    df['date'] = pd.to_datetime(df['date'])
    df['week'] = df['date'].dt.isocalendar().week
    
    weekly_metrics = df.groupby(['campaign', 'week']).agg({
        'impressions': 'sum',
        'clicks': 'sum',
        'conversions': 'sum',
        'revenue': 'sum',
        'cost': 'sum'
    }).reset_index()
    
    weekly_metrics['ctr'] = weekly_metrics['clicks'] / weekly_metrics['impressions']
    weekly_metrics['cac'] = weekly_metrics['cost'] / weekly_metrics['conversions']
    weekly_metrics['ltv'] = weekly_metrics['revenue'] / weekly_metrics['conversions']
    
    return weekly_metrics

def create_metric_visualizations(df, weekly_metrics):
    """Create visualizations for key metrics"""
    # Set style
    plt.style.use('seaborn')
    
    # 1. ROI by Campaign
    roi = calculate_roi(df)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='campaign', y='roi', data=roi)
    plt.title('ROI by Campaign')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('analysis/roi_by_campaign.png')
    plt.close()
    
    # 2. Weekly Trends
    metrics = ['ctr', 'cac', 'ltv']
    for metric in metrics:
        plt.figure(figsize=(15, 6))
        for campaign in weekly_metrics['campaign'].unique():
            campaign_data = weekly_metrics[weekly_metrics['campaign'] == campaign]
            plt.plot(campaign_data['week'], campaign_data[metric], label=campaign, marker='o')
        
        plt.title(f'{metric.upper()} Weekly Trends')
        plt.xlabel('Week')
        plt.ylabel(metric.upper())
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f'analysis/{metric}_weekly_trends.png')
        plt.close()
    
    # 3. Correlation Heatmap
    correlation_metrics = ['impressions', 'clicks', 'conversions', 'revenue', 'cost', 'ctr', 'cac', 'ltv']
    correlation_matrix = df[correlation_metrics].corr()
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Metrics Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('analysis/metrics_correlation.png')
    plt.close()

def generate_summary_report(df, weekly_metrics):
    """Generate a summary report of key metrics"""
    summary = {
        'Overall Metrics': {
            'Total Impressions': df['impressions'].sum(),
            'Total Clicks': df['clicks'].sum(),
            'Total Conversions': df['conversions'].sum(),
            'Total Revenue': df['revenue'].sum(),
            'Total Cost': df['cost'].sum(),
            'Average CTR': df['clicks'].sum() / df['impressions'].sum(),
            'Average CAC': df['cost'].sum() / df['conversions'].sum(),
            'Average LTV': df['revenue'].sum() / df['conversions'].sum()
        }
    }
    
    # Campaign-specific metrics
    campaign_metrics = df.groupby('campaign').agg({
        'impressions': 'sum',
        'clicks': 'sum',
        'conversions': 'sum',
        'revenue': 'sum',
        'cost': 'sum'
    })
    
    campaign_metrics['ctr'] = campaign_metrics['clicks'] / campaign_metrics['impressions']
    campaign_metrics['cac'] = campaign_metrics['cost'] / campaign_metrics['conversions']
    campaign_metrics['ltv'] = campaign_metrics['revenue'] / campaign_metrics['conversions']
    
    summary['Campaign Metrics'] = campaign_metrics.to_dict()
    
    # Save summary to CSV
    pd.DataFrame(summary['Overall Metrics'], index=[0]).to_csv('analysis/overall_metrics.csv', index=False)
    campaign_metrics.to_csv('analysis/campaign_metrics.csv')
    
    return summary

def main():
    # Load data
    df = load_data()
    
    # Calculate weekly metrics
    weekly_metrics = calculate_weekly_metrics(df)
    
    # Create visualizations
    create_metric_visualizations(df, weekly_metrics)
    
    # Generate summary report
    summary = generate_summary_report(df, weekly_metrics)
    
    # Print key findings
    print("\nKey Marketing Metrics Summary:")
    print("------------------------------")
    for metric, value in summary['Overall Metrics'].items():
        print(f"{metric}: {value:,.2f}")

if __name__ == "__main__":
    main() 