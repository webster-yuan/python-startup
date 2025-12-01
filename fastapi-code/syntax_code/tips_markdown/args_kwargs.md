## *args：处理可变数量的位置参数
作用：将多个位置参数打包成一个元组（tuple）。
*args 是Python的语法糖，用于将多个位置参数打包成一个元组（tuple）。

类比C++：类似于C++中的可变参数模板（variadic templates），但更简单直观。

示例：

```python
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3))  # 输出 6
print(sum_numbers(4, 5))     # 输出 9
```
这里 *args 会收集所有传入的位置参数（如 1, 2, 3）并组成元组 (1, 2, 3)。

**kwargs：处理可变数量的关键字参数
作用：将多个关键字参数打包成一个字典（dictionary）。

类比C++：类似C++中的命名参数（Python没有直接等价，但可以想象为键值对的集合）。

示例：

```python
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=30, role="admin")
# 输出:
# name: Alice
# age: 30
# role: admin
```
## **kwargs 会收集所有关键字参数（如 name="Alice"）并组成字典 {"name": "Alice", ...}。
行为：**kwargs 用于将多个关键字参数打包成一个字典（dict）。

底层机制：

调用 func(a=1, b=2) 时，kwargs 会被转换为 {"a": 1, "b": 2}。

字典是可变的，类似于C++中的 std::unordered_map。
* 总结：*args 和 **kwargs 的核心用途
语法	类型	数据结构	用途
*args	位置参数	元组	接收不确定数量的位置参数
**kwargs	关键字参数	字典	接收不确定数量的关键字参数
使用场景：
装饰器：让装饰器能适配不同参数数量的函数。

继承：在子类中扩展父类方法时保留参数。

通用函数：编写可接受任意参数的函数（如日志记录、权限校验等）。

## 总结：Python与C++的关键区别
特性	Python (*args/**kwargs)	C++
参数传递方式	自动打包为元组或字典	需显式使用模板或容器（如std::tuple）
内存管理	自动垃圾回收	手动管理（需注意指针和生命周期）
类型灵活性	动态类型（任意类型混合）	静态类型（需提前声明类型）
可变参数实现	语法糖（隐式解包/打包）	模板或va_list（显式操作）****