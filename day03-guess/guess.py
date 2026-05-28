"""
Day 3 — 猜数字游戏
知识点：
    1. random 模块 —— 生成随机数
    2. while 循环 —— 反复执行直到条件满足
    3. if-elif-else —— 多分支条件判断
    4. int() / input() —— 用户输入转整数
    5. 计数器模式 —— 用变量记录次数
"""

# ====== 第一步：导入随机数模块 ======
import random  # Python 内置模块，用于生成随机数

# ====== 第二步：生成一个 1~100 的随机整数 ======
secret = random.randint(1, 100)  # randint(a, b) 返回 a 到 b 之间的随机整数（包含两端）
count = 0                         # 猜测次数计数器，初始为 0

print("=" * 40)
print("   猜数字游戏！")
print("   我已经想好了一个 1~100 之间的数字")
print("   来猜猜看是多少吧！")
print("=" * 40)

# ====== 第三步：用 while 循环让用户反复猜测 ======
while True:                      # True 表示"永远循环"，直到遇到 break 才退出
    count += 1                   # 每猜一次，计数器 +1（等价于 count = count + 1）

    # 获取用户输入，并转为整数
    user_input = input(f"\n第 {count} 次，请输入你的猜测 (1-100): ")

    # ====== 异常处理：防止用户输入非数字 ======
    try:
        guess = int(user_input)  # 把字符串转成整数
    except ValueError:           # 如果转换失败（比如输入了字母）
        print("请输入数字哦！")
        count -= 1               # 这次不算，次数回退
        continue                 # 跳过本次循环，重新开始（回到 while True）

    # ====== 核心判断逻辑：比较大小 ======
    if guess < 1 or guess > 100:  # 先检查范围
        print("超出范围了！只能猜 1~100 之间的数字")
        count -= 1                # 范围错误不算一次有效猜测
        continue

    if guess < secret:            # 猜的数字 < 目标数字
        print("太小了！再大一点 📈")
    elif guess > secret:          # 猜的数字 > 目标数字
        print("太大了！再小一点 📉")
    else:                         # 猜对了！（guess == secret）
        print("\n" + "=" * 40)
        print(f"🎉 恭喜你！答案就是 {secret}！")
        print(f"你一共猜了 {count} 次")

        # ====== 根据次数给出评价 ======
        if count <= 3:
            print("评价：运气爆棚！你是算命的吗？ 🔮")       # 嵌套 if：在 else 里再判断
        elif count <= 7:
            print("评价：很厉害！脑子转得快 ⚡")
        elif count <= 15:
            print("评价：还不错，继续加油！💪")
        else:
            print("评价：嗯...下次用二分法试试？😅")

        print("=" * 40)
        break                     # 跳出 while 循环，程序结束


# ========== 知识点总结 ==========
#
# 【while 循环】
#   while 条件:      → 当条件为 True 时，重复执行下面的代码块
#   while True:      → 无限循环，必须配合 break 使用来退出
#   break            → 立即跳出当前循环
#   continue         → 跳过本次循环剩余部分，直接进入下一轮
#
# 【if-elif-else】
#   if 条件1:        → 条件1 成立时执行
#   elif 条件2:      → 条件1不成立但条件2成立时执行（可以有多个 elif）
#   else:            → 以上所有条件都不成立时执行
#
# 【random 模块】
#   import random                    → 导入模块
#   random.randint(1, 100)           → 生成 [1, 100] 闭区间内的随机整数
#   random.random()                  → 生成 [0, 1) 之间的小数
#   random.choice(["A", "B", "C"])   → 从列表中随机选一个元素
#
# 【计数器模式】
#   count = 0        → 初始化
#   count += 1       → 每次操作后自增（等价于 count = count + 1）
