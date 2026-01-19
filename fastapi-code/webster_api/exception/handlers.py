"""
异常处理器模块
将所有异常处理器集中管理，避免 main.py 代码过长
"""
import logging
from starlette.responses import JSONResponse
from fastapi import Request

from webster_api.exception.base import BusinessException, SystemException, InfraException

logger = logging.getLogger(__name__)


def business_exception_handler(request: Request, exc: BusinessException) -> JSONResponse:
    """
    业务异常处理器
    处理所有业务层抛出的异常（BusinessException 及其子类）
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


def system_exception_handler(request: Request, exc: SystemException) -> JSONResponse:
    """
    系统异常处理器
    处理系统级别的异常
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


def infra_exception_handler(request: Request, exc: InfraException) -> JSONResponse:
    """
    基础设施异常处理器
    处理基础设施相关的异常
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


# 注意：ValueError 和 AttributeError 处理器已移除
# 
# 架构原则：
# - 技术异常（ValueError、AttributeError 等）应该在 Service 层转换为业务异常
# - 如果技术异常暴露给用户，说明代码有问题，应该通过测试和代码审查发现并修复
# - 不应该用全局处理器兜底，而应该确保代码符合规范
#
# 示例：Service 层应该这样处理
# try:
#     hashed_password = get_password_hash(password)
# except (ValueError, AttributeError) as e:
#     raise PasswordValidationError("Password validation failed")  # 转换为业务异常


def general_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """
    捕获所有未预期的异常，返回友好的错误信息
    
    注意：这个处理器会捕获所有未被前面处理器处理的异常
    包括数据库错误、第三方库错误等未预期的异常
    
    安全考虑：
    - 不在响应中暴露内部错误详情（防止信息泄露）
    - 将详细的错误信息记录到日志（用于调试）
    """
    # 记录异常详情到日志（用于调试）
    logger.error(
        f"Unhandled exception: {type(exc).__name__}: {str(exc)}",
        exc_info=exc
    )
    
    # 返回友好的错误信息给用户（不暴露内部错误详情）
    return JSONResponse(
        status_code=500,
        content={
            "detail": "An internal server error occurred. Please try again later."
        }
    )
