def filter_main():
    nums = range(20)
    # 将一个指定的判断函数（或None），依次应用到一个可迭代对象的每个元素上，
    # 筛选出所有 “判断结果为真” 的元素，返回一个filter迭代器（包含所有符合条件的元素）
    # 所以function可以是 匿名函数（lambda，适用于简单筛选逻辑），自定义函数（返回值bool）等
    filter_nums = filter(lambda x: x % 2 == 0, nums)
    print(list(filter_nums))


filter_main()  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
