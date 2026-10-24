import os
import feedparser
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# TOOL: fetch the news
def get_news():
    feed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
    items = feed.entries[:10]
    return "\n".join(f"- {e.title}: {e.get('summary', '')}" for e in items)

# GOAL + BRAIN: summarize the top 5
news = get_news()
prompt = "Pick the top 5 stories and summarize each in one simple sentence:\n" + news
response = client.models.generate_content(model="gemini-3.8-flash", contents=prompt)
print(response.text)