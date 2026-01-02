import sqlite3
from contextlib import contextmanager


@contextmanager
def transaction(db_path):
    conn = sqlite3.connect(db_path)
    conn.execute('BEGIN')
    try:
        yield conn  # 把链接交给 with 语句
    except Exception:
        conn.rollback()
        raise
    else:
        conn.commit()
    finally:
        conn.close()


if __name__ == '__main__':
    with transaction('example') as connection:
        connection.execute('sql1')

    print('auto commit and close')
