"""
待办清单管理器 —— 列表、循环、字符串操作

今天学到的知识点：
1. 列表（list）：有序的数据集合，用 [] 表示
2. append()：在列表末尾添加元素
3. pop(index)：删除指定位置的元素，并返回被删的值
4. len()：获取列表长度
5. for 循环：遍历列表中的每个元素
6. while 循环：反复执行代码块，直到条件不满足
7. input()：获取用户输入
8. f-string：格式化输出字符串
"""

# ========== 第一步：创建初始待办清单 ==========
# 用列表（list）存储待办事项，每个元素是一个字符串
tasks = ["买菜", "写代码", "运动"]


# ========== 第二步：定义显示清单的函数 ==========
def show_tasks():
    """打印当前所有待办事项（带编号）"""
    print("\n====== 待办清单 =======")
    # 用 enumerate() 同时获取索引和元素
    # 索引从 1 开始显示（更符合人类习惯）
    if len(tasks) == 0:
        print("🎉 恭喜！所有任务都完成了！")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"  {i}. {task}")
    print("========================")


# ========== 第三步：主程序循环 ==========
print("欢迎使用待办清单管理器！")

while True:  # 无限循环，直到用户选择退出
    show_tasks()

    # 显示菜单
    print("\n请选择操作：")
    print("  1. 查看清单")
    print("  2. 添加事项")
    print("  3. 完成一项（删除）")
    print("  4. 退出")

    choice = input("\n> ")  # 获取用户选择

    # ========== 根据选择执行不同操作 ==========
    if choice == "1":
        # 查看清单 —— 其实每次循环开头已经显示了
        # 这里可以加一点额外的统计信息
        print(f"\n📊 当前共有 {len(tasks)} 个待办事项")

    elif choice == "2":
        # 添加新事项
        new_task = input("输入要添加的事项： ")
        # strip() 去掉首尾空格，防止用户误输入空格
        new_task = new_task.strip()
        if new_task:  # 如果输入不为空才添加
            tasks.append(new_task)  # append() 在列表末尾追加
            print(f"\n✅ 已添加：「{new_task}」")
        else:
            print("\n⚠️ 输入不能为空！")

    elif choice == "3":
        # 完成一项（从列表中删除）
        if len(tasks) == 0:
            print("\n⚠️ 已经没有待办事项了！")
            continue  # 跳过本次循环剩余部分，回到开头

        try:
            # 让用户输入要完成的序号
            num = input("输入要完成的序号： ")
            index = int(num) - 1  # 用户输入的是从1开始，列表索引是从0开始

            # 检查序号是否有效
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)  # pop() 删除并返回被删的元素
                print(f"\n✅ 已完成：「{removed}」加油！")
            else:
                print(f"\n⚠️ 无效的序号！请在 1~{len(tasks)} 之间选择")

        except ValueError:
            # int() 转换失败时进入这里（比如用户输入了字母）
            print("\n⚠️ 请输入数字序号！")

    elif choice == "4":
        # 退出程序
        print("\n再见！今天也要加油哦 💪")
        break  # 跳出 while True 循环，程序结束

    else:
        # 处理无效输入
        print("\n⚠️ 无效的选择，请输入 1-4 的数字")
