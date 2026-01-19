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
import logging
import os
import json
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """应用配置类"""
    
    # ============ 应用基础配置 ============
    # 应用名称
    app_name: str = "Webster API"

    # 运行环境：development / production
    # 企业实践：是否为生产环境不应仅用 debug 推断，而应显式由部署注入
    environment: str = "development"
    
    # API 主机地址
    api_host: str = "127.0.0.1"
    
    # API 端口
    api_port: int = 8000
    
    # 是否开启调试模式
    debug: bool = False
    
    # 是否开启自动重载（开发环境）
    reload: bool = False

    # ============ 代理/真实客户端 IP 配置 ============
    # 是否信任代理头（X-Forwarded-For / X-Real-IP）
    # 仅当 request.client.host 位于 trusted_proxies 中才会使用这些头，防止伪造
    trust_proxy_headers: bool = False
    # 可信代理列表（逗号分隔，支持 IP 或 CIDR）
    # 示例: "127.0.0.1,10.0.0.0/8,192.168.0.0/16"
    trusted_proxies: str = "127.0.0.1"
    
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
    
    # ============ JWT 认证配置 ============
    # JWT 密钥（用于签名和验证 token）
    # ⚠️ 生产环境必须使用强随机密钥，推荐通过 Secret 注入
    # 默认值仅用于开发环境，生产环境必须通过环境变量设置
    secret_key: str = "your-secret-key-change-in-production"
    
    # JWT 算法
    algorithm: str = "HS256"

    # JWT issuer / audience（企业基线：强校验）
    jwt_issuer: str = "webster-api"
    jwt_audience: str = "webster-api"

    # JWT key rotation support
    # - kid will be written into JWT header when signing
    # - old keys can be provided via JWT_KEYRING_JSON for multi-key verification
    jwt_signing_kid: str = "default"
    # JSON object string, e.g. {"default":"<current>","v0":"<old-key>"}
    jwt_keyring_json: str = ""
    
    # Access Token 过期时间（分钟）
    # 企业常用做法：access token 短时效（例如 5~15 分钟），logout 只撤销 refresh
    access_token_expire_minutes: int = 10
    
    # Refresh Token 过期时间（天）
    # 默认 7 天
    refresh_token_expire_days: int = 7
    
    # Token 前缀（用于 Authorization header）
    token_prefix: str = "Bearer"
    
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

    @property
    def trusted_proxies_list(self) -> List[str]:
        """将 trusted_proxies 字符串转换为列表"""
        return [p.strip() for p in self.trusted_proxies.split(",") if p.strip()]

    @property
    def jwt_keyring(self) -> dict[str, str]:
        """
        Keyring for JWT verification (kid -> key).

        - Always includes current signing key under jwt_signing_kid.
        - jwt_keyring_json can provide additional/old keys for verification during rotation.
        """
        ring: dict[str, str] = {}
        if self.jwt_keyring_json:
            try:
                parsed = json.loads(self.jwt_keyring_json)
                if isinstance(parsed, dict):
                    for k, v in parsed.items():
                        if isinstance(k, str) and isinstance(v, str) and k and v:
                            ring[k] = v
            except Exception:
                # Ignore invalid json; keep minimal ring
                pass

        # Ensure current signing key is always present
        ring[self.jwt_signing_kid] = self.secret_key
        return ring
    
    def validate_secret_key(self) -> None:
        """
        验证 secret_key 配置
        
        企业实践：
        - 是否为生产环境由 environment 显式控制（development/production）
        - production 环境禁止使用默认 SECRET_KEY（直接阻止启动）
        - development 环境仅告警，便于学习/本地启动
        
        Raises:
            ValueError: 如果 secret_key 不符合安全要求
        """
        default_key = "your-secret-key-change-in-production"
        env = (self.environment or "").strip().lower()
        is_production = env in {"prod", "production"}
        
        # 检查是否使用默认密钥
        if self.secret_key == default_key:
            if is_production:
                # 生产环境使用默认密钥是严重的安全问题（阻止启动）
                error_msg = (
                    "CRITICAL SECURITY WARNING: Using default SECRET_KEY in production! "
                    "Please set a strong random SECRET_KEY via environment variable. "
                    "Example (PowerShell): $env:SECRET_KEY = (python -c \"import secrets; print(secrets.token_hex(32))\")"
                )
                logger.critical(error_msg)
                raise ValueError(error_msg)
            else:
                # 开发环境仅记录警告
                logger.warning(
                    "Using default SECRET_KEY. This is acceptable for development, "
                    "but must be changed in production."
                )
        
        # 检查密钥长度（建议至少 32 字符）
        if len(self.secret_key) < 32:
            logger.warning(
                f"SECRET_KEY is too short ({len(self.secret_key)} characters). "
                "Recommendation: Use at least 32 characters for better security."
            )


# 创建全局配置实例
# 初始化时会按照优先级顺序读取配置：
# 1. 首先检查环境变量（os.environ）
# 2. 如果环境变量不存在，检查 .env 文件
# 3. 如果都不存在，使用代码中的默认值
settings = Settings()

# 验证关键配置（在应用启动时执行）
# 注意：这里只验证，不阻止启动，让应用可以正常初始化
# 如果验证失败，会在日志中记录错误，应用仍可启动（但可能不安全）
try:
    settings.validate_secret_key()
except ValueError as e:
    # 生产环境验证失败会抛出异常，阻止启动
    # 开发环境仅记录警告
    if (settings.environment or "").strip().lower() in {"prod", "production"}:
        raise
