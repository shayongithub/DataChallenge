import scrapy
from diemthi.items import DiemthiItem
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logzero import logfile, logger
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import json
import loguru
from lxml import etree
import glob
import shutil
import os

BROWSER_EXE = 'C:/Users/This PC/AppData/Local/Mozilla Firefox/firefox.exe'
GECKODRIVER = 'F:\Python\Data1\Assignment 1\cryptocurrency\geckodriver.exe'
FIREFOX_BINARY = FirefoxBinary(BROWSER_EXE)

class CrawldiemthiSpider(scrapy.Spider):
    name = 'crawldiemthi'
    allowed_domains = ['diemthi.hcm.edu.vn/']
    start_urls = ['http://diemthi.hcm.edu.vn/?fbclid=IwAR2tNCgz2xTIytLIVNX_V4lDMb3Hhq_6qu2Si7r8TeLgeLkfWCNHAfUH32M']
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            #"diemthi.middlewares.RotateProxyMiddleware": 300,  # Unhealthy proxy give timeout exception sometimes
            "diemthi.middlewares.RotateAgentMiddleware": 301,
            "diemthi.middlewares.DiemthiMiddleware": 302
        },
        "ITEM_PIPELINES": {
            "diemthi.pipelines.DiemthiPipeline": 300
        }
    }

    def parse(self, response):
        items = DiemthiItem()

        for i in json.loads(response.body):
            data = etree.HTML(i)
            table = data.xpath("//div[1]/table/tbody/tr[2]")

            for line in table:
                items["A_HO_VA_TEN"] = line.xpath(".//td[1]/text()")[0].strip()
                items["B_NGAY_SINH"] = line.xpath(".//td[2]/text()")[0].strip()
                items["C_DIEM_THI"] = line.xpath(".//td[3]/text()")[0].strip()

                yield items

        pass
