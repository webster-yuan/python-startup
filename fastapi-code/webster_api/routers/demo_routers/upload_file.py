from typing import Annotated

from fastapi import APIRouter, UploadFile, File

upload_file_router = APIRouter(prefix="/upload", tags=["upload"])


@upload_file_router.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    """
    File: 文件参数，与 Body 一样，实际是继承自 Form 的字类
    将您的路径操作函数参数的类型声明为 bytes，FastAPI 将为您读取文件，
    您将以 bytes 的形式接收内容。
    请注意，这意味着整个内容将存储在内存中。这对于小文件来说效果很好
    """
    return {"file_size": len(file)}


@upload_file_router.post("/upload_file")
async def create_file(file: UploadFile):
    """
    1. 您不必在参数的默认值中使用 File()。
    2. 它使用“spooled”文件
    文件存储在内存中，直到达到最大大小限制，超过限制后将存储在磁盘上。
    这意味着它适用于图像、视频、大型二进制文件等大型文件，而不会消耗所有内存。
    3. 您可以获取上传文件的元数据。
    它具有一个类似文件的 async 接口。
    它公开了一个实际的 Python SpooledTemporaryFile 对象，您可以直接将其传递给期望类似文件对象的其他库。

    节省内存：文件会在达到特定大小后转存到磁盘，这减少了内存消耗。
    高并发支持：异步操作可以让服务器在等待文件 I/O 时继续处理其他请求。
    """
    filename = file.filename
    content_type = file.content_type
    # 读取前100个字节
    file_content = await file.read(100)

    # 进行文件指针操作：将文件指针跳到文件开头
    await file.seek(0)

    # 写入数据到文件
    full_content = await file.read()
    with open(f"upload_{filename}", "wb") as f:
        await f.write(full_content)

    return {
        "filename": filename,
        "content_type": content_type,
        "file_content_preview": file_content.decode("utf-8", errors="ignore"),
        "full_content_preview": full_content.decode("utf-8", errors="ignore")
    }


@upload_file_router.post("/files/")
async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
    return {"file_size": len(file)}


@upload_file_router.post("/upload_file/")
async def create_upload_file(
        file: Annotated[UploadFile | None, File(description="A file read as UploadFile")] = None,
):
    """
    元数据：description
    """
    return {"filename": file.filename}


# 多文件上传
@upload_file_router.post("/files/")
async def create_files(files: Annotated[list[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}


@upload_file_router.post("/upload_files/")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}
