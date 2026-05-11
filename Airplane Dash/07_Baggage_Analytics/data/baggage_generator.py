import pandas as pd
import numpy as np
import os

def generate_baggage_data(num_bags=5000):
    np.random.seed(42)
    
    airports = ['JFK', 'LAX', 'ORD', 'ATL', 'LHR', 'DXB']
    data = []
    
    for bag_id in range(num_bags):
        origin = np.random.choice(airports)
        dest = np.random.choice([a for a in airports if a != origin])
        
        # Stages: Check-in -> Sorting -> Loading -> Arrival
        # A bag can fail at any stage
        is_mishandled = np.random.random() < 0.05 # 5% fail rate
        
        failure_point = None
        if is_mishandled:
            failure_point = np.random.choice(['Sorting', 'Loading', 'Transfer'])
            
        data.append({
            'bag_id': f"BAG{str(bag_id).zfill(5)}",
            'origin': origin,
            'destination': dest,
            'is_mishandled': is_mishandled,
            'failure_point': failure_point,
            'processing_time_min': np.random.randint(20, 120)
        })
        
    df = pd.DataFrame(data)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    df.to_csv(os.path.join(base_dir, 'baggage_flow.csv'), index=False)
    print(f"Generated baggage data for {num_bags} bags in {base_dir}")

if __name__ == "__main__":
    generate_baggage_data()
