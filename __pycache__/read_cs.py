import pandas as pd

# Specify the path to your Excel or csv  file
excel_file_path = r'C:\Users\arunv\Downloads\user_review.xls'


df = pd.read_excel(excel_file_path)

# Remove null values
df.dropna(inplace=True)

# Assuming 'review' is the column with the text data
# Remove unnecessary columns
df = df[['review']]

print(df)


import string

# Convert to lowercase
df['review'] = df['review'].str.lower()

# Remove punctuation
df['review'] = df['review'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))

print(df)


from textblob import TextBlob

# Function to perform sentiment analysis
def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Apply sentiment analysis to each review
df['sentiment'] = df['review'].apply(get_sentiment)

print(df)


# Function to categorize sentiments
def categorize_sentiment(polarity):
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'

# Apply sentiment categorization
df['sentiment_category'] = df['sentiment'].apply(categorize_sentiment)

# Generate summary report
summary = df['sentiment_category'].value_counts()

# Print summary report
print(summary)
print(df)

