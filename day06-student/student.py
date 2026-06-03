"""
Day 6：面向对象（一）— 类与对象 — 学生信息管理系统
====================================================

知识点：
1. class 关键字定义类
2. __init__ 构造方法（初始化对象）
3. self 代表对象自身
4. 实例属性 vs 类属性
5. 实例方法

核心概念：
  - 类（Class）= 设计图纸（比如"学生"的模板）
  - 对象（Object）= 按图纸造出来的实物（比如"张三"这个具体学生）
  - 属性（Attribute）= 对象的数据（姓名、年龄、成绩）
  - 方法（Method）= 对象的行为（显示信息、计算分数）
"""

# ========== 1. 定义第一个类 ==========

class Student:
    """
    学生类：管理一个学生的基本信息和成绩
    """
    # 类属性：所有学生共享（比如学生总数）
    total_count = 0

    def __init__(self, name, age):
        """
        构造方法：创建学生时自动调用
        self.name 和 self.age 是实例属性，每个学生各自不同
        """
        self.name = name
        self.age = age
        self.scores = {}  # 科目 → 分数的字典
        Student.total_count += 1  # 每创建一个学生，总数 +1

    # ---------- 实例方法 ----------

    def add_score(self, subject, score):
        """添加或修改某科成绩"""
        if not 0 <= score <= 100:
            print(f"⚠️ 分数 {score} 不在 0-100 范围内，已忽略")
            return
        self.scores[subject] = score
        print(f"✅ {self.name} 的 {subject} 成绩已录入：{score}")

    def get_average(self):
        """计算所有科目的平均分"""
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)

    def get_max_score(self):
        """返回最高分科目和分数"""
        if not self.scores:
            return None, 0
        subject = max(self.scores, key=self.scores.get)
        return subject, self.scores[subject]

    def show_info(self):
        """打印学生的完整信息"""
        print(f"\n📋 学生信息")
        print(f"  姓名：{self.name}")
        print(f"  年龄：{self.age}")
        if self.scores:
            print(f"  成绩：{self.scores}")
            print(f"  平均分：{self.get_average():.1f}")
            best_sub, best_score = self.get_max_score()
            print(f"  最高分：{best_sub} ({best_score})")
        else:
            print("  成绩：暂无")


# ========== 2. 创建对象试试看 ==========

print("=" * 40)
print("Day 6 — 学生信息管理系统")
print("=" * 40)

# 用类来创建具体的"对象"
s1 = Student("张三", 18)
s2 = Student("李四", 19)

s1.add_score("数学", 92)
s1.add_score("英语", 85)
s1.add_score("Python", 98)

s2.add_score("数学", 78)
s2.add_score("英语", 95)
s2.add_score("Python", 88)

s1.show_info()
s2.show_info()

print(f"\n目前共有 {Student.total_count} 名学生")


# ========== 3. 练习：完成学生管理系统 ==========

class StudentManager:
    """
    学生管理器：管理多个学生对象
    TODO: 请你补充完整下面的方法！
    """

    def __init__(self):
        self.students = []  # 存放所有学生对象的列表

    def add_student(self, name, age):
        """添加一个新学生"""
        # 提示：创建 Student 对象，添加到 self.students
        # 你的代码：
        pass

    def find_student(self, name):
        """按姓名查找学生，找到则返回对象，否则返回 None"""
        # 提示：遍历 self.students，比较 name
        # 你的代码：
        pass

    def remove_student(self, name):
        """按姓名删除学生"""
        # 提示：找到学生后用 self.students.remove() 删除
        # 你的代码：
        pass

    def list_all(self):
        """显示所有学生信息"""
        # 提示：遍历 self.students，每个调用 show_info()
        # 你的代码：
        pass

    def class_average(self):
        """计算全班所有学生所有科目的总平均分"""
        # 提示：汇总所有学生的平均分再求总平均
        # 你的代码：
        pass


# ========== 4. 程序入口（交互式） ==========

if __name__ == "__main__":
    print("\n" + "=" * 40)
    print("交互式学生管理系统")
    print("=" * 40)

    # 提示：创建 StudentManager 对象，写一个 while 循环菜单
    # 菜单选项：1.添加学生  2.录入成绩  3.查找学生
    #           4.删除学生  5.显示全部  6.全班平均分  0.退出

    # 你的代码：
    pass
