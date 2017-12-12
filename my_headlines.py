import feedparser
from flask import Flask
app = Flask(__name__)

bbc_feed = 'http://feeds.bbci.co.uk/news/world/rss.xml'

@app.route('/')
def get_news():
    feed = feedparser.parse(bbc_feed)
    first_article = feed['entries'][0]
    return '''
    <html>
    <body>
    <h1>BBC Headlines</h1>
    <b>{0}</b><br/>
    </body>
    </html>'''.format(first_article.get('title'),first_article.get('summary'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)