# Marketing Analytics Dashboard

A comprehensive marketing analytics project that demonstrates data analysis, visualization, and A/B testing capabilities for marketing campaign optimization.

## Project Overview

This project implements a complete marketing analytics solution that:
- Generates synthetic marketing data
- Performs A/B testing on marketing campaigns
- Calculates key marketing metrics (CAC, LTV, CTR)
- Creates data visualizations
- Provides insights for campaign optimization

## Key Features

1. **Data Generation**
   - Synthetic marketing data generation with realistic patterns
   - Multiple campaigns with varying performance
   - Seasonal effects and campaign-specific multipliers

2. **A/B Testing Analysis**
   - Statistical significance testing between campaigns
   - Effect size calculations
   - Visualization of test results
   - Automated reporting of significant findings

3. **Key Metrics Analysis**
   - Customer Acquisition Cost (CAC)
   - Customer Lifetime Value (LTV)
   - Click-Through Rate (CTR)
   - Return on Investment (ROI)
   - Weekly trend analysis
   - Campaign performance comparison

4. **Visualizations**
   - ROI by campaign
   - Weekly metric trends
   - Correlation heatmaps
   - A/B test result visualizations

## Project Structure

```
marketing-analytics/
├── data/
│   ├── generate_data.py
│   └── marketing_metrics.csv
├── analysis/
│   ├── ab_testing.py
│   ├── metrics_analysis.py
│   └── visualizations/
├── requirements.txt
└── README.md
```

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/marketing-analytics.git
cd marketing-analytics
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Generate the data:
```bash
python data/generate_data.py
```

4. Run the analysis:
```bash
python analysis/metrics_analysis.py
python analysis/ab_testing.py
```

## Usage

1. **Generate Data**
   - Run `generate_data.py` to create synthetic marketing data
   - Data will be saved in `data/marketing_metrics.csv`

2. **Run Analysis**
   - Execute `metrics_analysis.py` for key metrics analysis
   - Run `ab_testing.py` for A/B testing analysis
   - Results and visualizations will be saved in the `analysis` directory

3. **View Results**
   - Check the generated CSV files in the `analysis` directory
   - View visualizations in the `analysis/visualizations` directory

## Key Metrics

- **CAC (Customer Acquisition Cost)**: Cost per conversion
- **LTV (Customer Lifetime Value)**: Revenue per conversion
- **CTR (Click-Through Rate)**: Clicks per impression
- **ROI (Return on Investment)**: (Revenue - Cost) / Cost

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.