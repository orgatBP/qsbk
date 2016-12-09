# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#from qsbkquto.qsbkspd
    import MySQLdb
    import time

    class QsbkautoPipeline(object):
        def exeSQL(self,sql):
            '''
            功能：连接MySQL数据库并执行sql语句
            @sql：定义SQL语句
            '''
            con = MySQLdb.connect(
                host='localhost',  # port
                user='root',       # usr_name
                passwd='1104',     # passname
                db='spdRet',       # db_name
                charset='utf8',
                local_infile = 1
                )
            con.query(sql)
            con.commit()
            con.close()

        def process_item(self, item, spider):
            link_url = item['link'][0]
            content_header = item['content'][0][0:10]
            curr_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            content_header = curr_date+'__'+content_header
            if (len(link_url) and len(content_header)):#判断是否为空值
                try:
                    sql="insert into qiushi(content,link) values('"+content_header+"','"+link_url+"')"
                    self.exeSQL(sql)
                except Exception as er:
                    print("插入错误，错误如下：")
                    print(er)
            else:
                pass
            return item


