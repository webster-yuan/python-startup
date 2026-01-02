# enumerate.py
def main():
    txt = ['first line\n', 'second line\n', 'third line\n']
    for idx, line in enumerate(txt, 1):  # 行号从 1 开始
        print(f'{idx}: {line.rstrip()}')


if __name__ == '__main__':
    main()
