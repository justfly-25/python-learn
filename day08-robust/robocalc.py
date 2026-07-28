"""
Day 8：异常处理 — 健壮计算器
============================

知识点：
1. try/except          — 捕获异常
2. else                 — 无异常时执行
3. finally              — 无论如何都执行
4. raise                — 抛出异常
5. 自定义异常类
6. 异常链（raise from）
7. 日志记录错误

这个文件保留 Day 5 计算器的功能，但用异常处理让它"百毒不侵"。
"""

import traceback
from datetime import datetime

# ========== 1. 自定义异常类 ==========

class CalculatorError(Exception):
    """计算器基础异常"""
    pass


class DivisionByZeroError(CalculatorError):
    """除零错误（自定义）"""
    pass


class InvalidOperatorError(CalculatorError):
    """无效运算符"""
    pass


# ========== 2. 日志工具 ==========

LOG_FILE = "calc_errors.log"

def log_error(func_name, error):
    """将错误记录到日志文件"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {func_name} 出错: {error}\n")
        f.write(f"{traceback.format_exc()}\n")
        f.write("-" * 40 + "\n")
    print(f"(错误已记录到 {LOG_FILE})")


# ========== 3. 带异常处理的运算函数 ==========

def add(a, b):
    try:
        return a + b
    except TypeError as e:
        log_error("add", e)
        # raise from: 保留原始异常链
        raise CalculatorError(f"加法需要两个数字，收到了 {type(a)} 和 {type(b)}") from e


def subtract(a, b):
    try:
        return a - b
    except TypeError as e:
        log_error("subtract", e)
        raise CalculatorError(f"减法需要两个数字") from e


def multiply(a, b):
    try:
        return a * b
    except TypeError as e:
        log_error("multiply", e)
        raise CalculatorError(f"乘法需要两个数字") from e


def divide(a, b):
    """
    除法 —— try/except/else 完整用法：
    - try     尝试执行
    - except  捕获特定异常
    - else    没异常才执行（可以放 return）
    """
    try:
        result = a / b
    except ZeroDivisionError:
        log_error("divide", "除零")
        raise DivisionByZeroError("除数不能为 0！") from None
    except TypeError as e:
        log_error("divide", e)
        raise CalculatorError(f"除法需要数字") from e
    else:
        # else: 只在没有异常时执行
        return result


def power(base, exponent=2):
    """幂运算 —— else 演示"""
    try:
        result = base ** exponent
    except TypeError as e:
        log_error("power", e)
        raise CalculatorError("幂运算需要数字") from e
    except OverflowError as e:
        log_error("power", e)
        raise CalculatorError("数字太大，溢出！") from e
    else:
        return result


def safe_input(prompt):
    """
    安全输入：拦截 Ctrl+C（KeyboardInterrupt）
    finally 保证资源清理（虽然这里没有资源，但演示语法）
    """
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\n用户取消了输入。")
        raise  # 重新抛出，让上层处理
    except EOFError:
        print("\n输入流结束。")
        raise


# ========== 4. 健壮主程序 ==========

history = []

def add_to_history(expression, result):
    history.append(f"{expression} = {result}")


def show_history():
    if not history:
        print("暂无计算记录。")
        return
    print("\n======= 计算历史 =========")
    for i, record in enumerate(history, 1):
        print(f"  {i}. {record}")
    print("==========================\n")


def run_calculator():
    """
    健壮计算器主程序
    -----------------
    用了三层异常保护：
    1. 内层 try：捕获具体运算错误（ValueError、自定义异常）
    2. 中层 try：捕获整个 while 循环的意外异常
    3. finally：保证无论如何都会显示历史记录
    """
    print("\n===== 健壮计算器 =====")
    print("支持的运算： +  -  *  /  **（幂）")
    print("输入 q 退出，h 查看历史")
    print("========================\n")

    try:
        while True:
            try:
                cmd = safe_input("请输入运算符（+ - * / ** 或 q/h）：").strip()

                if cmd == "q":
                    print("再见！")
                    break
                if cmd == "h":
                    show_history()
                    continue
                if cmd not in ("+", "-", "*", "/", "**"):
                    raise InvalidOperatorError(f"不支持的运算符 '{cmd}'，请使用 + - * / **")

                # 获取数字输入
                try:
                    a = float(safe_input("请输入第一个数字："))
                    b = float(safe_input("请输入第二个数字："))
                except ValueError:
                    print("输入无效！请输入数字。")
                    continue

                # 执行运算
                if cmd == "+":
                    res = add(a, b)
                elif cmd == "-":
                    res = subtract(a, b)
                elif cmd == "*":
                    res = multiply(a, b)
                elif cmd == "/":
                    try:
                        res = divide(a, b)
                    except DivisionByZeroError as e:
                        print(f"错误：{e}")
                        continue
                elif cmd == "**":
                    res = power(a, b)

                print(f"结果：{a} {cmd} {b} = {res}")
                add_to_history(f"{a} {cmd} {b}", res)

            except InvalidOperatorError as e:
                print(f"提示：{e}")
            except CalculatorError as e:
                print(f"计算出错：{e}")
            except (KeyboardInterrupt, EOFError):
                print("\n收到退出信号。")
                break
            except Exception as e:
                # 兜底：捕获所有未预料的异常
                log_error("run_calculator", e)
                print(f"发生未知错误：{e}")

    finally:
        # finally 块：无论正常退出还是异常退出，都执行
        show_history()


# ========== 5. 程序入口 ==========

if __name__ == "__main__":
    try:
        run_calculator()
    except Exception as e:
        log_error("main", e)
        print(f"程序崩溃了：{e}")
        print(f"详细错误已记录到 {LOG_FILE}")
