# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DiemthiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    A_HO_VA_TEN = scrapy.Field()
    B_NGAY_SINH= scrapy.Field()
    C_DIEM_THI = scrapy.Field()

    pass
