1. 能用 with 绝不手动 close/release
2. 自己会写「可复用」的 __enter__/__exit__ 类
3. 会用 @contextmanager 把生成器秒变上下文

上下文管理器

原生写法(origin) → 生成器简写(generator) → 实战组合(practice)