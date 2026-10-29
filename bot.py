import os
import feedparser
import tweepy

# سحب المفاتيح بأمان من أسرار غيت هب
CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

# إعدادات عميل تويتر
client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
)

# مصادر الأخبار
FEEDS = {
    "أخبار عامة وانتقالات": "http://feeds.bbci.co.uk/sport/football/rss.xml",
    "فانتزي": "https://www.fantasyfootballscout.co.uk/feed/"
}

def fetch_and_tweet():
    try:
        for category, url in FEEDS.items():
            news_feed = feedparser.parse(url)
            if news_feed.entries:
                latest = news_feed.entries[0]
                title = latest.title
                link = latest.link
                break 

        tweet_text = (
            f"🚨 عاجل وحصري !\n\n"
            f"{title}\n\n"
            f"🔗 التفاصيل والقصة كاملة:\n{link}\n\n"
            f"#فانتزي_الدوري_الممتاز #انتقالات #كرة_قدم"
        )

        client.create_tweet(text=tweet_text)
        print("تم نشر التغريدة المتكاملة بنجاح")

    except Exception as e:
        print(f"حدث خطأ أثناء النشر: {e}")

if __name__ == "__main__":
    fetch_and_tweet()
