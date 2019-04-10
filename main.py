# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:28:25 2019

@author: Sean
"""

from flask import Flask, render_template, request
import base64

from config import DevConfig
from crawler import MyWebCrawler

app = Flask(__name__)
app.config.from_object(DevConfig)

CRAWLER = MyWebCrawler()

WEB_DICT = {
    'pchomeStore': 'https://www.pcstore.com.tw/adm/psearch.htm?store_k_word={}&slt_k_option=1'
}


@app.route('/')
@app.route('/search/<web>/')
def index(web=None):
    if request.path == '/':
        return render_template('index.html', request=request, web_list=WEB_DICT.keys())

    else:
        query = request.query_string.decode('utf-8').split('=')[1]
        target = WEB_DICT.get(web)
        print(target)
        if target:
            web_to_crawl = target.format(base64.b64encode(query.encode('utf-8')).decode('utf-8'))
            CRAWLER(web_to_crawl, 'big5')
            title_list = CRAWLER.find_target('div', 'pic2t pic2t_bg')
            response = render_template('search.html', title_list=title_list)
        else:
            response = f'<script>alert(\'No this web in select\'); window.location=\'http://{request.host}/\'</script>'

        return response


if __name__ == '__main__':
    app.run()

