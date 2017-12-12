import feedparser
from flask import Flask
app = Flask(__name__)

rss_feed = {
    'bbc':'http://feeds.bbci.co.uk/news/world/rss.xml',
    'cbn':'http://www.cbn.com/cbnnews/world/feed/'}

@app.route('/')
@app.route('/bbc')
def bbc():
    return get_news('bbc')

@app.route('/cbn')
def cbn():
    return get_news('cbn')

def get_news(source):
    feed = feedparser.parse(rss_feed[source])
    first_article = feed['entries'][0]
    return '''
    <html>
    <body>
    <h1>Headlines</h1>
    <b>{0}</b><br/>
    <i>{1}</i><br/>
    </body>
    </html>'''.format(first_article.get('title'),first_article.get('summary'), first_article.get('published'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)