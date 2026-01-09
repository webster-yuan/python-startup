---

# 📁 infrastructure/README.md

# Infrastructure 层设计规范

## 一、Infrastructure 层是什么？

Infrastructure 层用于封装 **外部系统能力（External Dependencies）**，  
是业务系统与外部世界之间的“适配层”。

这些外部系统包括但不限于：

- Redis / Memcached
- 消息队列（Kafka / RabbitMQ）
- 第三方 HTTP API
- 搜索引擎（Elasticsearch）
- 分布式锁 / 幂等组件
- 对象存储（S3 / OSS）

Infrastructure 层 **不包含业务决策逻辑**，只提供“能力”。

---

## 二、Infrastructure 层的职责

### Infrastructure 层应该做的事情

- 封装外部系统的连接与配置
- 提供清晰、稳定的调用接口
- 屏蔽底层实现细节（SDK / 协议）
- 统一外部系统的异常类型
- 便于替换实现（如 Redis → Memcached）

### Infrastructure 层不应该做的事情

- 不包含业务语义判断
- 不直接依赖 HTTP Router
- 不直接返回 HTTP Response
- 不决定事务提交或回滚
- 不访问数据库（除非是基础设施自身需要）

---

## 三、推荐的目录结构

```text
infrastructure/
├── redis/
│   ├── client.py      # 连接与配置
│   ├── cache.py       # Redis 操作封装
│   └── README.md
├── mq/
│   ├── producer.py
│   ├── consumer.py
│   └── README.md
├── http/
│   ├── client.py      # 第三方 HTTP Client
│   └── README.md
├── lock/
│   ├── distributed.py
│   └── README.md
└── README.md
````

---

## 四、函数设计规范

### 函数风格

* 推荐使用 **函数式风格**
* 不强制封装为类
* 一个函数只提供一个明确能力

```python
def get_hero_cache(...)


    def set_hero_cache(...)
```

---

### 入参规范

* 使用基础类型或简单结构
* 不接收 ORM Model
* 不接收 Pydantic Schema（除非是纯数据结构）

---

### 返回值规范

* 返回基础类型（dict / list / str / bool）
* 或返回 Infrastructure 自己定义的数据结构
* 不返回 ORM Model
* 不返回 HTTP Response

---

## 五、异常处理规范

### Infrastructure 层异常原则

* 可以抛出“基础设施异常”（如 RedisError、TimeoutError）
* 不捕获并吞掉异常
* 不抛 HTTPException
* 不返回错误码

推荐做法：

* Infrastructure 层抛出 **技术异常**
* Service 层将其包装为 **业务异常**

---

## 六、示例

### Redis 示例

```python
def get_hero_cache(hero_id: int) -> dict | None:
    return redis_client.get(f"hero:{hero_id}")
```

```python
def set_hero_cache(hero_id: int, data: dict, ttl: int = 60):
    redis_client.setex(f"hero:{hero_id}", ttl, data)
```

---

## 七、反例（禁止）

```python
# ❌ 错误示例
def get_hero_cache(hero_id: int):
    if not redis_client.exists(...):
        raise HeroNotFoundError()  # ❌ 业务异常不属于这里
```

---

## 八、与 Service 层的关系

```text
Service
  ↓ 调用
Infrastructure
  ↓ 封装
External System
```

Infrastructure 层只提供能力，
**是否调用、何时调用、调用失败如何处理，全部由 Service 决定。**

---

## 九、一句话总结

> **Infrastructure 层解决“怎么接入外部系统”，
> Service 层解决“业务上要不要用它”**

```

---

# 🧠 总体架构闭环总结（送你一句压轴）

> **Router / Service / CRUD / Infrastructure  
> 是一条“不可逆的数据与职责流向”**
