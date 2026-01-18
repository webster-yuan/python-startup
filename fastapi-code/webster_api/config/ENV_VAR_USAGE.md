# 环境变量使用指南

## 概述

本项目使用 `pydantic-settings` 管理配置，**环境变量优先级最高**，适用于 Kubernetes ConfigMap/Secret 注入的场景。

## 环境变量读取机制

### 自动读取

`pydantic-settings` 的 `BaseSettings` 会自动从环境变量读取配置，无需额外代码。

### 环境变量命名规则

- 环境变量名与配置字段名对应（不区分大小写）
- 支持大写、小写、混合大小写
- 示例：
  - `DATABASE_URL` → `database_url` 字段
  - `database_url` → `database_url` 字段
  - `Database_Url` → `database_url` 字段

### 配置项对应的环境变量

| 配置字段 | 环境变量名 | 示例值 |
|---------|-----------|--------|
| `app_name` | `APP_NAME` | `Webster API` |
| `api_host` | `API_HOST` | `0.0.0.0` |
| `api_port` | `API_PORT` | `8000` |
| `debug` | `DEBUG` | `false` |
| `reload` | `RELOAD` | `false` |
| `database_url` | `DATABASE_URL` | `postgresql://user:pass@host:5432/db` |
| `sqlite_check_same_thread` | `SQLITE_CHECK_SAME_THREAD` | `false` |
| `cors_origins` | `CORS_ORIGINS` | `https://yourdomain.com` |
| `cors_allow_credentials` | `CORS_ALLOW_CREDENTIALS` | `true` |
| `cors_allow_methods` | `CORS_ALLOW_METHODS` | `*` |
| `cors_allow_headers` | `CORS_ALLOW_HEADERS` | `*` |
| `log_level` | `LOG_LEVEL` | `INFO` |
| `log_file` | `LOG_FILE` | `logs/app.log` |

## 使用场景

### 1. 本地开发测试（使用 .env 文件）

```bash
# 复制示例文件
cp env.example .env

# 编辑 .env 文件
vim .env

# 运行应用（自动读取 .env）
python main.py
```

### 2. 命令行设置环境变量

```bash
# Linux/Mac
export DATABASE_URL="postgresql://user:pass@localhost:5432/webster_db"
export API_PORT=8080
python main.py

# Windows PowerShell
$env:DATABASE_URL="postgresql://user:pass@localhost:5432/webster_db"
$env:API_PORT="8080"
python main.py
```

### 3. Kubernetes ConfigMap 注入

**创建 ConfigMap：**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: webster-api-config
  namespace: default
data:
  APP_NAME: "Webster API"
  API_HOST: "0.0.0.0"
  API_PORT: "8000"
  DEBUG: "false"
  DATABASE_URL: "postgresql://user:pass@postgres:5432/webster_db"
  CORS_ORIGINS: "https://yourdomain.com"
  LOG_LEVEL: "INFO"
```

**在 Deployment 中使用：**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webster-api
spec:
  template:
    spec:
      containers:
      - name: webster-api
        image: webster-api:latest
        envFrom:
        - configMapRef:
            name: webster-api-config
```

### 4. Kubernetes Secret 注入（敏感信息）

**创建 Secret：**

```bash
kubectl create secret generic webster-api-secrets \
  --from-literal=DATABASE_URL='postgresql://user:password@postgres:5432/webster_db' \
  --from-literal=SECRET_KEY='your-secret-key'
```

**在 Deployment 中使用：**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webster-api
spec:
  template:
    spec:
      containers:
      - name: webster-api
        envFrom:
        - secretRef:
            name: webster-api-secrets
```

## 验证环境变量读取

### 测试脚本

创建测试文件 `test_config.py`：

```python
import os
from webster_api.config import settings

# 设置环境变量
os.environ["API_PORT"] = "9999"
os.environ["DATABASE_URL"] = "test://test:test@test:9999/test"

# 重新加载配置（注意：在测试中可能需要重新实例化）
from webster_api.config.settings import Settings
test_settings = Settings()

print(f"API Port (from env): {test_settings.api_port}")  # 应该是 9999
print(f"Database URL (from env): {test_settings.database_url}")  # 应该是 test://...
```

### 在代码中检查

```python
from webster_api.config import settings
import os

# 打印当前配置值
print(f"Database URL: {settings.database_url}")

# 打印环境变量（如果存在）
env_db_url = os.environ.get("DATABASE_URL")
print(f"Environment DATABASE_URL: {env_db_url}")

# 判断配置来源
if env_db_url and env_db_url == settings.database_url:
    print("配置来自环境变量")
elif settings.database_url == "sqlite:///db/database.db":
    print("配置来自默认值")
else:
    print("配置来自 .env 文件")
```

## 注意事项

1. **环境变量优先级最高**：K8s 注入的环境变量会覆盖 `.env` 文件
2. **类型转换**：`pydantic-settings` 会自动进行类型转换（字符串 → int/bool 等）
3. **布尔值**：环境变量中的布尔值使用字符串 `"true"` / `"false"`
4. **列表值**：CORS 相关的列表值用逗号分隔（如 `http://a.com,http://b.com`）

## 调试技巧

### 查看实际加载的配置

在 `main.py` 启动时打印配置：

```python
from webster_api.config import settings

print("=== 配置信息 ===")
print(f"App Name: {settings.app_name}")
print(f"API Host: {settings.api_host}")
print(f"API Port: {settings.api_port}")
print(f"Database URL: {settings.database_url}")
print(f"Debug Mode: {settings.debug}")
```

### 使用环境变量调试

```bash
# 临时覆盖配置运行
DATABASE_URL="postgresql://test:test@localhost:5432/test" python main.py
```
