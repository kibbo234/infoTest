#! /usr/bin/env python
#-*- coding:utf-8 -*-

from influxdb import InfluxDBClient
client = InfluxDBClient('vargoo.com', 8086, 'root', 'liuxh', '') # 初始化
print (client.get_list_database()) # 显示所有数据库名称
client.create_database('testdb') # 创建数据库
print (client.get_list_database()) # 显示所有数据库名称
client.drop_database('testdb') # 删除数据库
print (client.get_list_database()) # 显示所有数据库名称

client = InfluxDBClient('vargoo.com', 8086, 'root', 'liuxh', 'testDB') # 初始化（指定要操作的数据库）
result = client.query('show measurements;')
print("Result:{0}".format(result))

json_body=[
    {
	"measurement":"students",
	"tags":{
		"stuid":"s123"
	},
	# "time":"1324234"
	"fields":{
		"score":89
	}
    }
]
client.write_points(json_body)
def showDBNames(client):
	result = client.query('show measurements;')
	print("Result:{0}".format(result);

