
text="<div class='houseInfo'><a href='https://bj.lianjia.com/xiaoqu/1111027378138/' " \
     "target='_blank' data-log_index='1' data-el='region'>流星花园三区 " \
     "</a><span class='divide'>/</span>4室2厅<span class='divide'>/</span>" \
     "118.32平米<span class='divide'>/</span>南 西 北<span class='divide'>/</span>" \
     "精装<span class='divide'>/</span>有电梯</div>"



#content=text.xpath("//div[@class='houseInfo']/text()")


# 有问题的写法
dicttest = {'one':'1','one':'2','one':3,'two':'22','three':'33'}
# 正确的写法 ： key 不能重复，最后的key会覆盖前面的key ，value 可以重复
dicttest =  {'one': 3, 'two': '22', 'three': '33'}
# print(dicttest.values())
# print(dicttest.keys())

# 遍历字典项
# for keys,values in dicttest.items():
#      # print(keys)
#      # print(values)

#  遍历字典项
# for kv in dicttest.items():
#      print(kv)
#
#
# # 获取key值
# for kv in dicttest:
#      print(kv)
#      print(dicttest[kv])
#
# for kv in dicttest.values():
#      print(kv)
#
# print(dicttest)
#
# dicttest =  {'one': [3,4,5,6,7,8], 'two': '22', 'three': '33'}
#
# for k in dicttest:
#      print(dicttest[k][:2])

dicttest =  {'one': {3,4,5,6,7,8}}
#
for k in dicttest:
    print(dicttest[k])
