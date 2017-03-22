# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from  scrapy.item import Item, Field





class FoodieItem(Item):

    nickname = Field()
    comment_num = Field()
    comment_first = Field()
    comment_response = Field()
    flower = Field()
    level = Field()
    location = Field()
    gender = Field()
    rank = Field()
    contribution = Field()

    loc_check= Field()
    collect_num = Field()
    pic_num = Field()
    note_num = Field()
    reg_time = Field()
    fans = Field()
    interaction = Field()
    tags = Field()
    shops = Field() # 收藏店铺

    birthPlace = Field()

    shape = Field()
    love_situation = Field() #恋爱状况
    birthday = Field()
    movie = Field()
    music = Field()
    book = Field()
    occupation = Field()
    college = Field()
    hobby = Field()
    foodtype = Field()
    star_sign = Field()
    url = Field()#星座

#
#
# class reviewItem(Item):
#     type = Field()
#     city = Field()
