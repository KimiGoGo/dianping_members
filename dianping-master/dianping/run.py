#-*- coding: utf-8 -*-
# 调试


from scrapy import cmdline


name = 'dianping'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())