"""
mytools/animals.py — 动物园模块
===============================
从 Day 7 抽取出来的动物类（继承与多态）。

使用方式：
    from mytools.animals import Cat, Dog, Bird
    pets = [Cat("咪咪"), Dog("旺财"), Bird("啾啾")]
    for pet in pets:
        print(pet.speak())
"""


class Animal:
    """动物基类"""
    total_count = 0  # 类变量：统计所有动物数量

    def __init__(self, name):
        self.name = name
        Animal.total_count += 1

    def speak(self):
        """子类必须重写这个方法"""
        raise NotImplementedError("子类必须实现 speak() 方法")

    def info(self):
        print(f"{self.name} 是一只 {self.__class__.__name__}")

    @classmethod
    def get_count(cls):
        """类方法：返回创建的动物总数"""
        return cls.total_count

    @staticmethod
    def is_warm_blooded():
        """静态方法：所有动物是否恒温"""
        return "大多数是恒温动物"


class Cat(Animal):
    """猫 — 继承 Animal"""
    def speak(self):
        return f"{self.name}: 喵喵~ 🐱"

    def scratch(self):
        return f"{self.name} 在磨爪子！"


class Dog(Animal):
    """狗 — 继承 Animal"""
    def speak(self):
        return f"{self.name}: 汪汪！🐶"

    def fetch(self):
        return f"{self.name} 去叼球了！"


class Bird(Animal):
    """鸟 — 继承 Animal"""
    def speak(self):
        return f"{self.name}: 啾啾~ 🐦"

    def fly(self):
        return f"{self.name} 飞起来了！"


# ===== 模块自测 =====
if __name__ == "__main__":
    print("正在测试 animals 模块...")
    cat = Cat("小花")
    dog = Dog("大黄")
    bird = Bird("小蓝")

    for a in [cat, dog, bird]:
        a.info()
        print(f"  speak: {a.speak()}")

    print(f"  共创建了 {Animal.get_count()} 只动物")
    print("  测试完毕！")
