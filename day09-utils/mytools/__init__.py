"""
mytools 工具包
==============

把 Day 5-8 学到的功能模块化，做成一个可复用的工具包。

包结构：
    mytools/
    ├── __init__.py      ← 你在这里！包的入口
    ├── calculator.py    ← 计算器函数
    ├── banking.py       ← 银行账户类
    ├── animals.py       ← 动物类
    └── errors.py        ← 自定义异常 + 日志

三种导入方式：

    1. import mytools                    → mytools.calculator.add(1,2)
    2. from mytools import calculator    → calculator.add(1,2)
    3. from mytools.calculator import add → add(1,2)
"""

# __init__.py 的作用：
# 1. 让 Python 知道 mytools/ 是一个包
# 2. 控制 from mytools import * 时导出什么
# 3. 在这里写包级别的文档和初始化

__version__ = "1.0.0"
__author__ = "菲菲"

# 预导入常用的子模块，方便用户直接用 mytools.xxx
from mytools import calculator
from mytools import banking
from mytools import animals
from mytools import errors

# 把最常用的类和函数提升到包级别
# 这样用户可以直接 from mytools import BankAccount
from mytools.banking import BankAccount
from mytools.animals import Animal, Cat, Dog, Bird
from mytools.errors import (
    MyToolsError,
    CalculatorError,
    DivisionByZeroError,
    InsufficientBalanceError,
    log_error,
)

# __all__ 控制 from mytools import * 时导出什么
__all__ = [
    "calculator",
    "banking",
    "animals",
    "errors",
    "BankAccount",
    "Animal",
    "Cat",
    "Dog",
    "Bird",
    "CalculatorError",
    "DivisionByZeroError",
    "InsufficientBalanceError",
    "log_error",
]


# ===== 包级别自测 =====
if __name__ == "__main__":
    print(f"mytools v{__version__} — by {__author__}")
    print(f"\n可用模块：")
    print(f"  mytools.calculator  — 四则运算 + 幂运算")
    print(f"  mytools.banking     — 银行账户管理")
    print(f"  mytools.animals     — 动物园（继承与多态）")
    print(f"  mytools.errors      — 自定义异常 + 日志")
    print(f"\n快速开始：")
    print(f"  from mytools import BankAccount")
    print(f"  acc = BankAccount('张三', '001', 1000)")
    print(f"  acc.deposit(500)")
