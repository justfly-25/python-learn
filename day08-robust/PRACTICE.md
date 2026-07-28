# Day 8 练习：异常处理

学完 `robocalc.py` 后，试着完成下面练习。

---

## 练习 1：给温度转换器加异常保护

还记得 Day 5 的温度转换器吗？把它改造成"健壮版"：

- 用户输入非数字时，捕获 `ValueError` 并提示，不崩溃
- 用户按 Ctrl+C 时，显示"再见"再退出（捕获 `KeyboardInterrupt`）
- 输入温度不合法时（绝对零度以下），抛出自定义异常 `AbsoluteZeroError`
- 用 `finally` 表示感谢使用

```python
# 自定义异常
class AbsoluteZeroError(Exception):
    """温度不能低于绝对零度"""
    pass
```

---

## 练习 2：给银行账户加异常保护

打开 Day 6 的 `bank.py`，增强它的健壮性：

- `deposit()` 和 `withdraw()` 的 `amount` 参数必须是正数，否则抛出自定义异常
- `withdraw()` 余额不足时，抛出 `InsufficientBalanceError`（自定义异常）
- 转账 `transfer_to()` 要处理目标账户不存在的情况
- 主程序中 try/except 捕获这些异常，友好提示用户

---

## 练习 3（挑战）：文件安全读写工具

写一个 `safe_read_file()` 和 `safe_write_file()` 函数：

```python
def safe_read_file(filepath):
    """安全读文件，处理各种异常"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"文件不存在：{filepath}")
        return None
    except PermissionError:
        print(f"没有权限读取：{filepath}")
        return None
    except Exception as e:
        print(f"读取失败：{e}")
        return None

def safe_write_file(filepath, content):
    """安全写文件（类似上面，自己实现）"""
    pass  # 你的代码
```

要点：
- 用 `try/except/else/finally` 全套语法
- 用到什么异常就去查 Python 官方文档
- 测试：故意传不存在的路径 / 只读文件，看程序会不会崩
