import random
count = 0
win_count = 0
print("****欢迎来到石头剪刀布游戏！****")
while True:
    count += 1
    choices = ["石头", "剪刀", "布"]          # 改 ①：[] 列表，不是 {} 集合
    computer = random.choice(choices)
    player = input("请输入你的选择(石头/剪刀/布): ")

    # ✅ 先处理退出
    if player == "退出":
        print(f"再见!本次战绩:{win_count}胜{count - win_count - 1}负")
        break

    # ✅ 检查输入是否有效
    if player not in choices:
        print("输入无效，请重新输入！")
        count -= 1
        continue

    # ✅ 判断胜负
    if player == computer:
        print(f"平局！电脑也选择了{computer}")         # 改 ②：加 f
    elif player == "石头" and computer == "剪刀" or \
         player == "剪刀" and computer == "布" or \
         player == "布" and computer == "石头":
        print(f"恭喜你赢了!电脑选择了{computer}")       # 改 ②：加 f
        win_count += 1
    else:
        print(f"很遗憾，你输了！电脑选择了{computer}")   # 改 ③：else 代替复杂反向条件
