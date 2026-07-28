"""
mytools/banking.py — 银行账户模块
=================================
从 Day 6 抽取出来的 BankAccount 类。

使用方式：
    from mytools.banking import BankAccount
    acc = BankAccount("张三", "1001", 5000)
    acc.deposit(1000)
"""
from mytools.errors import InsufficientBalanceError


class BankAccount:
    """银行账户类"""

    def __init__(self, owner, account_id, balance=0):
        self.owner = owner
        self.account_id = account_id
        self.balance = balance
        self._history = []  # 交易记录（_ 开头表示"约定私有"）

    def deposit(self, amount):
        """存款"""
        if amount <= 0:
            raise ValueError("存款金额必须大于 0")
        self.balance += amount
        self._history.append(f"存款 +¥{amount}")
        print(f"存款成功！+¥{amount}，余额 ¥{self.balance}")

    def withdraw(self, amount):
        """取款"""
        if amount <= 0:
            raise ValueError("取款金额必须大于 0")
        if amount > self.balance:
            raise InsufficientBalanceError(
                f"余额不足！当前 ¥{self.balance}，无法取出 ¥{amount}"
            )
        self.balance -= amount
        self._history.append(f"取款 -¥{amount}")
        print(f"取款成功！-¥{amount}，余额 ¥{self.balance}")

    def transfer_to(self, target, amount):
        """转账给另一个账户"""
        self.withdraw(amount)
        target.deposit(amount)
        self._history.append(f"转账 → {target.owner} ¥{amount}")

    def show_info(self):
        """显示账户信息"""
        print(f"\n--- {self.owner} 的账户 ---")
        print(f"账号：{self.account_id}")
        print(f"余额：¥{self.balance}")
        if self._history:
            print(f"最近 5 笔交易：")
            for h in self._history[-5:]:
                print(f"  {h}")
        print("-" * 25)

    def __str__(self):
        """print(对象) 时显示的内容"""
        return f"BankAccount({self.owner}, {self.account_id}, ¥{self.balance})"


# ===== 模块自测 =====
if __name__ == "__main__":
    print("正在测试 banking 模块...")
    a = BankAccount("测试", "9999", 1000)
    a.deposit(500)
    a.withdraw(200)
    a.show_info()
    print("  测试完毕！")
