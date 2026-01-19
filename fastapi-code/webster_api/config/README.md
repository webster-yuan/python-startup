# 配置管理模块

## 概述

本模块使用 `pydantic-settings` 管理应用配置，支持从环境变量和 `.env` 文件读取配置。

## 使用方法

### 1. 创建 .env 文件

在 `webster_api` 目录下创建 `.env` 文件，参考 `.env.example`：

```bash
cp .env.example .env
```

### 2. 配置项说明

#### 应用基础配置

- `APP_NAME`: 应用名称，默认 `Webster API`
- `API_HOST`: API 主机地址，默认 `127.0.0.1`
- `API_PORT`: API 端口，默认 `8000`
- `DEBUG`: 是否开启调试模式，默认 `false`
- `RELOAD`: 是否开启自动重载，默认 `false`

#### 数据库配置

- `DATABASE_URL`: 数据库连接 URL
  - SQLite: `sqlite:///db/database.db`
  - PostgreSQL: `postgresql://user:password@localhost:5432/dbname`
  - MySQL: `mysql://user:password@localhost:3306/dbname`
- `SQLITE_CHECK_SAME_THREAD`: SQLite 线程检查，默认 `false`

#### CORS 配置

- `CORS_ORIGINS`: 允许的来源，多个用逗号分隔，默认 `http://localhost:3000`
- `CORS_ALLOW_CREDENTIALS`: 是否允许携带 Cookie，默认 `true`
- `CORS_ALLOW_METHODS`: 允许的 HTTP 方法，默认 `*`（所有）
- `CORS_ALLOW_HEADERS`: 允许的请求头，默认 `*`（所有）

#### 日志配置

- `LOG_LEVEL`: 日志级别（DEBUG/INFO/WARNING/ERROR/CRITICAL），默认 `INFO`
- `LOG_FILE`: 日志文件路径（可选）

### 3. 在代码中使用配置

```python
from webster_api.config import settings

# 使用配置
print(settings.app_name)
print(settings.database_url)
print(settings.cors_origins_list)  # 自动转换为列表
```

### 4. 多环境配置

可以通过设置不同的 `.env` 文件来支持多环境：

- **开发环境**: `.env.development` 或 `.env`
- **测试环境**: `.env.test`
- **生产环境**: `.env.production`

在不同环境部署时，复制对应的 `.env` 文件为 `.env` 即可。

或者通过环境变量 `ENV_FILE` 指定：

```bash
export ENV_FILE=.env.production
python main.py
```

## 配置优先级

**pydantic-settings 的配置读取顺序（从高到低）：**

1. **环境变量（Environment Variables）** - 最高优先级 ⭐
   - 适用于 Kubernetes ConfigMap/Secret 注入
   - 适用于 CI/CD 环境
   - 命令行设置示例：`export DATABASE_URL=postgresql://...`

2. **.env 文件** - 中间优先级
   - 适用于本地开发测试
   - 开发时使用 `env.example` 作为模板创建 `.env`

3. **代码默认值** - 最低优先级
   - 仅在环境变量和 `.env` 都未设置时使用

## Kubernetes 部署说明

在 Kubernetes 中部署时，ConfigMap 和 Secret 会通过环境变量注入到 Pod：

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
        - configMapRef:
            name: webster-api-config  # ConfigMap 中的配置会注入为环境变量
        - secretRef:
            name: webster-api-secrets  # Secret 中的敏感信息会注入为环境变量
```

**ConfigMap 示例（webster-api-config.yaml）：**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: webster-api-config
data:
  APP_NAME: "Webster API"
  API_HOST: "0.0.0.0"
  API_PORT: "8000"
  DEBUG: "false"
  DATABASE_URL: "postgresql://user:pass@postgres:5432/webster_db"
  CORS_ORIGINS: "https://yourdomain.com"
  LOG_LEVEL: "INFO"
```

**关键点：**
- ConfigMap/Secret 注入的环境变量会**覆盖** `.env` 文件中的配置
- 这确保了生产环境配置由 K8s 统一管理，而非应用内文件
- 本地开发时仍可使用 `.env` 文件，不会影响 K8s 部署

## 示例

### 开发环境配置 (.env)

```env
DEBUG=true
RELOAD=true
DATABASE_URL=sqlite:///db/database.db
LOG_LEVEL=DEBUG
```

### 生产环境配置 (.env.production)

```env
DEBUG=false
RELOAD=false
DATABASE_URL=postgresql://user:password@localhost:5432/webster_db
LOG_LEVEL=INFO
CORS_ORIGINS=https://yourdomain.com
```
