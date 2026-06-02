scores ={
    "海绵宝宝": 88,
    "喜羊羊": 92,
    "光头强": 77,
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
        score = int(input(f"请输入{name}的成绩(0-100): "))
        if score < 0 or score > 100:
            print("成绩必须在0-100之间")
            return
    except ValueError:
        print("请输入数字!")
        return
    scores[name]= score
    print(f"已添加： {name}:{score}分")

def remove_student():
        show_all()
        name = input("请输入要删除学生的姓名")
        if scores.get(name) is None:
            print(f"不存在学生{name}")
            return
        
        removed_score = scores.pop(name)
        print(f"已删除：{name} {removed_score}分")

def  query_student():
    if len(scores) == 0:
        print("当前没有学生的信息")
        return
    all_scores = list(scores.values())
    total = sum(all_scores)
    average = total / len(all_scores)
    lowest = min(all_scores)
    higest = max(all_scores)
    
    passed = sum(1 for score in all_scores if score >=60)
    passed_rate = passed / len(all_scores)*100
    
    top_students = [name for name, sc in scores.items() if sc == higest]
    low_students = [name for name, sc in scores.items() if sc == lowest]

    print(f"平均分：{average:.1f}")
    print(f"学生总数：{len(all_scores)}")
    print(f"最高分：{higest}分, 学生： ({', '.join(top_students)})")
    print(f"最低分：{lowest}分, 学生： ({', '.join(low_students)})")
    print(f"及格率： {passed_rate:.1f}%")
    print("="*40)

def demo_set():
   print(f"\n===集合小课堂===")
   classmateA = {"111","222","333"}
   classmateB = {"222","333","444"}
   print(f"A班级同学: {classmateA}")
   print(f"B班级同学: {classmateB}")
   both =classmateA.intersection(classmateB)
   print(f"两个班级都有的同学: {both}")
   all_students = classmateA | classmateB
   print(f"所有课程：{all_students}")

   raw_list = [1, 2, 3, 4, 1, 2, 5]
   unique_set = set(raw_list)
   print(f"\n演示")
   print(f"原始： {raw_list}")
   print(f"去除后： {unique_set}")

while True:
    print("\n1. 查看所有学生成绩")
    print("2. 添加学生成绩")
    print("3. 删除学生成绩")
    print("4. 查询学生成绩")
    print("5. 退出系统")
    print("6. 集合小课堂")
    choice = input("请输入选项： ")
    if choice == "1":
        show_all()
    elif choice == "2":
        add_student()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        query_student()
    elif choice == "5":
        print("再见！")
        break
    elif choice == "6":
        demo_set()
    else:
        print("无效数字,请重新输入!")

                 

