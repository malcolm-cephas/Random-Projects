import pandas as pd
import numpy as np
import os

def generate_reviews(num_reviews=1000):
    np.random.seed(42)
    
    aspects = ['Inflight Wi-Fi', 'Seat Comfort', 'Food & Drink', 'Cabin Crew', 'Baggage Handling', 'Legroom']
    positive_comments = [
        "The cabin crew was amazing!", "Great legroom in economy.", "Wi-fi was fast and reliable.",
        "Loved the meal options.", "Smooth boarding process.", "Clean plane and friendly staff."
    ]
    negative_comments = [
        "The food was cold.", "No legroom at all.", "Wi-fi didn't work the whole flight.",
        "Rude staff at the gate.", "Lost my bags again.", "The seat wouldn't recline."
    ]
    
    data = []
    for _ in range(num_reviews):
        is_positive = np.random.random() > 0.4
        comment = np.random.choice(positive_comments if is_positive else negative_comments)
        score = np.random.randint(7, 11) if is_positive else np.random.randint(1, 6)
        
        data.append({
            'review_id': _,
            'review_text': comment,
            'overall_score': score,
            'travel_type': np.random.choice(['Business', 'Personal']),
            'customer_class': np.random.choice(['Economy', 'Business', 'Eco Plus'])
        })
        
    df = pd.DataFrame(data)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    df.to_csv(os.path.join(base_dir, 'customer_reviews.csv'), index=False)
    print(f"Generated {num_reviews} reviews in {base_dir}")

if __name__ == "__main__":
    generate_reviews()
