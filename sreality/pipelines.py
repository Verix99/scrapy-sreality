from itemadapter import ItemAdapter
import psycopg2

class SrealityPipeline:
    
    def __init__(self):
        # Data pro připojení k databázi
        hostname = 'db'
        username = 'postgres'
        password = '123456' 
        port = '5432'
        database = 'postgres'

        # Připojení k databázi a získání dat
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port)
        self.cur = self.connection.cursor()
        # Vyvtoření tabulky, když neexistuje
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS flat(
            id serial PRIMARY KEY,
            title text,
            imgs text
        )
        """)
        # Smazání všech  dat z tabulky
        self.cur.execute("""
        DELETE FROM flat *
        """)

    def process_item(self, item, spider):
        # Vloží nový záznam do tabulky
        self.cur.execute(""" insert into flat (title, imgs) values (%s,%s)""", (
            item["title"],
            item["imgs"]
        ))
        # Aktualizuje databázi a vrací položku
        self.connection.commit()
        return item

    def close_spider(self, spider):
        #Ukončení cursoru a kontaktu s databzí
        self.cur.close()
        self.connection.close()
