#!/usr/bin/env python
# -*- coding:utf-8 -*-


# demo test 
# https://www.cnblogs.com/melonjiang/p/6536876.html

from pymongo import MongoClient

''''
连接mongodb
'''
conn = MongoClient('10.211.240.69', 27017)
db = conn.mydb #连接mydb数据库，没有则自动创建
my_set = db.test_set #使用test_set集合，没有则自动创建


''' 
插入数据（insert插入一个列表多条数据不用遍历，效率高， save需要遍历列表，一个个插入）
'''
# my_set.insert({"name":"zhangsan1","age":18})
#或
#my_set.save({"name":"zhangsan2","age":18})

#添加多条数据到集合中
# users=[{"name":"zhangsan3","age":18},{"name":"lisi","age":20}]  
# my_set.insert(users) 
#或
# my_set.save(users) 

# 多级路径元素操作
# 　　先插入一条数据
# dic = {"name":"zhangsan",
#        "age":18,
#        "contact" : {
#            "email" : "1234567@qq.com",
#            "iphone" : "11223344"}
#        }
# my_set.insert(dic)


''''
查询数据（查询不到则返回None）
'''
#查询全部
for i in my_set.find():
    print(i)
#查询name=zhangsan的
'''
for i in my_set.find({"name":"zhangsan"}):
    print(i)
print(my_set.find_one({"name":"zhangsan"}))
'''


'''
my_set.update(
   <query>,    #查询条件
   <update>,    #update的对象和一些更新的操作符
   {
     upsert: <boolean>,    #如果不存在update的记录，是否插入
     multi: <boolean>,        #可选，mongodb 默认是false,只更新找到的第一条记录
     writeConcern: <document>    #可选，抛出异常的级别。
   }
)
'''
#把上面插入的数据内的age改为20
my_set.update({"name":"zhangsan3"},{'$set':{"age":20}})



'''
my_set.remove(
   <query>,    #（可选）删除的文档的条件
   {
     justOne: <boolean>,    #（可选）如果设为 true 或 1，则只删除一个文档
     writeConcern: <document>    #（可选）抛出异常的级别
   }
)
'''
'''
#删除name=lisi的全部记录
my_set.remove({'name': 'zhangsan'})

#删除name=lisi的某个id的记录
id = my_set.find_one({"name":"zhangsan"})["_id"]
my_set.remove(id)
'''
#删除集合里的所有记录
# my_set.remove()
