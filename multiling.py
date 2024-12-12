import pandas as pd

# Sample multilingual dataset with tweets in different Indian languages and their sentiment labels
data = {
    "tweet": [
        "मुझे यह उत्पाद पसंद है, यह अद्भुत है!",         # Hindi: Positive
        "यह सबसे खराब अनुभव है!",                       # Hindi: Negative
        "నేను ఈ ఉత్పత్తిని ప్రేమిస్తున్నాను!",             # Telugu: Positive
        "ఈ అనుభవం చాలా దిగజారుతుంది!",                 # Telugu: Negative
        "இந்த தயாரிப்பு மிகச் சிறந்தது!",                  # Tamil: Positive
        "என்னால் இதனை மீண்டும் வாங்க முடியாது, மோசமானது!",  # Tamil: Negative
        "আমি এই পণ্যটি পছন্দ করি!",                     # Bengali: Positive
        "এটি অত্যন্ত হতাশাজনক ছিল!",                   # Bengali: Negative
        "This product is fantastic!",                    # English: Positive
        "I would never buy this again, it's terrible!"   # English: Negative
    ]
}

# Convert data into a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("multilingual_tweets_dataset.csv", index=False)

print("Sample multilingual dataset 'multilingual_tweets_dataset.csv' created successfully.")
