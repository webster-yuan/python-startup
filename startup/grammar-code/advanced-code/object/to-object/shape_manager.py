from abc import ABC, abstractmethod


# 抽象图形
class Shape(ABC):
    @abstractmethod
    def area(self):
        """"""
        pass


# 具体图形
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


# 工厂类（统一创建图形）
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == "circle":
            return Circle(*args)
        elif shape_type == "rectangle":
            return Rectangle(*args)
        else:
            raise ValueError("不支持的图形类型")


# 图形管理系统核心
class ShapeManager:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape_type, *args):
        shape = ShapeFactory.create_shape(shape_type, *args)
        self.shapes.append(shape)

    def calculate_total_area(self):
        return sum(shape.area() for shape in self.shapes)


# 测试
manager = ShapeManager()
manager.add_shape("circle", 5)
manager.add_shape("rectangle", 3, 4)
print(manager.calculate_total_area())  # 84.5
