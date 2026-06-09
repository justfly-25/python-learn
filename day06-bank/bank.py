"""
Day 6：面向对象（一）— 银行账户管理系统
=====================================

知识点：
1. class 定义类
2. __init__ 构造方法
3. self 代表实例本身
4. 实例方法（带 self 参数的方法）
5. 创建对象、调用方法
"""


# ========== 1. 定义 BankAccount 类 ==========

class BankAccount:
    """银行账户类"""

    def __init__(self, owner, account_id, balance=0):
        """
        构造方法：创建账户时自动调用
        owner      — 户主姓名
        account_id — 账号
        balance    — 初始余额（默认 0）
        """
        self.owner = owner
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount):
        """存款"""
        if amount <= 0:
            print("存款金额必须大于 0！")
            return
        self.balance += amount
        print(f"存款成功！存入 ¥{amount}，当前余额 ¥{self.balance}")

    def withdraw(self, amount):
        """取款"""
        if amount <= 0:
            print("取款金额必须大于 0！")
            return
        if amount > self.balance:
            print(f"余额不足！当前余额 ¥{self.balance}，无法取出 ¥{amount}")
            return
        self.balance -= amount
        print(f"取款成功！取出 ¥{amount}，当前余额 ¥{self.balance}")

    def show_info(self):
        """显示账户信息"""
        print(f"\n--- 账户信息 ---")
        print(f"户主：{self.owner}")
        print(f"账号：{self.account_id}")
        print(f"余额：¥{self.balance}")
        print("-----------------")


# ========== 2. 测试代码 ==========

if __name__ == "__main__":
    # 创建两个账户
    acc1 = BankAccount("张三", "1001", 5000)
    acc2 = BankAccount("李四", "1002", 2000)

    # 显示初始信息
    acc1.show_info()
    acc2.show_info()

    # 存取操作
    print("\n>>> 张三存 3000")
    acc1.deposit(3000)

    print("\n>>> 张三取 10000（余额不足）")
    acc1.withdraw(10000)

    print("\n>>> 张三取 2000")
    acc1.withdraw(2000)

    print("\n>>> 李四存 500")
    acc2.deposit(500)

    # 最终状态
    print("\n========== 最终账户状态 ==========")
    acc1.show_info()
    acc2.show_info()
