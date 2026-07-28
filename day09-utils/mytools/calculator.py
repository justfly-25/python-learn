"""
mytools/calculator.py — 计算器工具模块
======================================
从 Day 5 和 Day 8 抽取出来的计算器函数。

使用方式：
    from mytools.calculator import add, divide
    from mytools import calculator
    print(calculator.add(1, 2))
"""
from mytools.errors import CalculatorError, DivisionByZeroError


def add(a, b):
    """加法"""
    try:
        return a + b
    except TypeError as e:
        raise CalculatorError(f"加法需要数字，不是 {type(a)} 和 {type(b)}") from e


def subtract(a, b):
    """减法"""
    try:
        return a - b
    except TypeError as e:
        raise CalculatorError(f"减法需要数字") from e


def multiply(a, b):
    """乘法"""
    try:
        return a * b
    except TypeError as e:
        raise CalculatorError(f"乘法需要数字") from e


def divide(a, b):
    """除法（带除零保护）"""
    try:
        return a / b
    except ZeroDivisionError:
        raise DivisionByZeroError("除数不能为 0！") from None
    except TypeError as e:
        raise CalculatorError(f"除法需要数字") from e


def power(base, exponent=2):
    """幂运算，默认计算平方"""
    try:
        return base ** exponent
    except TypeError as e:
        raise CalculatorError(f"幂运算需要数字") from e


# ===== 模块自测：只在直接运行本文件时执行 =====
if __name__ == "__main__":
    print("正在测试 calculator 模块...")
    print(f"  add(10, 5)    = {add(10, 5)}")
    print(f"  divide(10, 2) = {divide(10, 2)}")
    print(f"  power(5)      = {power(5)}")
    print("  测试完毕！")
