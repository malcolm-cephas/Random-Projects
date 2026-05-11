import pandas as pd
import numpy as np
import os

def generate_demand_data(years=5):
    np.random.seed(42)
    
    # Generate dates
    dates = pd.date_range(start='2019-01-01', periods=years*12, freq='M')
    
    # Components of demand
    base_demand = 100000
    growth_trend = np.linspace(0, 50000, len(dates)) # Long term growth
    
    # Seasonality (Sin wave)
    seasonality = np.sin(np.linspace(0, 2*np.pi*years, len(dates))) * 20000
    
    # Noise
    noise = np.random.normal(0, 5000, len(dates))
    
    passengers = base_demand + growth_trend + seasonality + noise
    
    df = pd.DataFrame({
        'month': dates,
        'passengers': passengers.astype(int)
    })
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    df.to_csv(os.path.join(base_dir, 'historical_demand.csv'), index=False)
    print(f"Generated demand data for {years} years in {base_dir}")

if __name__ == "__main__":
    generate_demand_data()
