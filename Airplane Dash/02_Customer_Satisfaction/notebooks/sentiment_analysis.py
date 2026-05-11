# 02_Customer_Satisfaction/notebooks/sentiment_analysis.py
import pandas as pd
from textblob import TextBlob
import os

# Set paths
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, '../data/customer_reviews.csv')

# Load data
df = pd.read_csv(data_path)

# Sentiment Scoring
def get_sentiment_score(text):
    return TextBlob(text).sentiment.polarity

def get_sentiment_label(score):
    if score > 0: return 'Positive'
    elif score == 0: return 'Neutral'
    else: return 'Negative'

df['sentiment_score'] = df['review_text'].apply(get_sentiment_score)
df['sentiment_label'] = df['sentiment_score'].apply(get_sentiment_label)

# Calculate NPS (Proxy)
nps_score = ((df['overall_score'] >= 9).sum() - (df['overall_score'] <= 6).sum()) / len(df) * 100

print(f"--- Customer Satisfaction Analysis ---")
print(f"Total Reviews: {len(df)}")
print(f"Calculated NPS Score: {nps_score:.2f}")
print(f"Sentiment Breakdown:\n{df['sentiment_label'].value_counts(normalize=True) * 100}")

# Save for Power BI
output_path = os.path.join(base_dir, '../data/processed_reviews.csv')
df.to_csv(output_path, index=False)
print(f"\nProcessed data saved for Power BI at: {output_path}")
