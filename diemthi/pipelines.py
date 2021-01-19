# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter
from diemthi.middlewares import DiemthiMiddleware
import os
import glob
import shutil
import loguru

class DiemthiPipeline():
    def __init__(self, file_name):
        self.file = open("diemthi/diemthi.csv", "wb")
        self.exporter = CsvItemExporter(self.file)

    @classmethod
    def from_crawler(cls, crawler):
        file_name = getattr(crawler.spider, "name")
        return cls(file_name)

    def open_spider(self, spider):
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

        source = r'diemthi/diemthi.csv'
        destination = r'csv'
        shutil.move(source, destination)
        loguru.logger.info('Move the crawled file to csv file successfully ')
