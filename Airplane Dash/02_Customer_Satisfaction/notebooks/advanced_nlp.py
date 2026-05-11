# 02_Customer_Satisfaction/notebooks/advanced_nlp.py
import pandas as pd
import nltk
from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# Initialize NLTK
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Set paths
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, '../data/customer_reviews.csv')
output_dir = os.path.join(base_dir, '../power_bi/')

# Load data
df = pd.read_csv(data_path)

# Filter for NEGATIVE reviews only (This is where the money is saved!)
negative_reviews = df[df['overall_score'] <= 5]['review_text']

# Tokenize and clean
all_words = []
for review in negative_reviews:
    words = review.lower().split()
    words = [w for w in words if w.isalpha() and w not in stop_words]
    all_words.extend(words)

# Top 10 Keywords
top_keywords = Counter(all_words).most_common(10)
print("\nTop 10 Passenger Pain Points:")
for word, freq in top_keywords:
    print(f"{word}: {freq}")

# Generate WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(all_words))
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Negative Review Word Cloud (Area for Improvement)')
plt.savefig(os.path.join(output_dir, 'pain_points_wordcloud.png'))

print(f"\nWordCloud saved to {output_dir}")
