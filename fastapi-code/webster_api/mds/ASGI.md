**ASGI** 是：

> **Asynchronous Server Gateway Interface**
> **异步服务器网关接口**

它是 **Python Web 服务器 和 Web 应用之间的一套“标准协议”**，可以理解为 **WSGI 的升级版（异步版）**。

---

## 一句话解释（面试速答版）

> **ASGI 是一套支持异步的 Python Web 应用接口规范，用来定义 Web 服务器（如 Uvicorn）和 Web 框架（如 FastAPI）之间如何通信，它支持
HTTP、WebSocket 等多种协议。**

---

## 一、ASGI 解决了什么问题？

在 ASGI 之前，Python Web 世界主要用的是 **WSGI**：

|        | WSGI         | ASGI               |
|--------|--------------|--------------------|
| 是否支持异步 | ❌ 不支持        | ✅ 原生支持             |
| 并发模型   | 同步、阻塞        | 异步、非阻塞             |
| 支持协议   | 仅 HTTP       | HTTP、WebSocket、SSE |
| 代表框架   | Flask、Django | FastAPI、Starlette  |

👉 **WSGI 时代的问题**：

* 一个请求占一个线程
* WebSocket / 长连接基本没法优雅支持
* 高并发下线程成本高

**ASGI 就是为了解决这些问题而出现的。**

---

## 二、ASGI 的核心思想（非常重要）

### ASGI ≈ 事件驱动 + 协程

ASGI 定义了一个统一的调用形式：

```python
async def app(scope, receive, send):
    ...
```

这三个参数分别代表：

| 参数        | 含义                            |
|-----------|-------------------------------|
| `scope`   | 连接的元信息（协议、路径、headers 等）       |
| `receive` | 用来 **接收事件**（请求体、WebSocket 消息） |
| `send`    | 用来 **发送事件**（响应、推送消息）          |

📌 所有请求、本质上都是 **事件流**

---

## 三、ASGI 架构图（文字版）

```
浏览器
   ↓
Uvicorn / Hypercorn  (ASGI Server)
   ↓
FastAPI / Starlette (ASGI App)
   ↓
async def endpoint()
```

* **Uvicorn**：负责网络通信、事件循环
* **FastAPI**：负责路由、依赖注入、业务逻辑
* 它们通过 **ASGI 协议** 解耦

---

## 四、为什么 FastAPI 一定要用 ASGI？

因为 FastAPI 的核心能力：

* `async / await`
* 高并发
* WebSocket
* Streaming Response
* BackgroundTask

👉 **全部依赖 ASGI**

如果没有 ASGI：

```python
async def endpoint():
    await db.query()  # ❌ 没意义
```

---

## 五、ASGI vs WSGI（面试必考对比）

### WSGI 示例（同步）

```python
def application(environ, start_response):
    start_response('200 OK', [])
    return [b"hello"]
```

* 同一时间只能处理一个请求
* 遇到 I/O 就阻塞

---

### ASGI 示例（异步）

```python
async def application(scope, receive, send):
    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": []
    })
    await send({
        "type": "http.response.body",
        "body": b"hello"
    })
```

* I/O 不阻塞
* 可同时处理成千上万连接

---

## 六、ASGI 能支持哪些场景？

| 场景        | WSGI | ASGI |
|-----------|------|------|
| REST API  | ✅    | ✅    |
| 高并发       | ❌    | ✅    |
| WebSocket | ❌    | ✅    |
| 长连接       | ❌    | ✅    |
| 实时推送      | ❌    | ✅    |
| SSE       | ❌    | ✅    |

---

## 七、FastAPI + ASGI 的真实价值（面试加分）

你可以这样总结 👇

> FastAPI 基于 ASGI 协议，使得整个框架天生支持异步 I/O 和事件驱动模型，从而在高并发、实时通信和微服务场景下，比传统 WSGI
> 框架有更好的性能和扩展性。

---

## 八、一句话记忆法

> **ASGI 是 Python Web 的“异步底座”，FastAPI 是站在 ASGI 上的现代 Web 框架。**

---