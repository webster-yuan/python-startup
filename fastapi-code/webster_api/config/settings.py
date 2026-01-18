"""
配置管理模块
使用 pydantic-settings 管理应用配置

配置读取优先级（从高到低）：
1. 环境变量（Environment Variables）- 最高优先级
   - 适用于 K8s ConfigMap/Secret 注入
   - 适用于 CI/CD 环境
   - 命令行设置：export DATABASE_URL=xxx
2. .env 文件 - 中间优先级
   - 适用于本地开发测试
   - 开发环境使用 env.example 作为模板
3. 代码默认值 - 最低优先级
   - 仅在环境变量和 .env 都未设置时使用

在 Kubernetes 中部署时：
- ConfigMap 和 Secret 会通过环境变量注入到 Pod
- 环境变量的值会覆盖 .env 文件中的配置
- 这确保了生产环境配置由 K8s 统一管理
"""
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """应用配置类"""
    
    # ============ 应用基础配置 ============
    # 应用名称
    app_name: str = "Webster API"
    
    # API 主机地址
    api_host: str = "127.0.0.1"
    
    # API 端口
    api_port: int = 8000
    
    # 是否开启调试模式
    debug: bool = False
    
    # 是否开启自动重载（开发环境）
    reload: bool = False
    
    # ============ 数据库配置 ============
    # 数据库 URL
    # SQLite 示例: sqlite:///db/database.db
    # PostgreSQL 示例: postgresql://user:password@localhost/dbname
    # MySQL 示例: mysql://user:password@localhost/dbname
    database_url: str = "sqlite:///db/database.db"
    
    # SQLite 连接参数
    sqlite_check_same_thread: bool = False
    
    # ============ CORS 配置 ============
    # 允许的来源列表，多个用逗号分隔
    cors_origins: str = "http://localhost:3000"
    
    # 是否允许携带 Cookie
    cors_allow_credentials: bool = True
    
    # 允许的 HTTP 方法，多个用逗号分隔
    cors_allow_methods: str = "*"
    
    # 允许的请求头，多个用逗号分隔
    cors_allow_headers: str = "*"
    
    # ============ 日志配置 ============
    # 日志级别: DEBUG, INFO, WARNING, ERROR, CRITICAL
    log_level: str = "INFO"
    
    # 日志文件路径（可选）
    log_file: str | None = None
    
    # ============ 模型配置 ============
    model_config = SettingsConfigDict(
        # 从 .env 文件读取配置（仅当环境变量未设置时）
        # 环境变量优先级高于 .env 文件
        env_file=".env",
        env_file_encoding="utf-8",  # .env 文件编码
        case_sensitive=False,  # 环境变量名不区分大小写（DATABASE_URL 和 database_url 等价）
        extra="ignore",  # 忽略未定义的配置项
        
        # 注意：BaseSettings 默认会从环境变量读取配置
        # 这是 pydantic-settings 的内置行为，无需额外配置
        # 环境变量名称与字段名一致（不区分大小写）
        # 例如：DATABASE_URL 环境变量会映射到 database_url 字段
    )
    
    @property
    def cors_origins_list(self) -> List[str]:
        """将 CORS origins 字符串转换为列表"""
        if self.cors_origins == "*":
            return ["*"]
        return [origin.strip() for origin in self.cors_origins.split(",")]
    
    @property
    def cors_allow_methods_list(self) -> List[str]:
        """将 CORS methods 字符串转换为列表"""
        if self.cors_allow_methods == "*":
            return ["*"]
        return [method.strip() for method in self.cors_allow_methods.split(",")]
    
    @property
    def cors_allow_headers_list(self) -> List[str]:
        """将 CORS headers 字符串转换为列表"""
        if self.cors_allow_headers == "*":
            return ["*"]
        return [header.strip() for header in self.cors_allow_headers.split(",")]


# 创建全局配置实例
# 初始化时会按照优先级顺序读取配置：
# 1. 首先检查环境变量（os.environ）
# 2. 如果环境变量不存在，检查 .env 文件
# 3. 如果都不存在，使用代码中的默认值
settings = Settings()
