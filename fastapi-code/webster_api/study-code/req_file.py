from fastapi import FastAPI, File, UploadFile

from typing import Annotated, Union

from fastapi.responses import HTMLResponse

app = FastAPI()


# bytes:接收二进制形式的数据,常用语处理文件数据,网络通信中的数据传输
@app.post("/files/")
async def create_file_v1(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file_v1(file: UploadFile):
    return {"filename": file.filename}


# File是直接继承的Form,所以文件将作为表单数据上传
# 将路径操作函数参数的类型声明为bytes,FastAPI读取文件,收到bytes形式的内容
# 所有数据都会存储在内存中,所以大多数情况要使用UploadFile


# 使用标准类型注释将默认值设置为None设置可选
@app.post("/files/")
async def create_file_v2(file: Annotated[Union[bytes, None], File()] = None):
    if not file:
        return {"message": "no file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file_v2(file: Union[UploadFile, None] = None):
    if not file:
        return {"message": "no file sent"}
    else:
        return {"file_size": file.size}


# 带有附加元数据的UploadFile
@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File(description="a file read as bytes")] = bytes()
):
    if not file:
        return {"message": "no file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(
    file: Annotated[UploadFile, File(description="a file read as Uploadfile")]
):
    if not file:
        return {"message": "no file sent"}
    else:
        return {"file_size": file.size}


# 多个文件上传
@app.post("/files")
async def create_files_v3(files: Annotated[list[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles")
async def create_upload_files_v3(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
    <body>
    <form action="/files/" enctype="multipart/form-data" method="post>
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post>
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    </body>
    """
    return HTMLResponse(content=content)

# 附带元数据的多文件上传
@app.post("/files")
async def create_files(
    files: Annotated[
        list[bytes], 
        File(description="multiple files as bytes")
    ]
):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles")
async def create_upload_files(
    files: Annotated[list[UploadFile],
                     File(description="multiple files as UploadFile")]
):
    return {"filenames": [file.filename for file in files]}
