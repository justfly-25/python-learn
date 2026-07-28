# Day 9 练习：模块与包

学完 `main.py` 和 `mytools/` 后，试试下面的练习。

---

## 练习 1：写一个自定义模块

在 `day09-utils/` 下新建 `string_utils.py`，包含：

```python
# string_utils.py
def reverse(s):
    """反转字符串"""
    pass

def count_vowels(s):
    """统计元音数量"""
    pass

def is_palindrome(s):
    """判断回文，忽略大小写"""
    pass
```

把 Day 5 exercises.py 里练习 2 的代码搬过来（那些函数你已经写过了），改造成独立模块。

然后在 `main.py` 里 `import string_utils` 测试它。

---

## 练习 2：理解 `__name__ == "__main__"`

在 `mytools/calculator.py` 末尾有自测代码：

```python
if __name__ == "__main__":
    print("正在测试 calculator 模块...")
```

做这个实验：
1. 直接运行 `calculator.py` → 自测代码会执行
2. 从 `main.py` 里 `import` calculator → 自测代码不会执行

**思考**：为什么 `import` 时不执行，直接运行时执行？查一下 `__name__` 在两种情况下分别是什么值。

---

## 练习 3（挑战）：把温度转换器也加入 mytools

在 `mytools/` 下新建 `temperature.py`：

- 包含 `celsius_to_fahrenheit()` 和 `fahrenheit_to_celsius()`
- 加上输入校验：温度不能低于绝对零度（-273.15°C / -459.67°F）
- 自定义 `AbsoluteZeroError` 异常（放到 `errors.py` 里）
- 更新 `__init__.py`，把新模块加进去
- 在 `main.py` 里演示用法

---

## 练习 4：探索 Python 标准库

在终端用 `dir()` 和 `help()` 探索以下模块，记录你发现的有用功能：

```python
import math
import random
import datetime

print(dir(math))     # 看看 math 里有什么
help(math.sqrt)      # 查看 sqrt 的文档
print(dir(random))   # 看看 random 里有什么
help(datetime.datetime)  # 查看 datetime 类的文档
```
