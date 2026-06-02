"""
Day 5：函数（Functions）— 简易计算器
===============================

知识点：
1. 定义函数 def
2. 参数与返回值
3. 默认参数 / 关键字参数
4. 局部变量与全局变量
5. 函数作为模块化工具
"""

# ========== 1. 基本函数定义 ==========

def say_hello():
    """打印问候语（函数文档字符串）"""
    print("你好！欢迎使用简易计算器。")


def add(a, b):
    """加法：接收两个数，返回它们的和"""
    return a + b


# ========== 2. 调用函数 ==========

say_hello()

# 调用 add 并打印结果
result = add(10, 5)
print(f"10 + 5 = {result}")


# ========== 3. 多种参数形式 ==========

def subtract(a, b):
    """减法"""
    return a - b


def multiply(a, b):
    """乘法"""
    return a * b


def divide(a, b):
    """除法（带除零保护）"""
    if b == 0:
        return "错误：除数不能为 0！"
    return a / b


# ========== 4. 默认参数 ==========

def power(base, exponent=2):
    """幂运算，默认计算平方"""
    return base ** exponent


print(f"3 的平方 = {power(3)}")      # 使用默认参数 exponent=2
print(f"2 的 10 次方 = {power(2, 10)}")  # 传入 exponent=10


# ========== 5. 多个返回值（元组）==========

def calc_all(a, b):
    """返回加减乘除四个结果"""
    s = a + b
    diff = a - b
    prod = a * b
    quot = a / b if b != 0 else "无意义"
    return s, diff, prod, quot  # 实际上返回一个元组


sum_val, diff_val, prod_val, quot_val = calc_all(20, 4)
print(f"20 和 4 的计算结果：和={sum_val}, 差={diff_val}, 积={prod_val}, 商={quot_val}")


# ========== 6. 全局变量与局部变量 ==========

# 全局变量
history = []  # 用来记录所有计算历史


def add_to_history(expression, result):
    """将一条计算记录追加到全局 history 列表中"""
    # 这里 history 是全局变量，但要修改它需要用 global 声明吗？
    # 答：如果是修改列表内容（append/pop），不需要 global；
    # 如果是重新赋值（history = ...），才需要 global
    history.append(f"{expression} = {result}")
    print(f"已记录：{expression} = {result}")


def show_history():
    """显示所有计算历史"""
    if not history:
        print("暂无计算记录。")
        return

    print("\n===== 计算历史 =====")
    for i, record in enumerate(history, 1):
        print(f"{i}. {record}")
    print("====================\n")


# ========== 7. 主程序：交互式计算器 ==========

def run_calculator():
    """
    简易计算器主程序
    用户输入两个数和运算符，进行计算并记录历史
    """
    print("\n===== 简易计算器 =====")
    print("支持的运算：+  -  *  /  **（幂）")
    print("输入 q 退出")

    while True:
        cmd = input("\n请输入运算符（+ - * / ** 或 q 退出）：").strip()

        if cmd == "q":
            print("再见！")
            break

        if cmd not in ("+", "-", "*", "/", "**"):
            print("无效运算符，请重新输入！")
            continue

        try:
            a = float(input("请输入第一个数字："))
            b = float(input("请输入第二个数字："))
        except ValueError:
            print("输入无效，请输入数字！")
            continue

        # 根据运算符调用对应的函数
        if cmd == "+":
            res = add(a, b)
        elif cmd == "-":
            res = subtract(a, b)
        elif cmd == "*":
            res = multiply(a, b)
        elif cmd == "/":
            res = divide(a, b)
        elif cmd == "**":
            res = power(a, b)

        print(f"结果：{a} {cmd} {b} = {res}")

        # 记录到历史
        add_to_history(f"{a} {cmd} {b}", res)


# ========== 8. 程序入口 ==========

if __name__ == "__main__":
    run_calculator()

    # 用户退出后，展示历史记录
    show_history()
