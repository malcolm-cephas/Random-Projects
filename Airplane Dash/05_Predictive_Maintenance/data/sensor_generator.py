import pandas as pd
import numpy as np
import os

def generate_sensor_data(num_engines=10):
    np.random.seed(42)
    data = []
    
    for engine_id in range(1, num_engines + 1):
        # Each engine lasts between 150 and 300 cycles
        max_cycles = np.random.randint(150, 301)
        
        for cycle in range(1, max_cycles + 1):
            # Simulate sensor drift (e.g., temperature increases over time)
            base_temp = 500
            drift = (cycle / max_cycles) * 50 # Temp rises by 50 degrees near failure
            temp = base_temp + drift + np.random.normal(0, 2)
            
            # Simulated vibration (increases exponentially near end)
            vibration = 0.01 + (cycle / max_cycles)**2 * 0.5 + np.random.normal(0, 0.05)
            
            data.append({
                'engine_id': engine_id,
                'cycle': cycle,
                'temperature': temp,
                'vibration': vibration,
                'rul': max_cycles - cycle # Remaining Useful Life
            })
            
    df = pd.DataFrame(data)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    df.to_csv(os.path.join(base_dir, 'engine_sensors.csv'), index=False)
    print(f"Generated sensor data for {num_engines} engines in {base_dir}")

if __name__ == "__main__":
    generate_sensor_data()
