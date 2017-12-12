import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

rss_feed = {
    'bbc':'http://feeds.bbci.co.uk/news/world/rss.xml',
    'cbn':'http://www.cbn.com/cbnnews/world/feed/'}

@app.route('/')
@app.route('/<publication>')

def get_news(publication='bbc'):
    feed = feedparser.parse(rss_feed[publication])
    #first_article = feed['entries'][0]
    return render_template('home.html',
                           articles=feed['entries']
                           )

if __name__ == '__main__':
    app.run(port=5000, debug=True)