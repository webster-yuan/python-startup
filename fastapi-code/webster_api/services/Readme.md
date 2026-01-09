---

# 📁 services/README.md

# Service 层设计规范

## 一、Service 层的职责

Service 层用于承载 **业务流程（Business Flow）**，位于 Router 与 CRUD 之间，是系统的核心协调层。

### Service 层应该做的事情

- 承载业务语义（如：创建英雄、发布订单、冻结账户）
- 协调多个 CRUD 操作
- 协调多个外部资源（DB / Redis / MQ / 第三方 API）
- 进行 Schema ↔ Model 的转换
- 决定事务边界（是否提交 / 回滚）
- 抛出业务异常（Business Exception）

### Service 层不应该做的事情

- 不直接处理 HTTP 细节（Request / Response）
- 不返回数据库 Model 给 Router
- 不直接写 SQL
- 不依赖 FastAPI 的具体实现（如 Depends）

---

## 二、Service 层函数设计规范

### 函数形式

- 推荐使用 **函数式风格**
- 不强制封装为类
- 函数命名应体现业务含义，而不是技术含义

```python
def create_hero_service(...)


    def delete_hero_service(...)

    def list_heros_service(...)
````

### 入参规范

* 接收 Schema（如 `HeroCreate`、`HeroUpdate`）
* 接收基础类型（int / str / bool 等）
* 接收数据库 Session

### 返回值规范

* 返回 Read Schema（如 `HeroRead`）
* 或返回业务所需的结构体
* 不返回 ORM Model

---

## 三、事务管理约定

### 事务边界

* Service 层是事务的逻辑边界
* 实际的 commit / rollback 推荐由依赖注入统一管理

```text
正常执行 → commit
抛出异常 → rollback
```

Service 层无需显式调用 `commit()`，除非特殊场景。

---

## 四、异常处理规范

### Service 层可以抛出的异常类型

* 业务异常（如：资源不存在、状态不合法）
* 下游依赖异常的业务封装版本

### 不允许的异常行为

* 不抛 `HTTPException`
* 不直接返回错误码
* 不吞异常（必须明确抛出）

---

## 五、示例

```python
def delete_hero_service(session: Session, hero_id: int):
    hero = get_hero_by_id(session, hero_id)
    if not hero:
        raise HeroNotFoundError()

    delete_hero(session, hero)
```

---

## 六、一句话总结

> **Service 层是“业务语言”的载体，而不是技术细节的堆放地**



