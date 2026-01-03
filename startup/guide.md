---

### ✅ L1 必过关（不写这些，代码没法看）

| 主题 | 关键子项 | 最低要求 | 自检小任务 |
|---|---|---|---|
| 虚拟环境 & 依赖管理 | venv / pip / requirements.txt / pip-tools | 任何项目都能`python -m venv venv && pip install -r requirements.txt`一键还原 | 把第6模块的`demo.py`做成包，建venv并在新环境跑通 |
| 代码风格 | PEP8 + black + isort + flake8 | 保存即自动格式化，0 warning | 给上述项目`pre-commit`配齐三件套 |
| 工程结构 | 包/模块/`__init__.py` / `if __name__ == "__main__"` / 入口脚本 | 能写`python -m myproj`启动，也能`pip install -e .`装到任意环境 | 把脚本改成`src/myproj/cli.py`结构 |
| 日志 | `logging`而非`print` | 会配basicConfig+文件Handler+RotatingFileHandler | 把`demo.py`所有`print`换成`logging`，并输出到文件 |

---

### ✅ L2 开发刚需（不写这些，项目无法迭代）

| 主题        | 关键子项                             | 最低要求                   | 自检小任务                            |
|-----------|----------------------------------|------------------------|----------------------------------|
| 测试        | `pytest`+覆盖率`pytest-cov`         | 给核心函数写3个测试，覆盖率>80 %    | 为L1的`myproj`写`tests/test_cli.py` |
| 异常 & 日志追踪 | 自定义异常+日志回溯                       | 出错能一眼定位到行号+参数          | 故意传错文件，日志要打出栈并退出码2               |
| 配置管理      | `pydantic-settings`/toml/ini/env | 代码里不出现裸`os.getenv`到处飘  | 把`-t/--top`默认值挪到配置文件             |
| 类型提示      | `typing`+`mypy --strict`         | 所有公开函数带类型，0 mypy error | 给`demo.py`全量加类型并跑mypy            |
| 调试器       | `pdb`+IDE断点                      | 能在10秒内打断点并看到变量值        | 在递归函数里下断点，看缓存命中                  |

---

### ✅ L3 进阶招式（不写这些，性能/并发/扩展性翻车）

| 主题      | 关键子项                                               | 最低要求                                      | 自检小任务                       |
|---------|----------------------------------------------------|-------------------------------------------|-----------------------------|
| 并发模型    | `concurrent.futures`（Thread/Process池）+ `asyncio`基础 | I/O密集用线程池，CPU密集用进程池，会`async/await`写百行级小服务 | 把统计词频改成线程池同时扫10个文件          |
| 性能剖析    | `cProfile`+`line_profiler`+`timeit`                | 能找出热点函数并给出数量级优化证据                         | 对比`Counter`与手动dict速度差异      |
| 内存优化    | `__slots__` / 生成器 / 对象池                            | 能用生成器改写列表推导，能用`pympler`看到内存峰值下降           | 把读取大文件改成`yield`并监控内存        |
| 数据库     | `SQLAlchemy Core`+连接池                              | 会写CRUD+事务+索引+迁移(`alembic`)                | 把词频结果写进SQLite，再按次数倒序查       |
| 缓存 & 队列 | `redis-py` / `Celery` 基础                           | 能把耗时任务丢到队列，结果缓存5分钟                        | 统计10 G日志时，用Redis缓存已算过的文件MD5 |

---

### ✅ L4 工程化（不写这些，项目无法上线）

| 主题        | 关键子项                             | 最低要求                            | 自检小任务                                  |
|-----------|----------------------------------|---------------------------------|----------------------------------------|
| Docker    | 官方Python镜像+多阶段构建                 | 能写出<50 MB的生产镜像，一键`docker run`启动 | 给`myproj`写`Dockerfile`+`.dockerignore` |
| CI/CD     | GitHub Actions / GitLab CI       | push即跑测试+lint+镜像build           | 每次push自动跑pytest+flake8+mypy            |
| 文档        | `Sphinx`+`mkdocs`+`pdoc`任选一个     | 公开函数有docstring，能一键生成静态站点        | 把`demo.py`的docstring生成HTML             |
| 打包发布      | `pyproject.toml`+`build`+`twine` | 能`pip install`自己上传的包            | 把`myproj`推到Test PyPI并安装验证              |
| 监控 & 日志规范 | `structlog`+`prometheus_client`  | 关键指标能暴露/metrics，日志带trace_id     | 给统计服务加`/metrics`接口，Grafana能画图          |

---

### ✅ L5 领域纵深（选1～2个方向继续钻）

| 方向    | 技术栈示例                                 | 小目标                           |
|-------|---------------------------------------|-------------------------------|
| Web   | FastAPI / Flask + JWT + OAuth2        | 写个「上传日志→返回Top-N词频」的REST接口，带认证 |
| 数据科学  | pandas + numpy + matplotlib / seaborn | 把日志切成小时粒度，画PV折线               |
| 机器学习  | scikit-learn + joblib                 | 用TF-IDF+logistic回归做日志异常检测     |
| 运维自动化 | Ansible / Fabric / Click              | 批量给100台机器跑日志统计并回收结果           |
| 测试进阶  | Hypothesis + pytest-benchmark         | 用策略测试生成任意日志，benchmark性能       |

---

### 30 天可落地路线（按每天1～2小时）

| 周  | 目标                   | 产出                    |
|----|----------------------|-----------------------|
| W1 | L1全部+黑盒重构`demo.py`   | 可安装包+black+flake8零警告  |
| W2 | L2测试+类型+mypy+配置      | pytest覆盖率>80%，mypy零错误 |
| W3 | L3并发+数据库+性能          | 线程池10文件并发，结果入库，性能报告   |
| W4 | L4 Docker+CI+文档+PyPI | push自动测试&镜像，文档站点在线可看  |

---

把上面每层的“自检小任务”挨个跑通，你就从“语法会了”进化到“工程能上手”，再往后就是选领域深耕+读源码+参与开源，路线就彻底打开了。  
任何一步需要示例模板或卡壳，随时@我。祝你打怪愉快！