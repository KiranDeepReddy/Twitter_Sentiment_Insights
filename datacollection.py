import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def fetch_posts(topic, num_posts=100):
    base_url = f"https://x.com/home"  # Replace with a target website's search URL
    posts = []
    page = 1
    
    while len(posts) < num_posts:
        # Adjust the URL to reflect page numbers if necessary
        url = f"{base_url}&page={page}"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
            break
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Customize selectors based on the structure of the target website
        articles = soup.find_all("article", class_="post")
        
        for article in articles:
            if len(posts) >= num_posts:
                break
            
            # Get the headline or content; adapt the tag/class selectors based on site structure
            headline = article.find("h2").get_text(strip=True)
            link = article.find("a")["href"]
            content = article.find("p", class_="post-summary").get_text(strip=True)  # Modify as per site
            
            posts.append({
                "headline": headline,
                "content": content,
                "link": link
            })
        
        # Increment page counter and add delay to avoid hitting server too quickly
        page += 1
        time.sleep(2)  # Be cautious with request frequency
    
    return posts

# Fetch and save posts
topic = "AI technology"  # Replace with any specific topic you're interested in
data = fetch_posts(topic)

# Convert to DataFrame and save
df = pd.DataFrame(data)
df.to_csv("scraped_posts.csv", index=False)
print("Data saved to scraped_posts.csv")
