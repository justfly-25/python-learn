"""
Day 9 主程序 — 使用 mytools 工具包
====================================

这个文件演示如何导入和使用我们自己打造的 mytools 包。
"""

# ===== 导入方式一：import 包名 =====
# 需要用完整路径 mytools.xxx
import mytools

print("=" * 50)
print("方式 1：import mytools")
print("=" * 50)

print(f"\n>>> {mytools.animals.Dog.__name__} 类演示")
dog = mytools.animals.Dog("大黄")
print(dog.speak())

print(f"\n>>> 计算器演示")
print(f"  2 + 3  = {mytools.calculator.add(2, 3)}")
print(f"  10 / 3 = {mytools.calculator.divide(10, 3):.2f}")

print(f"\n>>> 异常处理演示")
try:
    mytools.calculator.divide(1, 0)
except mytools.errors.DivisionByZeroError as e:
    print(f"  捕获到: {e}")


# ===== 导入方式二：from 包 import 模块 =====
from mytools import banking, animals as zoo  # 可以取别名！

print(f"\n{'=' * 50}")
print("方式 2：from mytools import banking, animals")
print("=" * 50)

print(f"\n>>> 银行操作")
acc1 = banking.BankAccount("张三", "1001", 5000)
acc2 = banking.BankAccount("李四", "1002", 3000)
acc1.deposit(2000)
acc1.transfer_to(acc2, 1500)
acc2.show_info()

print(f"\n>>> 动物园（用别名 zoo）")
pets = [zoo.Cat("咪咪"), zoo.Bird("啾啾")]
for p in pets:
    print(f"  {p.speak()}")

# ===== 导入方式三：from 包.模块 import 具体 =====
# 也可以用 dir() 和 help() 探索模块
from mytools.calculator import add, divide, power

print(f"\n{'=' * 50}")
print("方式 3：from mytools.calculator import add, divide, power")
print("=" * 50)

print(f"\n>>> 直接调用函数（无需前缀）")
print(f"  add(100, 200)     = {add(100, 200)}")
print(f"  divide(100, 3)    = {divide(100, 3):.2f}")
print(f"  power(2, 10)      = {power(2, 10)}")

print(f"\n>>> 用 dir() 探索 calculator 模块")
print(f"  {dir(mytools.calculator)}")

print(f"\n{'=' * 50}")
print("所有导入方式演示完毕！")
print(f"mytools 版本：{mytools.__version__}")
print("=" * 50)
