我按 **Python 语言层 → FastAPI 依赖注入** 这个顺序，给你一个**清晰、可记忆、适合面试**的答案。

---

## 一、什么叫「可调用对象（callable）」？

在 Python 里：

> **只要一个对象能用 `()` 调用，它就是可调用对象**

判断方式只有一个：

```python
callable(obj)
```

返回 `True`，就是可调用对象。

---

## 二、Python 中「可调用对象」的完整分类（重点）

### 1️⃣ 函数（最常见 ✅）

```python
def get_user():
    return "user"


get_user()  # ✅
callable(get_user)  # True
```

📌 **FastAPI 中最常用的依赖形式**

```python
def get_db():
    return "db"


Depends(get_db)
```

---

### 2️⃣ 方法（本质也是函数）

```python
class Service:
    def run(self):
        pass


s = Service()
s.run()  # ✅
callable(s.run)  # True
```

📌 FastAPI 很少直接用，但语义上是成立的

---

### 3️⃣ 类（⚠️很多人第一次会懵）

```python
class MyDep:
    def __init__(self):
        pass


MyDep()  # ✅
callable(MyDep)  # True
```

📌 原因：
**类被调用时，本质是在调用 `__init__`**

#### 在 FastAPI 里非常重要 👇

```python
class Settings:
    def __init__(self):
        self.debug = True


def endpoint(settings=Depends(Settings)):
    return settings.debug
```

✔️ FastAPI 会自动：

* 实例化类
* 把实例注入进来

---

### 4️⃣ 实现了 `__call__` 的对象（高级但非常重要 ⭐）

```python
class TokenValidator:
    def __call__(self, token: str):
        return token == "secret"


validator = TokenValidator()

validator("secret")  # ✅
callable(validator)  # True
```

📌 **这是 FastAPI 里写“高级依赖”的核心方式**

```python
validator = TokenValidator()


def endpoint(
        ok: bool = Depends(validator)
):
    return ok
```

👉 常用于：

* 权限校验
* 认证
* 复杂依赖状态

---

### 5️⃣ lambda 表达式（不推荐但合法）

```python
Depends(lambda: "value")
```

⚠️ **能用，但不推荐**

* 不利于调试
* 文档不友好
* 类型提示差

---

### 6️⃣ 内建可调用对象（少见）

```python
callable(len)  # True
callable(print)  # True
```

📌 理论上可以，但 FastAPI 中基本不用

---

## 三、总结一张「Depends 能用什么」的表（重点记）

| 类型                | 是否可用于 Depends | 常用程度  |
|-------------------|---------------|-------|
| 普通函数              | ✅             | ⭐⭐⭐⭐⭐ |
| 方法                | ✅             | ⭐⭐    |
| 类                 | ✅             | ⭐⭐⭐⭐  |
| 实现 `__call__` 的对象 | ✅             | ⭐⭐⭐⭐⭐ |
| lambda            | ✅             | ⭐     |
| 内建函数              | ✅             | ⭐     |

---

## 四、FastAPI 角度的「本质一句话」

你可以这样理解 Depends 👇

> **Depends 接收的不是“值”，而是一个“如何产生值的可调用对象”**

FastAPI 会：

1. 调用它
2. 解析参数（依赖嵌套）
3. 注入返回值

---

## 五、面试一句话标准答案（直接背）

> 在 Python 中，只要对象实现了 `__call__`，或者本身就是函数、方法或类，就属于可调用对象。FastAPI 的 Depends
> 可以接收任意可调用对象，包括函数、类以及实现了 `__call__` 的实例，FastAPI 会负责调用并将返回结果注入到接口函数中。

---

## 六、你现在这个阶段「最值得掌握的 3 种」

我给你一个**学习优先级**：

1. ✅ 普通函数（必须会）
2. ✅ 类作为依赖（非常常用）
3. ✅ `__call__` 对象（进阶依赖）

其他的你知道存在即可。

---