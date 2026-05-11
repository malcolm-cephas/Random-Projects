import pandas as pd
import numpy as np
import os

def generate_pricing_data(num_tickets=5000):
    np.random.seed(42)
    
    # Days to Departure (DTD)
    dtd = np.random.randint(1, 60, num_tickets)
    
    # Base price (influenced by duration/route)
    base_price = 200
    
    # Pricing logic: Price = Base + (Exp growth as DTD decreases) + randomness
    # This simulates real airline revenue management
    price = base_price + (1000 / (dtd + 1)) + np.random.normal(0, 50, num_tickets)
    
    df = pd.DataFrame({
        'ticket_id': range(num_tickets),
        'days_to_departure': dtd,
        'price': price.clip(min=150), # Minimum fare
        'is_weekend': np.random.choice([0, 1], num_tickets),
        'flight_duration_min': np.random.randint(60, 360, num_tickets)
    })
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    df.to_csv(os.path.join(base_dir, 'ticket_prices.csv'), index=False)
    print(f"Generated {num_tickets} tickets in {base_dir}")

if __name__ == "__main__":
    generate_pricing_data()
