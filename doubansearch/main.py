from scrapy import cmdline
cmdline.execute('scrapy crawl douban'.split())
#保存数据到文件，-S 编码
# cmdline.execute('scrapy crawl douban -o filename.json -s FEED_EXPORT_ENCODING=uft-8/...')