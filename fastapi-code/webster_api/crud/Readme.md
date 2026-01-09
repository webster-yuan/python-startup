---

# 📁 crud/README.md

# CRUD 层设计规范

## 一、CRUD 层的职责

CRUD 层负责 **数据持久化操作**，是系统与数据库之间的唯一通道。

### CRUD 层应该做的事情

- 执行数据库读写操作
- 使用 ORM / SQL 表达数据访问
- 返回数据库 Model 或基础数据结构
- 提供最小、可复用的数据操作单元

### CRUD 层不应该做的事情

- 不包含业务语义判断
- 不抛业务异常
- 不抛 HTTPException
- 不进行事务提交或回滚
- 不关心调用方是 Service 还是其他模块

---

## 二、CRUD 层函数设计规范

### 函数形式

- 使用 **函数式风格**
- 一个函数只做一件数据操作
- 函数命名以数据行为为主，而非业务行为

```python
get_hero_by_id(...)
create_hero(...)
delete_hero(...)
list_heros(...)
````

---

### 入参规范

* 接收数据库 Session
* 接收数据库 Model 或基础类型
* 不接收 HTTP Request / Schema

---

### 返回值规范

* 返回 ORM Model
* 或返回列表 / 基础类型
* 不返回 Schema

---

## 三、异常处理约定

### CRUD 层异常原则

* 允许抛出数据库异常（IntegrityError 等）
* 不捕获异常
* 不包装异常
* 由上层 Service 决定如何处理

---

## 四、示例

```python
def get_hero_by_id(session: Session, hero_id: int) -> Hero | None:
    statement = select(Hero).where(Hero.id == hero_id)
    return session.exec(statement).first()
```

---

## 五、反例（禁止）

```python
# ❌ 错误示例
def delete_hero(session: Session, hero_id: int):
    hero = get_hero_by_id(session, hero_id)
    if not hero:
        raise HTTPException(status_code=404)  # ❌
```

---

## 六、一句话总结

> **CRUD 层是数据库的“翻译器”，而不是业务的决策者**
