def say_hello():
    print("你好!欢迎使用计算器")

def add(a,b):
    return a+b

say_hello()
result = add(10,5)
print(f"10 +5 = {result}")

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        return"错误:除数不能为0!"
    return a/b

def power(base, exponent=2):
    return base ** exponent

def calc_all(a,b):
    s= a+b
    diff = a-b
    prod = a*b
    quot =a / b if b != 0 else "无意义" 
    return s, diff,prod,quot
sum_val, diff_val,prod_val,quot_val = calc_all(20,4)
print(f"20 和 4 的计算结果： 和={sum_val},差={diff_val},积={prod_val},商={quot_val}")

history = []

def add_to_history(expression,result):
    history.append(f"{expression} = {result}")
    print(f"已记录:{expression} = {result}")

def show_history():
    """BUG修复①: 统一缩进为4空格，分隔线移到循环外部，只打印一次"""
    if not history:
        print("暂无计算记录。")
        return

    print("\n======= 计算历史 =========")  # \n 放在开头，先换行再打标题
    for i, record in enumerate(history, 1):
        print(f"  {i}. {record}")
    print("==========================\n")  # 分隔线只打一次，放在循环外面

def main_calculator():
    print("\n====简单计算器======")
    print("支持的运算： + - * / ** ")
    print("======================")
    while True:
        cmd = input("\n请输入运算符")
        if cmd == "q":
            print("再见！")  # BUG修复③: 退出时给个提示
            break
        if cmd not in ["+","-","*","/","**"]:
            print("不支持的运算符,请重新输入!")
            continue
        try:
            a = float(input("请输入第一个数："))
            b = float(input("请输入第二个数："))
        except  ValueError as e:
            print(f"输入无效,错误原因： {e}")
            continue
        if cmd == "+":
           res = add(a,b)
        elif cmd == "-":
            res = subtract(a,b)
        elif cmd == "*":
            res = multiply(a,b)
        elif cmd == "/":
            res = divide(a,b)
        elif cmd == "**":
            res = power(a,b)
        print(f"结果：{a} {cmd} {b} = {res}")
        # BUG修复②: 只传表达式，不要传结果——add_to_history 会自动拼 "{表达式} = {结果}"
        add_to_history(f"{a} {cmd} {b}", res)

if __name__ == "__main__":
    main_calculator()
    show_history()
    
