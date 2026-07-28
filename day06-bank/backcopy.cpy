class BankAccount:

    def __init__(self, owner, account_id, balance=0):
        self.owner = owner
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("存款必须大于0")
            return
        self.balance += amount
        print(f"存款成功!存入￥{amount},当前余额￥{self.balance}")


    def withdraw(self, amount):
        if amount <= 0:
           print("取款金额必须大于0")
           return
        if amount > self.balance:
            print(f"余额不足,当前余额为￥{self.balance},无法取出￥{amount}")
        self.balance -= amount
        print(f"取款成功,取出￥{amount},剩余￥{self.balance}")
    
    def show_account(self):
        print(f"\n---账户信息---")
        print(f"户主: {self.owner}")
        print(f"账号: {self.account_id}")
        print(f"余额: {self.balance}")

if __name__ == "__main__":

    acc1 = BankAccount("张三","1001",5000)
    acc2 = BankAccount("李四","1002",6000)
    acc1.show_account()
    acc2.show_account()

    print(f"\n>>张三存 3000")
    acc1.deposit(3000)

    print("\n>>李四取 2000")
    acc2.withdraw(2000)

    print("\n=======最终情况========")
    acc1.show_account()
    acc2.show_account()


