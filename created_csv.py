import csv

# Define a list of tweets
tweets = [
    "Amazing service by AcmeCorp! Highly recommend their products. #satisfied",
    "AcmeCorp's new update is fantastic! Loving the new features.",
    "Customer support from AcmeCorp was top-notch! Problem solved quickly.",
    "Shoutout to AcmeCorp for their eco-friendly initiatives! Keep it up! #GoGreen",
    "Been using AcmeCorp's product for years, and it keeps getting better!",
    "Disappointed with AcmeCorp's latest product. Not up to the mark.",
    "Waited for over 30 minutes on hold with AcmeCorp's customer service. Not happy!",
    "The new update from AcmeCorp is full of bugs. Please fix ASAP!",
    "AcmeCorp used to be reliable, but their quality has dropped recently. #frustrated",
    "AcmeCorp's pricing is too high for the value they offer. Not worth it.",
    "AcmeCorp released a new product update today.",
    "Received an email from AcmeCorp about their latest promotions.",
    "Considering buying a product from AcmeCorp. Any recommendations?",
    "AcmeCorp has announced changes to their return policy.",
    "Just checked out AcmeCorp's website. Looks nice!"
]

# Specify the CSV file name
filename = "tweets_dataset.csv"

# Open the file in write mode
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["tweet"])
    # Write the tweets
    for tweet in tweets:
        writer.writerow([tweet])

print(f"CSV file '{filename}' created successfully with 10 tweet texts!")
