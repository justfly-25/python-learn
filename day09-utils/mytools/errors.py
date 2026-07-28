"""
mytools/errors.py — 自定义异常 + 日志工具
==========================================
从 Day 8 抽取出来的异常类和日志函数。

使用方式：
    from mytools.errors import CalculatorError, log_error
    raise CalculatorError("出错了")
"""

import traceback
from datetime import datetime


# ===== 自定义异常类 =====

class MyToolsError(Exception):
    """mytools 包的基础异常"""
    pass


class CalculatorError(MyToolsError):
    """计算器相关异常"""
    pass


class DivisionByZeroError(CalculatorError):
    """除零异常"""
    pass


class InsufficientBalanceError(MyToolsError):
    """余额不足异常"""
    pass


# ===== 日志工具 =====

def log_error(func_name, error, log_file="errors.log"):
    """将错误记录到日志文件"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {func_name} 出错: {error}\n")
        f.write(f"{traceback.format_exc()}\n")
        f.write("-" * 40 + "\n")
    print(f"(错误已记录到 {log_file})")


# ===== 模块自测 =====
if __name__ == "__main__":
    print("正在测试 errors 模块...")
    try:
        raise DivisionByZeroError("测试除零异常")
    except MyToolsError as e:
        print(f"  捕获到异常: {e}")

    try:
        1 / 0
    except ZeroDivisionError as e:
        log_error("测试", e)
        print("  日志已写入")

    print("  测试完毕！")
