import streamlit as st
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt
from googletrans import Translator



# Initialize the sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
translator = Translator()

def translate_text(text):
    # Translate text to English
    translation = translator.translate(text, dest='en')
    return translation.text
# Streamlit app title
st.title("Twitter Sentiment Insights")

# Sidebar options for input methods
st.sidebar.header("Input Options")
input_method = st.sidebar.selectbox(
    "Choose input method:",
    ("Upload CSV file", "Enter tweets manually")
)

def analyze_sentiment_transformer(text):
    result = sentiment_analyzer(text)[0]
    
    # Map star ratings to sentiment categories
    # label = result['label']
    if result['label'] in ['1 star', '2 stars']:
        sentiment = 'NEGATIVE'
    elif result['label'] in ['4 stars', '5 stars']:
        sentiment = 'POSITIVE'
    else:
        sentiment = 'UNKNOWN'  # Handle unexpected labels
    
    return sentiment, result['score']
overall_scores = []
if input_method == "Upload CSV file":
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    if uploaded_file:
        # Load and display the dataset
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview", df.head())

        # Check if a specific column for tweets exists
        if "tweet" in df.columns:
            df['tweet'] = df['tweet'].apply(translate_text)
            df['Sentiment'], df['Score'] = zip(*df['tweet'].apply(analyze_sentiment_transformer))
            overall_scores.extend(df['Score'])
            st.write("Sentiment Analysis Results", df[['tweet', 'Sentiment', 'Score']])
        
        else:
            st.error("CSV file must contain a 'tweet' column.")
        sentiment_counts = df['Sentiment'].value_counts()

        # Display as Bar Chart
        st.subheader("Sentiment Distribution - Bar Chart")
        st.bar_chart(sentiment_counts)

        # Display as Pie Chart
        st.subheader("Sentiment Distribution - Pie Chart")
        fig, ax = plt.subplots()
        ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140, colors=['green', 'red', 'blue'])
        ax.axis("equal")  # Equal aspect ratio ensures the pie chart is circular
        st.pyplot(fig)
        # Determine the dominant sentiment
        # Determine the dominant sentiment
        total_tweets = sentiment_counts.sum()
        positive_count = sentiment_counts.get('POSITIVE', 0)
        negative_count = sentiment_counts.get('NEGATIVE', 0)
        neutral_count = sentiment_counts.get('NEUTRAL', 0)

        if positive_count > negative_count and positive_count > neutral_count:
            summary = "Overall Sentiment: The company's feedback on Twitter is largely positive."
        elif negative_count > positive_count and negative_count > neutral_count:
            summary = "Overall Sentiment: The company's feedback on Twitter is largely negative."
        elif neutral_count > positive_count and neutral_count > negative_count:
            summary = "Overall Sentiment: The company's feedback on Twitter is largely neutral."
        else:
            summary = "Overall Sentiment: The company's feedback on Twitter is mixed."

        # Display the summary
        st.subheader("Sentiment Summary")
        st.write(summary)

elif input_method == "Enter tweets manually":
    tweets_input = st.text_area("Enter tweets (one per line):")

    if st.button("Analyze Sentiment"):
        tweets = tweets_input.splitlines()
        results = {"Tweet": [], "Sentiment": [], "Score": []}

        for tweet in tweets:
            tweet = translate_text(tweet)
            sentiment, score = analyze_sentiment_transformer(tweet)
            results["Tweet"].append(tweet)
            results["Sentiment"].append(sentiment)
            results["Score"].append(score)

        # Display results as a DataFrame
        results_df = pd.DataFrame(results)
        st.write("Sentiment Analysis Results", results_df)


if overall_scores:
    overall_confidence = sum(overall_scores) / len(overall_scores)
    st.subheader("Overall Model Confidence")
    st.write(f"The overall confidence of the model on the given dataset is: **{overall_confidence:.2f}**")