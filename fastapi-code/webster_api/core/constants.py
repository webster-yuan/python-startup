"""
认证相关常量定义
避免硬编码，提高代码可维护性
"""

# JWT Token 类型
TOKEN_TYPE_ACCESS = "access"
TOKEN_TYPE_REFRESH = "refresh"

# JWT 标准字段名
JWT_CLAIM_SUB = "sub"  # Subject - JWT 标准中的用户标识字段
JWT_CLAIM_TYPE = "type"  # 自定义字段，用于区分 access 和 refresh token
JWT_CLAIM_EXP = "exp"  # Expiration Time - JWT 标准中的过期时间字段
JWT_CLAIM_ISS = "iss"  # Issuer - JWT 标准中的签发方
JWT_CLAIM_AUD = "aud"  # Audience - JWT 标准中的受众

# HTTP 认证相关
BEARER_TOKEN_TYPE = "bearer"  # OAuth2 Bearer Token 类型
WWW_AUTHENTICATE_HEADER = "WWW-Authenticate"  # HTTP 认证响应头
BEARER_AUTH_SCHEME = "Bearer"  # HTTP Bearer 认证方案（注意：首字母大写）

# 密码相关常量
BCRYPT_MAX_PASSWORD_BYTES = 72  # bcrypt 算法限制：明文密码最大字节数
