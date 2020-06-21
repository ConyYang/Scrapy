# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# Scraped Data -> Item Containers -> Json/Csv files
# Scraped Data -> Item Containers -> Pipeline ->SQL/Mongo Databases
import sqlite3


class QuotePipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connection = sqlite3.connect("myquotes.db")
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS quotes """)
        self.cursor.execute("""create table quotes(
                                title text,
                                author text,
                                tag text
                                )""")

    def process_item(self, item, spider):
        self.store_db(item)

        print("Pipeline: : " + item['title'][0])
        return item

    def store_db(self, item):
        self.cursor.execute("""insert into quotes values (?,?,?)""",
            (
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.connection.commit()
