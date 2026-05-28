import random
secret = random.randint(1,100)
count =0

print("=" * 40)
print("  猜数字游戏！")
print(" 我已经想好了一个1~100之间的数字!")
print(" 试着猜猜是多少吧!")
print("="*40)

while True:
    count += 1
    user_input = input(f"\n第{count}次,请输入你的猜测(1-100): ")
    try:
        guess = int(user_input)
    except ValueError:
        print("请输入数字哦！")
        count -= 1
        continue
    if guess < secret:
        print("太小了!再大一点")
    elif guess > secret:
        print("太大了！再小一点")
    else:
        print(f"恭喜你!猜对了,答案就是{secret}!")
        print(f"你一共猜了{count}次")
        
        if count <= 3:
            print("你是甜菜来的吧！")
        elif count <=7:
            print("开挂了吗？")
        elif count <=15:
            print("还行吧,加油")
        else:
            print("你是🐖么!")
    print("="*40)
    break