import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def generate_airline_data(num_flights=10000):
    """
    Generates realistic synthetic flight data for portfolio projects.
    Includes time-of-day and day-of-week delay patterns.
    """
    np.random.seed(42)
    
    carriers = ['AA', 'DL', 'UA', 'WN', 'AS', 'B6']
    airports = ['JFK', 'LAX', 'ORD', 'DFW', 'ATL', 'SFO', 'SEA', 'MIA']
    
    data = []
    start_date = datetime(2024, 1, 1)
    
    for i in range(num_flights):
        # Random flight metadata
        date = start_date + timedelta(days=np.random.randint(0, 90))
        carrier = np.random.choice(carriers)
        origin = np.random.choice(airports)
        dest = np.random.choice([a for a in airports if a != origin])
        
        # Scheduled departure (random hour)
        sched_hour = np.random.randint(5, 23)
        sched_dep = datetime(date.year, date.month, date.day, sched_hour, np.random.randint(0, 60))
        
        # LOGIC: Late day flights and weekends have higher delay probability
        delay_prob = 0.2 + (sched_hour / 24) * 0.3 # Increases as day goes on
        if date.weekday() >= 5: # Weekend boost
            delay_prob += 0.1
            
        is_delayed = np.random.random() < delay_prob
        dep_delay = 0
        if is_delayed:
            # Exponential distribution for realistic delay lengths
            dep_delay = int(np.random.exponential(scale=30) + 5)
            
        # Arrival logic
        distance = np.random.randint(300, 3000)
        flight_time = int(distance / 8) + 30 # Simple speed estimate
        arr_delay = dep_delay + np.random.randint(-10, 15) # Some recovery or extra delay
        
        data.append({
            'flight_date': date.date(),
            'carrier': carrier,
            'origin_airport': origin,
            'dest_airport': dest,
            'scheduled_departure_time': sched_dep.strftime('%H:%M:%S'),
            'departure_delay': dep_delay,
            'arrival_delay': max(0, arr_delay),
            'distance': distance,
            'cancelled': np.random.random() < 0.02, # 2% cancellation rate
        })
        
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, 'flights_sample.csv')
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    print(f"Successfully generated {num_flights} flights in {output_path}")

if __name__ == "__main__":
    generate_airline_data()
