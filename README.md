# Scrapy Sreality Scraper

This project scrapes the first 500 items (title and image URL) from sreality.cz (flats, sell) using Scrapy and saves them in a PostgreSQL database. It also implements a simple Python HTTP server to display these items on a web page.

### Installation and Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/Verix99/scrapy-sreality.git
    ```

2. Navigate to the project directory:

    ```bash
    cd sreality-scrapy
    ```

3. Run:

    ```bash
    docker-compose up
    ```

4. Open your web browser and go to [http://127.0.0.1:8080](http://127.0.0.1:8080) to view the scraped ads.
