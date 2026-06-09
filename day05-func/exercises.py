"""
Day 5 练习题：函数练习
====================

做完 calc.py 的学习后，试试独立完成下面的练习吧！
"""

# ===== 练习 1：温度转换器 =====
# 定义两个函数：
#   celsius_to_fahrenheit(c)   — 摄氏度 → 华氏度
#   fahrenheit_to_celsius(f)   — 华氏度 → 摄氏度
# 公式：℉ = ℃ × 9/5 + 32
# 然后写一个主程序让用户选择转换方向并输入温度。
# （提示：参考 calc.py 里 run_calculator 的写法）

# 你的代码写在这里：
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def run_temperature_converter():
    print("\n=====温度转换器=====")
    print("选择准换方向")
    print("1. 摄氏度 → 华氏度")
    print("2. 华氏度 → 摄氏度")
    try:
        user_choice = int(input("输入选择(1或2): "))
    except ValueError:
        print("输入无效，请输入数字。")
        return
    if user_choice == 1:
        celsius = float(input("请输入摄氏度："))
        print(f"{celsius}C = {celsius_to_fahrenheit(celsius)}F")
    
    else:
        fahrenheit = float(input("请输入华氏度："))
        print(f"{fahrenheit}F = {fahrenheit_to_celsius(fahrenheit)}C")

# ===== 练习 2：字符串工具包 =====
# 定义以下函数：
#   reverse_text(s)      — 反转字符串
#   count_vowels(s)      — 统计元音字母（aeiou）的个数（不区分大小写）
#   is_palindrome(s)     — 判断字符串是否为回文（正反一样，忽略大小写）
# 写一个主程序让用户输入一段文字，输出以上三个结果。

# 你的代码写在这里：
def reverse_text(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
        
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
    
def run_string_toolkit():
    print("\n=====字符串工具包=====")
    user_input = input("请输入随机大小字母")
    print(f"反转字符串: {reverse_text(user_input)}")
    print(f"元音字母的个数：{count_vowels(user_input)}")
    if is_palindrome(user_input)
        print("是回文!")
    else:
        print("不是回文!")





# ===== 练习 3（挑战）：数字猜猜看（用函数重构）=====
# 你还记得 Day 3 的猜数字游戏吗？现在用函数重构它！
# 要求：
#   1. generate_answer()     — 生成 1~100 的随机数
#   2. get_user_guess()      — 获取用户输入（带 try-except）
#   3. check_guess(guess, answer)  — 判断大小，返回提示文字
#   4. play_game()           — 主游戏循环
# 主程序调用 play_game() 即可运行。

# 你的代码写在这里：
import random

def generate_answer():
    """生成 1~100 的随机数"""
    return random.randint(1, 100)


def get_user_guess():
    """获取用户输入，带 try-except，返回 int 或 None"""
    # BUG修复①: 引号用英文直引号 " 而不是 ”
    # BUG修复②: 加了 return，无效输入返回 None
    user_guess = input("请输入你猜的数字：")
    try:
        guess = int(user_guess)
        return guess
    except ValueError:
        print("请输入数字哦")
        return None


def check_guess(guess, answer):
    """判断大小，返回提示文字"""
    # BUG修复③: 逻辑反了——原来写 0 < guess < 100 却打印错误，应该是判断是否越界
    # BUG修复④: elif 后面必须跟条件，guess = answer 是赋值不是比较
    # BUG修复⑤: 每个分支后面要加 : 号
    if guess < 1 or guess > 100:
        return "请输入 1~100 以内的数字！"
    if guess == answer:
        return "猜对了！"
    elif guess < answer:
        return "太小了！"
    else:
        return "太大了！"


def play_game():
    """主游戏循环"""
    # BUG修复⑥: def 后面要加 :
    # BUG修复⑦: 原来没有 while 循环，只能猜一次
    # BUG修复⑧: get_user_guess() 没有接收返回值
    # BUG修复⑨: generate_answer 要加 () 才能调用
    print("欢迎来到猜数游戏！")
    answer = generate_answer()
    print("(答案已生成，范围 1~100)")

    while True:
        guess = get_user_guess()
        if guess is None:  # 输入无效，重新来
            continue

        result = check_guess(guess, answer)
        print(result)

        if guess == answer:
            break  # 猜对了，退出

    print("游戏结束！")


# 运行游戏

if __name__ == "__main__"
    play_game()

