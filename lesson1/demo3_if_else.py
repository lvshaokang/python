'''
if条件判断
'''
'''
如果 条件成立:
	做某事
否则:
	做其他事情

if sth == True:
	do sth
else:
	do other
'''
'''
#单条件判断
age = input("请输入你的年龄：")
age_int = int(age) #类型转换
if age_int < 18:
	print("不向未成年人销售烟酒，请买块糖吧！")
else:
 	print("年龄合法，请付款！")

print("欢迎下次光临！")
'''
#多条件判断
'''
age = input("请输入你的年龄：")
age_int = int(age) #类型转换
if age_int < 16:
	print("不向未成年人销售烟酒，请买块糖吧！")
elif age_int < 18:
	print("小于16岁")
elif age_int == 18:
	print("恭喜你年满18")
else:
	print("年龄合法，请付款！")

print("欢迎下次光临！")
'''
#嵌套判断
fee = input("请缴费50：")
fee_int = int(fee)
if fee_int == 50:
	print("缴费成功！")
	gender = input("请输入性别：b男性，g女性：")
	if gender == "b":
		print("请排在男生队伍")
	elif gender == "g":
		print("请排在女生队伍")
else:
	print("对不起，金额不足！")