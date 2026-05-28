"""
Day 4 — 简易学生成绩系统
知识点：
    1. dict 字典 —— 键值对存储，用花括号 {} 创建
    2. set 集合   —— 去重、集合运算（交集/并集）
    3. 字典的增删改查 —— .get() / del / in / .keys() / .values() / .items()
    4. 遍历字典    —— for key, value in dict.items()
"""

# ====== 第一步：初始化数据 ======
# 用字典存储学生姓名和成绩，格式: {名字: 分数}
scores = {
    "张三": 85,
    "李四": 92,
    "王五": 78,
    "赵六": 96,
}

print("=" * 40)
print("   学生成绩管理系统")
print("=" * 40)

# ====== 第二步：定义各功能函数 ======

def show_all():
    """查看所有学生的成绩"""
    if len(scores) == 0:
        print("暂无学生数据")
        return

    print("\n--- 学生成绩列表 ---")
    # .items() 返回 (键, 值) 的元组，可以同时遍历
    for name, score in scores.items():
        # 根据分数显示不同表情
        if score >= 90:
            emoji = "🌟"
        elif score >= 80:
            emoji = "✅"
        else:
            emoji = "💪"
        print(f"  {name}: {score}分 {emoji}")


def add_student():
    """添加一个新学生"""
    name = input("请输入学生姓名: ").strip()
    if not name:
        print("姓名不能为空！")
        return

    # 检查是否已存在（用 in 判断字典里有没有这个键）
    if name in scores:
        print(f"⚠️ 学生 '{name}' 已存在，当前成绩: {scores[name]}分")
        return

    try:
        score = int(input(f"请输入 {name} 的成绩 (0-100): "))
        if score < 0 or score > 100:
            print("成绩必须在 0~100 之间！")
            return
    except ValueError:
        print("请输入数字！")
        return

    scores[name] = score  # 字典添加元素：dict[key] = value
    print(f"✅ 已添加: {name} - {score}分")


def remove_student():
    """删除一个学生"""
    show_all()
    if not scores:
        return

    name = input("\n输入要删除的学生姓名: ").strip()

    # 用 .get() 安全取值，不会报错（找不到返回 None）
    if scores.get(name) is None:
        print(f"❌ 找不到学生 '{name}'")
        return

    # 方法一：del 删除（直接删，找不到会报错）
    # del scores[name]

    # 方法二：pop() 删除（推荐，还能拿到被删除的值）
    removed_score = scores.pop(name)
    print(f"✅ 已删除: {name} ({removed_score}分)")


def query_stats():
    """查询统计信息：平均分、最高分、最低分、及格率"""
    if len(scores) == 0:
        print("暂无数据可统计")
        return

    all_scores = list(scores.values())       # 把所有成绩提取成列表
    total = sum(all_scores)                  # 求和
    avg = total / len(all_scores)            # 平均分
    highest = max(all_scores)                # 最高分
    lowest = min(all_scores)                 # 最低分

    # 及格人数：用 sum + 生成器表达式统计 >= 60 的数量
    passed = sum(1 for s in all_scores if s >= 60)
    pass_rate = passed / len(all_scores) * 100  # 及格率(%)

    # 找出最高分和最低分的学生（可能有多个！）
    # 列表推导式 + 条件筛选
    top_students = [name for name, sc in scores.items() if sc == highest]
    bottom_students = [name for name, sc in scores.items() if sc == lowest]

    print("\n" + "-" * 30)
    print(f"  学生总数: {len(scores)} 人")
    print(f"  平均分:   {avg:.1f} 分")          # :.1f 保留1位小数
    print(f"  最高分:   {highest} 分 ({', '.join(top_students)})")
    print(f"  最低分:   {lowest} 分 ({', '.join(bottom_students)})")
    print(f"  及格率:   {pass_rate:.1f}%")
    print("-" * 30)


def demo_set():
    """演示 set 集合的用法（去重 & 运算）"""
    print("\n=== 集合小课堂 ===")

    # 场景：两个班级选了不同的选修课
    class_a = {"Python", "C语言", "电路", "高数", "英语"}
    class_b = {"Python", "Java", "电路", "物理", "体育"}

    print(f"\nA班选修课: {class_a}")
    print(f"B班选修课: {class_b}")

    # 交集 —— 两边都选了什么？
    both = class_a & class_b           # 或 class_a.intersection(class_b)
    print(f"共同选修: {both}")          # {'Python', '电路'}

    # 并集 —— 加起来一共开了哪些课？
    all_courses = class_a | class_b    # 或 class_a.union(class_b)
    print(f"全部课程 ({len(all_courses)}门): {all_courses}")

    # 差集 —— A班选了但B班没选的？
    only_a = class_a - class_b         # 或 class_a.difference(class_b)
    print(f"A班独有: {only_a}")

    # 实战用法：去重
    raw_list = [85, 92, 78, 85, 96, 92, 85]
    unique_scores = set(raw_list)      # 列表转集合 → 自动去重
    unique_list = list(unique_scores)  # 再转回列表（如果需要排序）
    print(f"\n去重演示:")
    print(f"  原始: {raw_list}")
    print(f"  去重后: {sorted(unique_list)}")  # sorted() 排序后输出


# ====== 第三步：主循环（命令行菜单）======

while True:
    print("\n" + "=" * 40)
    print("  1. 查看所有学生")
    print("  2. 添加学生")
    print("  3. 删除学生")
    print("  4. 成绩统计")
    print("  5. 集合小演示 🆕")
    print("  0. 退出")
    print("=" * 40)

    choice = input("> ").strip()

    if choice == "1":
        show_all()
    elif choice == "2":
        add_student()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        query_stats()
    elif choice == "5":
        demo_set()
    elif choice == "0":
        print("再见！👋")
        break
    else:
        print("输入有误，请重新选择")


# ========== 知识点总结 ==========
#
# 【字典 dict】—— 用 {} 或 dict() 创建，存储 键-值 对
#
#   创建:   d = {"a": 1, "b": 2}
#   取值:   d["a"]      ← 键不存在会报错！
#          d.get("a")   ← 键不存在返回 None（安全）
#   赋值/新增: d["c"] = 3
#   删除:   del d["a"]  或  d.pop("a")
#   检查:   "a" in d    ← 判断键是否存在
#   遍历:   for k, v in d.items():
#          for k in d.keys():     只遍历键
#          for v in d.values():   只遍历值
#   长度:   len(d)
#
# 【集合 set】—— 无序、不重复，用 {} 或 set() 创建
#
#   创建:   s = {1, 2, 3}   或   s = set([1,2,2,3])  → {1,2,3}
#   添加:   s.add(4)
#   删除:   s.discard(4)   （不存在也不报错）/  s.remove(4)（不存在会报错）
#   交集:   a & b          两边都有的
#   并集:   a | b          合并去重
#   差集:   a - b          a 有但 b 没有的
#   去重:   list(set(原始列表))    最常用技巧！
#
# ⚠️ 注意：空字典是 {}，空集合必须写成 set()（不能写 {}，那会是空字典）
