"""
Day 7：面向对象（二）— 动物园管理系统
=====================================

知识点：
1. 继承（子类继承父类的属性和方法）
2. super().__init__() 调用父类构造方法
3. 方法重写（子类重新定义父类的方法 → 多态）
4. isinstance() 类型判断
"""


# ========== 1. 定义 Animal 基类 ==========

class Animal:
    """所有动物的基类（父类）"""

    def __init__(self, name, age):
        self.name = name        # 名字
        self.age = age          # 年龄

    def speak(self):
        """所有动物都会叫，但叫声不同 — 子类来重写"""
        return "..."

    def eat(self):
        """吃 — 通用方法，子类可直接继承"""
        return f"{self.name} 正在吃东西"

    def show_info(self):
        """显示动物信息"""
        return f"{self.name}（{self.age}岁）— 叫声：{self.speak()}"


# ========== 2. 派生具体动物子类 ==========

class Cat(Animal):
    """猫类 — 继承自 Animal"""

    def __init__(self, name, age, breed="中华田园猫"):
        # super() 调用父类的 __init__，初始化 name 和 age
        super().__init__(name, age)
        self.breed = breed      # 猫咪特有属性：品种

    def speak(self):
        """猫的叫声 — 重写父类方法"""
        return "喵喵喵~ 🐱"

    def scratch(self):
        """猫咪特有行为"""
        return f"{self.name} 正在磨爪子！"


class Dog(Animal):
    """狗类 — 继承自 Animal"""

    def __init__(self, name, age, breed="中华田园犬"):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return "汪汪汪！🐶"

    def wag_tail(self):
        """狗狗特有行为"""
        return f"{self.name} 开心地摇着尾巴！"


class Bird(Animal):
    """鸟类 — 继承自 Animal"""

    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly  # 鸟类特有属性：是否会飞

    def speak(self):
        return "叽叽喳喳~ 🐦"

    def fly(self):
        if self.can_fly:
            return f"{self.name} 展翅飞翔！"
        else:
            return f"{self.name} 不会飞（比如企鹅）"


# ========== 3. 多态演示：统一管理 ==========

def zoo_announce(animals):
    """
    多态的核心：不管是什么动物，都可以调用 speak()
    同一个方法名，不同的动物有不同的表现
    """
    print("\n===== 动物园大合唱 =====")
    for animal in animals:
        print(f"  {animal.show_info()}")

    print("\n===== 开饭时间 =====")
    for animal in animals:
        print(f"  {animal.eat()}")


# ========== 4. 测试代码 ==========

if __name__ == "__main__":
    # 创建各种动物
    cat = Cat("小花", 2, "英短")
    dog = Dog("旺财", 3, "金毛")
    bird = Bird("啾啾", 1)
    penguin = Bird("QQ", 4, can_fly=False)

    # 展示每个动物
    print(cat.show_info())
    print(dog.show_info())
    print(bird.show_info())
    print(penguin.show_info())

    # 多态演示：统一处理不同子类
    zoo_announce([cat, dog, bird, penguin])

    # isinstance 类型判断
    print("\n===== 类型检查 =====")
    print(f"小花是猫吗？{isinstance(cat, Cat)}")       # True
    print(f"小花是动物吗？{isinstance(cat, Animal)}")   # True（子类也是父类！）
    print(f"小花是狗吗？{isinstance(cat, Dog)}")        # False
