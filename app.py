from flask import Flask, render_template, request
import psycopg2
from multiprocessing import Process, Queue
from scrapy.crawler import CrawlerProcess
from sreality.spiders.flatspider import FlatSpider
from scrapy.utils.project import get_project_settings
import os

app = Flask(__name__)

#asynchronní spuštění spideru
def f(q):
    try:
        settings = get_project_settings()
        process = CrawlerProcess(settings)
        process.crawl(FlatSpider)
        process.start()
        q.put(None)
    except Exception as e:
        q.put(e)

def run_spider():
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    result = q.get()
    p.join()

    if result is not None:
        raise result

@app.route('/')
def index():
    if request.method == 'GET':
        run_spider()

    # Data pro připojení k databázi
    hostname = 'db'
    username = 'postgres'
    password = '123456'
    port = '5432'
    database = 'postgres'

    # Připojení k databázi a získání dat
    connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port)
    cur = connection.cursor()
    cur.execute("SELECT to_json(flat) FROM flat")
    flat_records = cur.fetchall()
    cur.close()
    connection.close()

    # Zobrazí stránku s daty
    return render_template('index.html', data=flat_records)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)