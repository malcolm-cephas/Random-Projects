import pandas as pd
import numpy as np
import os

def generate_profit_data(num_routes=50):
    np.random.seed(42)
    
    routes = [f"R{str(i).zfill(3)}" for i in range(num_routes)]
    data = []
    
    for route in routes:
        # Business logic: Longer routes have higher costs but higher revenue potential
        distance = np.random.randint(500, 5000)
        flights_per_month = np.random.randint(30, 90)
        avg_fare = np.random.randint(150, 600)
        load_factor = np.random.uniform(0.65, 0.95) # 65% to 95% full
        capacity = 180 # Standard narrowbody
        
        revenue = flights_per_month * capacity * load_factor * avg_fare
        
        # Costs
        fuel_cost = distance * 15 * flights_per_month # $15 per mile for fuel/ops
        crew_cost = flights_per_month * 5000 # Fixed per flight
        airport_fees = flights_per_month * 2000
        
        total_costs = fuel_cost + crew_cost + airport_fees
        
        data.append({
            'route_id': route,
            'distance': distance,
            'total_revenue': revenue,
            'total_costs': total_costs,
            'net_profit': revenue - total_costs,
            'margin_pct': ((revenue - total_costs) / revenue) * 100
        })
        
    df = pd.DataFrame(data)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    df.to_csv(os.path.join(base_dir, 'route_profitability.csv'), index=False)
    print(f"Generated {num_routes} route P&Ls in {base_dir}")

if __name__ == "__main__":
    generate_profit_data()
