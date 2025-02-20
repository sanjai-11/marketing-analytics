import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    return pd.read_csv('data/marketing_metrics.csv')

def perform_ab_test(df, metric='ctr', confidence_level=0.95):
    """
    Perform A/B testing on the specified metric between campaigns
    """
    # Group data by campaign and calculate mean and standard error
    campaign_stats = df.groupby('campaign')[metric].agg(['mean', 'std', 'count'])
    campaign_stats['std_err'] = campaign_stats['std'] / np.sqrt(campaign_stats['count'])
    
    # Perform t-test between each pair of campaigns
    results = []
    campaigns = campaign_stats.index.tolist()
    
    for i in range(len(campaigns)):
        for j in range(i+1, len(campaigns)):
            camp1, camp2 = campaigns[i], campaigns[j]
            
            # Get data for both campaigns
            data1 = df[df['campaign'] == camp1][metric]
            data2 = df[df['campaign'] == camp2][metric]
            
            # Perform t-test
            t_stat, p_value = stats.ttest_ind(data1, data2)
            
            # Calculate effect size
            effect_size = (data2.mean() - data1.mean()) / data1.mean() * 100
            
            results.append({
                'Campaign_A': camp1,
                'Campaign_B': camp2,
                'Metric': metric,
                'P_Value': p_value,
                'Significant': p_value < (1 - confidence_level),
                'Effect_Size_Percent': effect_size
            })
    
    return pd.DataFrame(results)

def visualize_ab_test_results(df, metric='ctr'):
    """
    Create visualizations for A/B test results
    """
    plt.figure(figsize=(12, 6))
    
    # Create box plot
    sns.boxplot(x='campaign', y=metric, data=df)
    plt.title(f'{metric.upper()} Distribution by Campaign')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'analysis/ab_test_{metric}_boxplot.png')
    plt.close()
    
    # Create time series plot
    plt.figure(figsize=(15, 6))
    for campaign in df['campaign'].unique():
        campaign_data = df[df['campaign'] == campaign]
        plt.plot(campaign_data['date'], campaign_data[metric], label=campaign)
    
    plt.title(f'{metric.upper()} Over Time by Campaign')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'analysis/ab_test_{metric}_timeseries.png')
    plt.close()

def main():
    # Load data
    df = load_data()
    
    # Perform A/B tests for different metrics
    metrics = ['ctr', 'cac', 'ltv']
    all_results = []
    
    for metric in metrics:
        results = perform_ab_test(df, metric)
        all_results.append(results)
        
        # Create visualizations
        visualize_ab_test_results(df, metric)
    
    # Combine all results
    final_results = pd.concat(all_results, ignore_index=True)
    final_results.to_csv('analysis/ab_test_results.csv', index=False)
    
    # Print summary of significant findings
    significant_results = final_results[final_results['Significant']]
    print("\nSignificant A/B Test Results:")
    print(significant_results[['Campaign_A', 'Campaign_B', 'Metric', 'Effect_Size_Percent']])

if __name__ == "__main__":
    main() 