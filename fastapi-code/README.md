# FastAPI 学习与示例项目

本项目是一个用于学习FastAPI框架和Python编程的综合示例仓库，包含了基础API开发、Python语法特性、设计模式实现以及实用工具函数等内容。

## 项目结构

```
fastapi-code/
├── INSTALLROOT/              # 安装相关配置
│   └── app/
│       └── requirements.txt  # 项目依赖
├── __pycache__/              # Python编译缓存
├── syntax_code/              # Python语法特性示例
│   ├── keywords/             # 关键字用法示例
│   │   ├── function_signatures/  # 函数签名示例
│   │   └── yield/            # yield关键字用法
│   ├── singleton/            # 单例设计模式实现
│   ├── static/               # 静态资源
│   ├── tips_markdown/        # 技术提示文档
│   └── utils/                # 实用工具函数
│       └── decorator/        # 装饰器实现
└── webster_api/              # FastAPI应用示例
    ├── __pycache__/          # Python编译缓存
    ├── main.py               # 应用主入口
    ├── routers/              # API路由定义
    └── study-code/           # FastAPI学习示例代码
```

## 主要模块说明

### webster_api

这是一个基本的FastAPI应用示例，展示了如何创建API路由和处理HTTP请求。

- **main.py**: 应用入口点，初始化FastAPI应用并注册路由
- **routers/**: 包含定义API端点的路由文件
    - **item.py**: 处理item相关的API请求
    - **response.py**: 展示如何操作HTTP响应
- **study-code/**: 包含大量FastAPI学习示例，涵盖：
    - 依赖注入
    - 请求参数处理
    - 表单数据处理
    - 安全认证
    - 响应模型
    - 异常处理
    - 依赖注入进阶用法
    - 以及更多FastAPI特性...

### syntax_code

这个模块包含Python语法特性和设计模式的示例代码。

- **keywords/**: 展示Python关键字的高级用法
    - **function_signatures/**: 函数签名和类型提示示例
    - **yield/**: yield关键字和生成器用法示例
- **singleton/**: 多种单例模式实现方式
- **utils/decorator/**: 各种实用装饰器实现
    - 缓存装饰器
    - 日志装饰器
    - 重试装饰器
    - 验证参数装饰器
    - 以及更多...
- **tips_markdown/**: Markdown格式的技术提示和最佳实践

## 快速开始

### 安装依赖

```bash
cd E:\python-code\fastapi-code\INSTALLROOT\app
pip install -r requirements.txt
```

### 运行Webster API

```bash
cd E:\python-code\fastapi-code\webster_api
python main.py
```

然后访问：

- API文档: http://127.0.0.1:8000/docs
- ReDoc文档: http://127.0.0.1:8000/redoc

## API端点

### Item 路由

- **GET /item/items/**: 获取所有items
- **GET /item/headers-and-object/**: 获取带自定义头部的响应

## 学习资源

### FastAPI 核心概念示例

在`webster_api/study-code/`目录中包含了大量FastAPI学习示例，包括但不限于：

- **依赖注入** (`dependency_injection.py`): 展示FastAPI强大的依赖注入系统
- **路径参数** (`path_parameter.py`): 演示如何处理URL路径参数
- **查询参数** (`query_parameter.py`): 展示查询参数的使用方法
- **请求体** (`req_body.py`): 演示如何处理和验证请求体
- **响应模型** (`resp_model_return_type.py`): 展示如何定义和使用响应模型
- **异常处理** (`handle_error.py`): 演示错误处理机制
- **安全认证** (`Bearer_password.py`, `security_first.py`): 展示认证和授权机制

### Python 高级特性

在`syntax_code/`目录中包含了Python高级特性的示例：

- **装饰器** (`utils/decorator/`): 多种实用装饰器的实现和用法
- **生成器和yield** (`keywords/yield/`): 展示生成器的使用和内存优化
- **设计模式** (`singleton/`): 单例模式的多种实现方式

## 技术栈

- **Python**: 3.10+
- **FastAPI**: 高性能的现代Web框架
- **Uvicorn**: ASGI服务器
- **Pydantic**: 数据验证和设置管理

## 贡献指南

欢迎提交Issue和Pull Request！
        