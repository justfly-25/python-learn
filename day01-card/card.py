print("="*7 + "BMI计算器" + "="*7)
姓名 = input("请输入你的姓名： ")
身高 = float(input("请输入你的身高(米) : "))
体重 = float(input("请输入你的体重(千克) : "))
BMI = 体重/ (身高*身高)
BMI = round(BMI,2)
print("="*10 + "结果" + "="*10)
print(f"姓名：{姓名}")
print(f"身高：{身高}")
print(f"BMI: {BMI}")
if BMI < 18.5:
    print(f"偏瘦")
elif BMI < 24:
    print(f"正常")
elif BMI <28:
    print(f"偏胖")
else:
    print(f"肥胖")

print("="*30)
