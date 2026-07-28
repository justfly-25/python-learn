import traceback
from datetime import datetime


class CalculatorError(Exception):
    pass

class DivisionByZeroError(CalculatorError):
    pass

class InvalidOperatorError(CalculatorError):
    pass

LOG_FILE = "calc_error.log"
def log_error(func_name, error):
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {func_name} 出错： {error}\n")
        f.write(f"{traceback.format_exc()}\n") 
        f.write(f"-"*40 + "\n")
    print(f"(错误已经记录到{LOG_FILE})")

def add(a, b):
    try:
        return a + b
    except TypeError as e:
        log_error("subject",e)
        raise CalculatorError (f"加法需要二个数字，收到了{type(a)}and {type(b)}") from e
    
def multiply(a,b):
     try :
         return a * b
     except TypeError as e:
         log_error("multiply",e)
         raise CalculatorError(f"乘法需要二个数字")from e
     
def subtract(a, b):
    try:
        return a - b
    except TypeError as e:
        log_error("subtract", e)
        raise CalculatorError(f"减法需要二个数字") from e


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        log_error("divide", "除零")
        raise DivisionByZeroError("除数不能为 0！") from None
    except TypeError as e:
        log_error("divide", e)
        raise CalculatorError(f"除法需要数字") from e
    else:
        return result


def power(base, exponent=2):
    try:
        result = base ** exponent
    except TypeError as e:
        log_error("power", e)
        raise CalculatorError("幂运算需要数字") from e
    except OverflowError as e:
        log_error("power", e)
        raise CalculatorError("数字太大，溢出！") from e
    else:
        return result


def safe_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\n用户取消了输入。")
        raise
    except EOFError:
        print("\n输入流结束。")
        raise


# ========== 主程序 ==========

history = []

def add_to_history(expression, result):
    history.append(f"{expression} = {result}")

def show_history():
    if not history:
        print("暂无计算记录。")
        return
    print("\n======= 计算历史 =========")
    for i, record in enumerate(history, 1):
        print(f"  {i}. {record}")
    print("==========================\n")

def run_calculator():
    print("\n===== 健壮计算器 =====")
    print("支持的运算： +  -  *  /  **（幂）")
    print("输入 q 退出，h 查看历史")
    print("========================\n")

    try:
        while True:
            try:
                cmd = safe_input("请输入运算符（+ - * / ** 或 q/h）：").strip()

                if cmd == "q":
                    print("再见！")
                    break
                if cmd == "h":
                    show_history()
                    continue
                if cmd not in ("+", "-", "*", "/", "**"):
                    raise InvalidOperatorError(f"不支持的运算符 '{cmd}'，请使用 + - * / **")

                try:
                    a = float(safe_input("请输入第一个数字："))
                    b = float(safe_input("请输入第二个数字："))
                except ValueError:
                    print("输入无效！请输入数字。")
                    continue

                if cmd == "+":
                    res = add(a, b)
                elif cmd == "-":
                    res = subtract(a, b)
                elif cmd == "*":
                    res = multiply(a, b)
                elif cmd == "/":
                    try:
                        res = divide(a, b)
                    except DivisionByZeroError as e:
                        print(f"错误：{e}")
                        continue
                elif cmd == "**":
                    res = power(a, b)

                print(f"结果：{a} {cmd} {b} = {res}")
                add_to_history(f"{a} {cmd} {b}", res)

            except InvalidOperatorError as e:
                print(f"提示：{e}")
            except CalculatorError as e:
                print(f"计算出错：{e}")
            except (KeyboardInterrupt, EOFError):
                print("\n收到退出信号。")
                break
            except Exception as e:
                log_error("run_calculator", e)
                print(f"发生未知错误：{e}")

    finally:
        show_history()


if __name__ == "__main__":
    try:
        run_calculator()
    except Exception as e:
        log_error("main", e)
        print(f"程序崩溃了：{e}")
        print(f"详细错误已记录到 {LOG_FILE}")
