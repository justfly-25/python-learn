scores ={
    "张三": 88,
    "李四": 92,
    "王五": 77,
    "江菲": 100,
}

print("="*40)
print("  学生成绩管理系统")
print("="*40)

def show_all():
    if len(scores) == 0:
        print("当前还没有学生数据")
        return
    
    print("\n学生成绩列表")
for name, score in scores.items():
    if score >= 90:
        emoji = "😘"
    elif score >= 80:
        emoji = "👍"
    else:
        emoji = "😒"
    print(f"  {name}: {score}分 {emoji}")

def add_student():
    name = input("请输入学生的姓名： ").strip()
    if not name:
        print("姓名不能为空")
        return
    if name in scores:
        print("该学生已经存在了!")
        return
    try:
        score = int(input("请输入{name}的成绩(0-100): "))
        if score < 0 and score > 100:
            print("成绩必须在0-100之间")
            return
    except ValueError:
        print("请输入数字!")
        return
    scores[name]= score
    print(f"已添加： {学生}:{score}分")

