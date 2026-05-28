tasks = ["学习高数","学习python","学习英语"]
def show_tasks():
    print("\n======待办清单=======")
    if len(tasks) == 0:
        print("good job! 所以任务都完成了")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i} . {task}")
print("========================")
print("欢迎使用代办任务清单处理器")
while True:
    show_tasks()
    
    print("\n请输入你的选择: ")
    print("  1. 查看清单")
    print("  2. 添加任务")
    print("  3. 完成一项任务(delete)")
    print("  4. 退出程序")
    choice = input("\n> ")

    if choice == "1" :
        print(f"\n目前还有{len(tasks)}个代办任务")
    
    elif choice == "2" :
        new_task = input("请输入你要添加的任务： ")
        new_task = new_task.strip()
        if new_task:
            tasks.append(new_task)
            print(f"\n已添加新任务:{new_task}")
        else:
            print("\n任务不能为空!")

    elif choice == "3" :
        if len(tasks) == 0:
            print("\n已经没有任务可以删除了!")
            continue
        try:
            num=input("请输入已完成的任务序号： ")
            index = int(num) -1

            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"\n{removed_task}已完成啦！")
            else:
                print(f"\n无效的序号!请在1到{len(tasks)}中选择")
        except ValueError:
            print("\n请输入一个有效的数字!")

    elif choice == "4" :
        print("\n谢谢使用!今天有好好学习哦!")
        break
    else:
        print("\n无效的选择,请输入 1,2,3,4 中的一个数字!")
