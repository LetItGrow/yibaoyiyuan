# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

from scrapy.exceptions import DropItem

class DuplicatesPipeline ( object ):
    def __init__ ( self ):
        self.ids_seen = [ ]

    def process_item ( self , item , spider ):
        if item[ 'url' ] in self.ids_seen:
            raise DropItem ( "Duplicate item found: %s" % item )
        else:
            self.ids_seen.append ( item[ 'url' ] )
            return item


class JsonWriterPipeline ( object ):
    def __init__ ( self ):
        self.file = open ( 'data2.json' , 'ab')

    def process_item ( self , item , spider ):
        line = json.dumps ( dict ( item ),ensure_ascii=False)  + "\n"
        self.file.write (line)
        return item
